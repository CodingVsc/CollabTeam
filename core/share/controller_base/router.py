from typing import Callable

from fastapi import APIRouter

from core.share.controller_base.base import DynamicParamMeta
from core.share.controller_base.consts import (
    DEFAULT_METHODS,
    METHOD_WRAPPER,
    SINGLE_METHODS,
    Method,
)


class ControllerRouter(APIRouter):
    def add_endpoint(self, path: str, view_func: Callable, method: str, status_code=200):
        self.add_api_route(path, view_func, methods=[method], status_code=status_code)


def add_routers(
    controller: DynamicParamMeta,
    methods: set[Method] = DEFAULT_METHODS,
    exclude_methods: set[Method] = {},
) -> ControllerRouter:
    default_router = ControllerRouter()

    for method_name in methods:
        if method_name not in exclude_methods:
            add_path(controller, method_name, default_router)

    return default_router


def add_path(controller: DynamicParamMeta, method_name: Method, default_router: ControllerRouter):
    method = getattr(controller(), method_name.name)
    path = f"/{{{controller.url_field}}}" if method_name in SINGLE_METHODS else "/"
    default_router.add_endpoint(path, method, METHOD_WRAPPER[method_name])
