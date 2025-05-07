from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from .admin import admin_router
from .admin.utils import get_client
from .admin.filters import IsAdmin


main_router = Router(name='main_router')
main_router.include_router(admin_router)

is_admin = IsAdmin()


async def get_user_token(tg_id: int) -> None:
    async with get_client() as client:
        response = await client.get(f'/users/token?tg_id={tg_id}')
        token = response.json().get('token')
        return token


@main_router.message(CommandStart(), is_admin)
async def handle_start_cmd(message: Message) -> None:
    user_token = await get_user_token(message.from_user.id)

    if user_token is None:
        await message.answer('Доступ запрещен')
        return

    url = f'http://localhost:5173/token/{user_token}'
    await message.answer(url)
