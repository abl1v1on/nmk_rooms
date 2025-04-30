import asyncio
from aiogram import Bot, Dispatcher

from config import settings
from app import main_router


bot = Bot(token=settings.bot.token)
dp = Dispatcher()
dp.include_router(main_router)


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
