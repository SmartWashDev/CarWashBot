import logging
import sys

from pydantic import ConfigDict

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(extra='ignore')  # Игнорирование лишних переменных в env файле

    # Debug
    DEBUG: bool = False
    SENTRY_DSN: str = ''

    # Application
    TELEGRAM_TOKEN: str

    # Nats


settings = Settings(_env_file='.env')

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
