from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.config import settings


root_dispatcher = Dispatcher()


@root_dispatcher.message(CommandStart)
async def command_start_handler(message: Message) -> None:
    await message.answer('я работаю')


async def run_bot():
    bot = Bot(settings.TELEGRAM_TOKEN)
    await root_dispatcher.start_polling(bot)
