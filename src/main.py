from fastapi import FastAPI

from core.config.settings import settings
from src.routers import get_apps_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version=settings.version,
    swagger_ui_parameters={"docExpansion": "none"},
)

app.include_router(get_apps_router())
