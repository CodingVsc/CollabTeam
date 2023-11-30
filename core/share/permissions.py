from abc import ABC, abstractmethod

from core.share.controller_base.base import UserModel


class AbstractPermission(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def check_permissions(self, user: UserModel) -> UserModel:
        raise NotImplementedError
