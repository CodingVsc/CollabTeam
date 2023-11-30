from typing import Callable, Dict, List, Type

from pydantic import BaseModel
from starlette.responses import Response

from .base import DynamicParamMeta, PyModel, Service, SlugField, UserModel


class Controller(metaclass=DynamicParamMeta):
    pydantic_models: Dict[str, Type[BaseModel]]
    permissions: Dict[str, Type[Callable]]
    service: Service
    url_field: str = "pk"


class ControllerMixin:
    async def all(self, user: UserModel) -> List[PyModel]:
        return await self.service.all(user)

    async def list(self, user: UserModel) -> List[PyModel]:
        return await self.service.list(user=user)

    async def create(self, model: PyModel, user: UserModel) -> PyModel:
        return await self.service.add(model, user)

    async def update(self, pk: SlugField, model: PyModel, user: UserModel) -> PyModel:
        return await self.service.update(pk, model, user)

    async def partial_update(self, pk, model: PyModel = None, user: UserModel = None) -> PyModel:
        return await self.service.partial_update(pk, model, user)

    async def retrieve(self, pk: SlugField, user: UserModel) -> PyModel:
        return await self.service.retrieve(pk, user)

    async def delete(self, pk: SlugField, user: UserModel) -> Response:
        await self.service.delete(pk, user)
        return Response(status_code=204)


class ControllerListCreateMixin:
    async def all(self, user: UserModel) -> List[PyModel]:
        return await self.service.all(user=user)

    async def list(self, user: UserModel) -> List[PyModel]:
        return await self.service.list(user=user)

    async def create(self, model: PyModel, user: UserModel) -> PyModel:
        return await self.service.add(model=model, user=user)
