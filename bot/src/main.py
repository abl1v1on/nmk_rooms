import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import settings


bot = Bot(token=settings.bot.token)
dp = Dispatcher()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Start')
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        print('Stop')
