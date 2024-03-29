from typing import List

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from core.db.session import AsyncDatabaseSession
from core.share.controller_base.base import PyModel, UserModel
from core.share.errors import (
    AlreadyExistError,
    DBError,
    MultipleRowsFoundError,
    NoRowsFoundError,
)
from core.share.repository import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository) -> None:
        self.repository = repository

    async def add(self, model: PyModel = None, user: UserModel = None):
        try:
            return await self.repository.create(model.model_dump())
        except AlreadyExistError as e:
            raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

    async def bulk_add(self, model: List[PyModel], user: UserModel = None):
        data = [model_data.model_dump() for model_data in model]
        try:
            return await self.repository.bulk_create(data)
        except AlreadyExistError as e:
            raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

    async def get_or_add(self, pk, data: dict):
        try:
            return await self.repository.get_single(id=pk)
        except NoRowsFoundError:
            await self.repository.create(data)
        return await self.repository.get_single(id=pk)

    async def all(self, user: UserModel = None):
        return await self.repository.all()

    async def filter(self, user: UserModel = None, filters: dict = None):
        return await self.repository.filter(filters=filters)

    async def retrieve(self, pk, model: PyModel = None, user: UserModel = None):
        try:
            return await self.repository.get_single(id=pk)
        except (NoRowsFoundError, MultipleRowsFoundError):
            raise HTTPException(HTTP_404_NOT_FOUND)

    async def update(self, pk, model: PyModel = None, user: UserModel = None):
        try:
            return await self.repository.update(model.model_dump(), {"id": pk})
        except NoRowsFoundError as e:
            raise HTTPException(HTTP_404_NOT_FOUND, f"{e} does not exist")
        except (DBError, AlreadyExistError) as e:
            raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

    async def partial_update(self, pk, model: PyModel = None, user: UserModel = None):
        data = model.model_dump(exclude_unset=True)
        try:
            return await self.repository.update(data, {"id": pk})
        except NoRowsFoundError as e:
            raise HTTPException(HTTP_404_NOT_FOUND, f"{e} does not exist")
        except (DBError, AlreadyExistError) as e:
            raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

    async def delete(self, pk, model: PyModel = None, user: UserModel = None):
        try:
            return await self.repository.delete(id=pk)
        except NoRowsFoundError as e:
            raise HTTPException(HTTP_404_NOT_FOUND, f"{e} does not exist")


class GenericService:
    def __init__(self, model, service=BaseService, repository=BaseRepository):
        self.model = model

        class Repository(repository):
            model = self.model

        self.repository = Repository(db_session=AsyncDatabaseSession().session)
        self.service = service(repository=self.repository)

    @property
    def get_service(self):
        return self.service
