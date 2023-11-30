import functools
import inspect
from collections import defaultdict
from inspect import Parameter, Signature
from types import FunctionType
from typing import Any, Callable, List, NewType, TypeVar, _GenericAlias

from fastapi import Depends
from pydantic import BaseModel, create_model

PyModel = NewType("PyModel", BaseModel)

UserModel = NewType("UserModel", BaseModel)

SlugField = TypeVar("SlugField")

Service = TypeVar("Service")

ClassName = NewType("ClassName", str)

T = TypeVar("T")


def change_annotation(
    annotation: Any, return_type: PyModel | None = None, slug: SlugField | None = None
):
    if annotation is PyModel:
        assert return_type is not None, "no py_model attr"
        return return_type
    elif annotation is SlugField:
        assert slug is not None, "no slug attr"
        return slug
    elif isinstance(annotation, _GenericAlias):
        # change annotation for generic typehints like this: list[PyModel]
        args = getattr(annotation, "__args__")  # subtype annotation: e.g: list[PyModel] -> PyModel
        origin = getattr(annotation, "__origin__")  # container annotation: e.g : list[int] -> list
        new_args = tuple(map(lambda x: change_annotation(x, return_type, slug), args))
        return _GenericAlias(origin, new_args, inst=False, name=origin.__name__)
    else:
        return annotation


def fetch_class_annotation(
    annotation: type, return_type: PyModel | None = None, slug: SlugField | None = None
):
    if not issubclass(annotation, BaseModel):
        return annotation

    fields = {}
    for key, value in annotation.model_fields.items():
        value.annotation = change_annotation(value.annotation, return_type, slug)
        fields[key] = (value.annotation, value.default)
    return create_model(
        "ResponseModel",
        **fields,
        __base__=annotation,
    )


def fetch_return_annotation(sig: Signature, return_type):
    return_annotation = sig.return_annotation
    if inspect.isclass(return_annotation):
        return fetch_class_annotation(return_annotation, return_type)
    else:
        return change_annotation(return_annotation, return_type)


class DynamicParamMeta(type):
    def __new__(cls, name: ClassName, bases: tuple[type], attrs: dict[str, Any]):
        if name == "Controller":
            return super().__new__(cls, name, bases, attrs)
        assert "pydantic_models" in attrs, "View not implemented py_models attr"
        assert "permissions" in attrs, "View not implemented permissions attr"

        py_models = attrs["pydantic_models"]
        response_models = attrs.get("response_models")

        perm = attrs["permissions"]
        slug_field = attrs.get("slug_field_type")

        for base in bases:
            for attr_name, attr_value in base.__dict__.items():
                if inspect.isfunction(attr_value) and attr_name not in attrs:
                    attrs[attr_name] = cls.deepcopy_func(attr_value)
                if attr_name == "url_field" and attr_name not in attrs:
                    attrs[attr_name] = attr_value

        for attr_name, attr_value in attrs.items():
            if not inspect.isfunction(attr_value):
                continue

            return_type = cls.fetch_response_model(py_models, response_models, attr_name)
            attrs[attr_name] = cls.wrap_method(
                attr_value,
                input_type=py_models[attr_name],
                output_type=return_type,
                perm=perm[attr_name],
                slug_field=slug_field,
            )
        return super().__new__(cls, name, (), attrs)

    @classmethod
    def fetch_response_model(
        cls,
        py_models: defaultdict[str, PyModel],
        response_models: dict[str, PyModel],
        attr_name: str,
    ) -> PyModel:
        if response_models is None:
            return py_models[attr_name]
        return response_models.get(attr_name, py_models[attr_name])

    @staticmethod
    def deepcopy_func(f) -> Callable:
        """Make deepcopy of method from base class and later put it to attrs for current class"""
        g = FunctionType(
            f.__code__,
            f.__globals__,
            name=f.__name__,
            argdefs=f.__defaults__,
            closure=f.__closure__,
        )
        g = functools.update_wrapper(g, f)
        g.__kwdefaults__ = f.__kwdefaults__
        return g

    @staticmethod
    def wrap_method(
        method: Callable[..., T],
        input_type: PyModel = None,
        output_type: PyModel = None,
        perm=None,
        slug_field: SlugField = None,
    ) -> Callable[..., T]:
        sig = inspect.signature(method)
        req_parameters: List[Parameter] = []
        def_parameters: List[Parameter] = []
        for parameter in sig.parameters.values():
            new_parameter = change_parameter_signature(parameter, input_type, slug_field, perm)
            if parameter.default is Parameter.empty:
                req_parameters.append(new_parameter)
            else:
                def_parameters.append(new_parameter)

        parameters = req_parameters + def_parameters
        return_annotation = fetch_return_annotation(sig, output_type)

        sig = sig.replace(parameters=parameters, return_annotation=return_annotation)

        method.__signature__ = sig

        return method


def change_parameter_signature(
    parameter: Parameter, input_type: PyModel, slug_field: SlugField, perm
) -> Parameter:
    annotation = change_annotation(parameter.annotation, input_type, slug_field)
    parameter = parameter.replace(annotation=annotation)
    if parameter.annotation is UserModel:
        parameter = parameter.replace(default=Depends(perm))
    return parameter
