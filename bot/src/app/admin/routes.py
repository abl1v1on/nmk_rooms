import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from string import ascii_letters, digits

from . import utils
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
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email) is None:
        await message.answer('Введите валидный email')
        return

    await state.update_data(email=email)
    await message.answer('Введите имя пользователя')
    await state.set_state(CreateUserForm.first_name)


@router.message(CreateUserForm.first_name)
async def set_user_first_name_state(message: Message, state: FSMContext) -> None:
    first_name = message.text

    if not (2 <= len(first_name) <= 30):
        await message.answer(
            'Длина имени должна быть от 2 до 30 (включительно) символов'
        )
        return

    allowed_letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    if not set(first_name.lower()).issubset(allowed_letters):
        await message.answer('Имя может содержать только русские символы')
        return

    await state.update_data(first_name=first_name)
    await message.answer('Введите фамилию пользователя')
    await state.set_state(CreateUserForm.last_name)


@router.message(CreateUserForm.last_name)
async def set_user_last_name_state(message: Message, state: FSMContext) -> None:
    last_name = message.text

    if not (2 <= len(last_name) <= 30):
        await message.answer(
            'Длина фамилии должна быть от 2 до 30 (включительно) символов'
        )
        return

    allowed_letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    if not set(last_name.lower()).issubset(allowed_letters):
        await message.answer('Фамилия может содержать только русские символы')
        return

    await state.update_data(last_name=last_name)
    await message.answer('Введите Telegram ID пользователя')
    await state.set_state(CreateUserForm.tg_id)


@router.message(CreateUserForm.tg_id)
async def set_user_tg_id_state(message: Message, state: FSMContext) -> None:
    tg_id = message.text

    try:
        tg_id = int(tg_id)
    except ValueError:
        await message.answer(
            'Telegram ID пользователя может состоять только из цифр'
        )
        return

    await state.update_data(tg_id=tg_id)
    await message.answer('Придумайте пароль')
    await state.set_state(CreateUserForm.password)


@router.message(CreateUserForm.password)
async def set_user_password_state(message: Message, state: FSMContext) -> None:
    password = message.text

    if not (8 <= len(password) <= 30):
        await message.answer(
            'Длина пароля должна быть от 8 до 30 (включительно) символов'
        )
        return

    if password.isdigit():
        await message.answer('Пароль не может состоять только из цифр')
        return

    has_upper = False
    has_special_char = False

    special_chars = '!@#$%^&*()'
    allowed_letters = ascii_letters + digits + special_chars

    for char in password:
        if char.isupper() and has_upper is False:
            has_upper = True

        if char in special_chars and has_special_char is False:
            has_special_char = True

        if char not in allowed_letters:
            await message.answer(
                'Пароль должен содержать латинские символы, цифры и спец-символы'
            )
            return

    if not has_upper:
        await message.answer('Пароль должен содержать хотя бы одну заглавную букву')
        return

    if not has_special_char:
        await message.answer('Пароль должен содержать хотя бы один спец-символ')
        return

    await state.update_data(password=password)

    user = await state.get_data()

    try:
        await utils.create_user(user)
        await message.answer('✅ Пользователь успешно добавлен')
    except:
        await message.answer('❌ При создании пользователя произошла ошибка')
    finally:
        await state.clear()


@router.message(F.text == '👥 Список пользователей 👥', is_admin)
async def handle_users_list_cmd(message: Message) -> None:
    await message.answer('\n'.join(await utils.get_users()))


@router.message(F.text == '🗺 Список локаций 🗺', is_admin)
async def handle_locations_list_cmd(message: Message) -> None:
    await message.answer('\n'.join(await utils.get_locations()))
