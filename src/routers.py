from fastapi import APIRouter

from src.auth.routers import auth_router
from src.users.routers import users_router
from src.boards.routers import board_router


def get_apps_router():
    router = APIRouter()
    router.include_router(board_router)
    router.include_router(auth_router)
    router.include_router(users_router)
    return router
