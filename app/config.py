import logging
import sys

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',  # Игнорирование лишних переменных в env файле
        env_file='.env',
        env_file_encoding='utf-8',
    )

    # Debug
    DEBUG: bool = False
    SENTRY_DSN: str = ''

    # Application
    TELEGRAM_TOKEN: str
    TELEGRAM_USER_ID: int

    # Nats
    NATS_URL: str
    NATS_SUBJECT: str


settings = Settings()

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
