from celery import Celery
from pydantic_settings import BaseSettings


class Settings:
    CELERY_IMPORTS = [
        "src.users.utils.tasks",
    ]


settings = Settings()


class ConfigCelery(BaseSettings):
    BROKER_URL: str
    RESULT_BACKEND: str
    NUMBER_OF_WORKERS: int = 1

    class Config:
        env_prefix = "CELERY_"


config_celery = ConfigCelery()

celery = Celery(__name__, config_source=settings)
celery.conf.broker_url = config_celery.BROKER_URL
celery.conf.result_backend = config_celery.RESULT_BACKEND
celery.conf.worker_concurrency = config_celery.NUMBER_OF_WORKERS
