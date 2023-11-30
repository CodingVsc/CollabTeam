from typing import List

from core.share.controller_base.base import PyModel, UserModel


class BulkCreateMixin:
    """Use this mixin only for mass creation"""

    async def create(self, model: List[PyModel], user: UserModel) -> PyModel:
        """This method will override the base 'create' method and works like 'bulk_create'"""
        return await self.__bulk_create(model, user)

    async def __bulk_create(self, model: List[PyModel], user: UserModel) -> PyModel:
        return await self.service.bulk_add(model, user)
