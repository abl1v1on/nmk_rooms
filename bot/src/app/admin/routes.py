from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .filters import IsAdmin
from .keyboards import admin_kb
from .forms import CreateUserForm


router = Router(name='admin_router')
is_admin = IsAdmin()


@router.message(Command('admin'), is_admin)
async def handle_admin_cmd(message: Message) -> None:
    await message.answer(
        'Добро пожаловать в админ панель!',
        reply_markup=admin_kb
    )


@router.message(F.text == '👤 Добавить пользователя 👤', is_admin)
async def handle_add_user_cmd(message: Message, state: FSMContext) -> None:
    await message.answer('Введите email пользователя')
    await state.set_state(CreateUserForm.email)


@router.message(CreateUserForm.email)
async def set_user_email_state(message: Message, state: FSMContext) -> None:
    email = message.text

    # TODO: добавить валидацию для email-а
    await state.update_data(email=email)
    await message.answer('Введите имя пользователя')
    await state.set_state(CreateUserForm.first_name)


@router.message(CreateUserForm.first_name)
async def set_user_first_name_state(message: Message, state: FSMContext) -> None:
    first_name = message.text

    # TODO: добавить валидацию для имени пользователя
    await state.update_data(first_name=first_name)
    await message.answer('Введите фамилию пользователя')
    await state.set_state(CreateUserForm.last_name)


@router.message(CreateUserForm.last_name)
async def set_user_last_name_state(message: Message, state: FSMContext) -> None:
    last_name = message.text

    # TODO: добавить валидацию для фамилии пользователя
    await state.update_data(last_name=last_name)
    await message.answer('Введите Telegram ID пользователя')
    await state.set_state(CreateUserForm.tg_id)


@router.message(CreateUserForm.tg_id)
async def set_user_tg_id_state(message: Message, state: FSMContext) -> None:
    tg_id = message.text

    # TODO: добавить валидацию для Telegram ID пользователя
    await state.update_data(tg_id=tg_id)
    await message.answer('Придумайте пароль')
    await state.set_state(CreateUserForm.password)


@router.message(CreateUserForm.password)
async def set_user_password_state(message: Message, state: FSMContext) -> None:
    password = message.text

    # TODO: добавить валидацию для пароля пользователя
    await state.update_data(password=password)

    data = await state.get_data()
    await message.answer(str(data))

    await state.clear()
