import asyncio

import sentry_sdk

from app.bot import run_bot
from app.config import settings


sentry_sdk.init(dsn=settings.SENTRY_DSN)

asyncio.run(run_bot())
