import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CollabTeam"
    debug: bool = bool(os.environ.get("DEBUG"))
    secret_key: str = os.environ.get("SECRET_KEY")
    cors_allowed_origins: str = os.environ.get("CORS_ALLOWED_ORIGINS")
    version: str = "0.1"


settings = Settings()
