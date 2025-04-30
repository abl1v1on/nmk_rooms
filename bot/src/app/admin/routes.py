from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from .filters import IsAdmin
from .keyboards import admin_kb


router = Router(name='admin_router')
is_admin = IsAdmin()


@router.message(Command('admin'), is_admin)
async def handle_admin_cmd(message: Message) -> None:
    await message.answer(
        'Добро пожаловать в админ панель!',
        reply_markup=admin_kb
    )


@router.message(F.text == '👤 Добавить пользователя 👤', is_admin)
async def handle_add_user_cmd(message: Message) -> None:
    await message.answer('Тут будет добавление пользователя')
