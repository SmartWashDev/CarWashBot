import dataclasses
import json

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import URLInputFile
from nats.aio.msg import Msg

from app.config import settings
from app.nats import NatsMessageProcessor


@dataclasses.dataclass
class DetectedCarWithPlate:
    image_url: str
    plate_number: str


root_dispatcher = Dispatcher()
bot = Bot(settings.TELEGRAM_TOKEN)

MESSAGE = r'''
**Новое авто**
*Гос\. Номер*: `{0}`
'''


async def process_nats_messages(message: Msg) -> None:
    data = message.data.decode()
    payload = DetectedCarWithPlate(**json.loads(data))
    file = URLInputFile(payload.image_url)

    await bot.send_photo(
        settings.TELEGRAM_USER_ID,
        photo=file,
        caption=MESSAGE.format(payload.plate_number),
        parse_mode=ParseMode.MARKDOWN_V2,
    )


async def run_bot():
    nats_processor = NatsMessageProcessor(
        nats_url=settings.NATS_URL,
        nats_subject=settings.NATS_SUBJECT,
        callback=process_nats_messages,
    )
    await nats_processor.run()
    await root_dispatcher.start_polling(bot)
    await nats_processor.stop()
