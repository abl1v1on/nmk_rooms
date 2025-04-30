from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from .filters import IsAdmin


router = Router(name='admin_router')
is_admin = IsAdmin()


@router.message(Command('admin'), is_admin)
async def handle_admin_cmd(message: Message) -> None:
    await message.answer('Добро пожаловать в админ панель!')
