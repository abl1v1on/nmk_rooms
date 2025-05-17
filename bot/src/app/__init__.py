from aiogram import Router
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode

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
    url = f"https://4525-77-238-239-82.ngrok-free.app/"
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='🔗 Перейти на сайт',
                    web_app=WebAppInfo(url=url)
                )
            ]
        ]
    )

    await message.answer('test', reply_markup=kb)
