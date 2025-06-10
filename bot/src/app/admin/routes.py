import re
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, or_f
from aiogram.fsm.context import FSMContext
from string import ascii_letters, digits

from . import utils
from . import keyboards
from .filters import IsAdmin
from .forms import (
    CreateUserForm,
    CreateLocationForm,
    CreateRoomForm,
    CreateEquipmentForm,
    AddEquipmentsToRoomForm,
    GetUserBookings,
    DeleteBookingForm
)


router = Router(name='admin_router')
is_admin = IsAdmin()


@router.message(or_f(Command('admin'), F.text == '⬅️ Назад ⬅️'), is_admin)
async def handle_admin_cmd(message: Message) -> None:
    await message.answer(
        'Добро пожаловать в админ панель!',
        reply_markup=keyboards.admin_kb
    )


@router.message(F.text == '👥 Пользователи 👥', is_admin)
async def handle_users_admin_cmd(message: Message) -> None:
    await message.answer(
        'Выберите действие',
        reply_markup=keyboards.admin_users_kb
    )


@router.message(F.text == '🗺 Локации 🗺', is_admin)
async def handle_locations_admin_cmd(message: Message) -> None:
    await message.answer(
        'Выберите действие',
        reply_markup=keyboards.admin_locations_kb
    )


@router.message(F.text == '🏠 Конференц залы 🏠', is_admin)
async def handle_rooms_admin_cmd(message: Message) -> None:
    await message.answer(
        'Выберите действие',
        reply_markup=keyboards.admin_rooms_kb
    )


@router.message(F.text == '💻 Оборудование 💻')
async def handle_equipments_admin_cmd(message: Message) -> None:
    await message.answer(
        'Выберите действие',
        reply_markup=keyboards.admin_equipments_kb
    )



@router.message(F.text == '👤 Добавить пользователя 👤', is_admin)
async def handle_add_user_cmd(message: Message, state: FSMContext) -> None:
    await message.answer('Введите email пользователя')
    await state.set_state(CreateUserForm.email)


@router.message(CreateUserForm.email)
async def set_user_email_state(message: Message, state: FSMContext) -> None:
    # TODO: добавить проверку на существующий email
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
    # TODO: добавить проверку на существующий Telegram ID
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


@router.message(F.text == '🏠 Забронированые залы пользователя 🏠', is_admin)
async def handle_user_bookings_cmd(message: Message, state: FSMContext) -> None:
    await message.answer('Введите ID пользователя')
    await state.set_state(GetUserBookings.user_id)


@router.message(GetUserBookings.user_id)
async def set_user_id_state(message: Message, state: FSMContext) -> None:
    user_id = message.text

    if not user_id.isdigit():
        await message.answer('Введите ID пользователя')
        return

    if int(user_id) <= 0:
        await message.answer(
            'ID пользователя не может быть меньше или равен нулю, введите валидное значение'
        )
        return

    await state.update_data(user_id=int(user_id))
    state_data = await state.get_data()

    try:
        bookings = await utils.get_user_bookings(state_data['user_id'])
        await message.answer(f'\n\n{'=' * 40}\n\n'.join(bookings))
    except:
        await message.answer(
            'При попытке отправки запроса произошла ошибка. Убедитесь, что пользвоатель с таким ID существует'
        )
    finally:
        await state.clear()


@router.message(F.text == '🗺 Добавить локацию 🗺', is_admin)
async def handle_add_location_cmd(message: Message, state: FSMContext) -> None:
    await message.answer('Введите адрес')
    await state.set_state(CreateLocationForm.address)


@router.message(CreateLocationForm.address)
async def set_location_address_state(message: Message, state: FSMContext) -> None:
    # TODO: добавить проверку на существующий адрес
    address = message.text

    if not (5 <= len(address) <= 255):
        await message.answer(
            'Длина адреса должна быть от 5 до 255 (включительно) символов'
        )
        return

    await state.update_data(address=address)
    location = await state.get_data()

    try:
        await utils.create_location(location)
        await message.answer('✅ Локация успешно добавлена')
    except:
        await message.answer('❌ При создании локации произошла ошибка')
    finally:
        await state.clear()


@router.message(F.text == '🗺 Список локаций 🗺', is_admin)
async def handle_locations_list_cmd(message: Message) -> None:
    await message.answer('\n'.join(await utils.get_locations()))


@router.message(F.text == '🏠 Добавить конференц зал 🏠', is_admin)
async def handle_add_room_cmd(message: Message, state: FSMContext) -> None:
    await message.answer('Введите номер зала')
    await state.set_state(CreateRoomForm.number)


@router.message(CreateRoomForm.number)
async def set_room_number_state(message: Message, state: FSMContext) -> None:
    # TODO: добавить проверку на существующий номер зала
    number = message.text

    try:
        number = int(number)
    except ValueError:
        await message.answer('Номер зала должен быть целым числом')
        return

    if number <= 0:
        await message.answer('Номер зала должен быть больше нуля')
        return

    await state.update_data(number=number)
    await message.answer('Введите вместимость зала')
    await state.set_state(CreateRoomForm.capacity)


@router.message(CreateRoomForm.capacity)
async def set_room_capacity_state(message: Message, state: FSMContext) -> None:
    capacity = message.text

    try:
        capacity = int(capacity)
    except ValueError:
        await message.answer('Вместимость зала должна быть целым числом')
        return

    if capacity <= 0:
        await message.answer('Вместимость зала должна быть больше нуля')
        return

    await state.update_data(capacity=capacity)
    await message.answer('Введите описание зала')
    await state.set_state(CreateRoomForm.description)


@router.message(CreateRoomForm.description)
async def set_room_description_state(message: Message, state: FSMContext) -> None:
    description = message.text

    if not (5 <= len(description) <= 100):
        await message.answer(
            'Длина описание должна быть от 5 до 100 (включительно) символов'
        )
        return

    await state.update_data(description=description)
    await message.answer(
        'Введите ссылку на изображение (или "-", если оно не требуется)'
    )
    await state.set_state(CreateRoomForm.image)


@router.message(CreateRoomForm.image)
async def set_room_image_state(message: Message, state: FSMContext) -> None:
    # TODO: добавить валидацию на соответствие ссылке
    image = message.text

    if image == '-':
        image = None
    else:
        if len(image) >= 10000:
            await message.answer('Ссылка на изображение слишком длинная')
            return

    await state.update_data(image=image)
    await message.answer('Введите ID локации')
    await state.set_state(CreateRoomForm.location_id)


@router.message(CreateRoomForm.location_id)
async def set_room_location_id_state(message: Message, state: FSMContext) -> None:
    # TODO: добавить проверку на существование локации с введенным Location ID
    location_id = message.text

    try:
        location_id = int(location_id)
    except ValueError:
        await message.answer('ID локации должен быть целым числом')
        return

    if location_id <= 0:
        await message.answer('ID локации должен быть больше нуля')
        return

    await state.update_data(location_id=location_id)
    room = await state.get_data()

    try:
        await utils.create_room(room)
        await message.answer('✅ Зал успешно добавлен')
    except:
        await message.answer('❌ При создании зала произошла ошибка')
    finally:
        await state.clear()


@router.message(F.text == '💻 Добавить оборудование в зал 💻', is_admin)
async def handle_add_equipments_to_room_cmd(
        message: Message,
        state: FSMContext
    ) -> None:
    await message.answer('Введите ID зала')
    await state.set_state(AddEquipmentsToRoomForm.room_id)


@router.message(AddEquipmentsToRoomForm.room_id)
async def set_room_id_state(message: Message, state: FSMContext) -> None:
    # TODO: добавить проверку на существование выбранной комнаты
    room_id = message.text

    try:
        room_id = int(room_id)
    except ValueError:
        await message.answer('ID комнаты должен быть целым числом')
        return

    if room_id <= 0:
        await message.answer('ID комнаты должен быть больше нуля')
        return

    await state.update_data(room_id=room_id)
    await message.answer(
        'Введите названия оборудований через запятую (проектор, планшет, ноутбук)'
    )
    await state.set_state(AddEquipmentsToRoomForm.equipments)


@router.message(AddEquipmentsToRoomForm.equipments)
async def set_rooms_equipments_state(message: Message, state: FSMContext) -> None:
    equipments = list(map(
        lambda equipment: {'name': equipment.strip().capitalize()},
        message.text.split(',')
    ))

    await state.update_data(equipments=equipments)

    data = await state.get_data()

    try:
        await utils.add_equipments_to_room(data)
        await message.answer('✅ Оборудование успешно добавлено')
    except:
        await message.answer(
            '❌ При попытке добавления оборудования произошла ошибка'
        )
    finally:
        await state.clear()


@router.message(F.text == '🏠 Список конференц залов 🏠', is_admin)
async def handle_rooms_list_cmd(message: Message) -> None:
    await message.answer('\n'.join(await utils.get_rooms()))


@router.message(F.text == '💻 Добавить оборудование 💻', is_admin)
async def handle_add_equipment_cmd(message: Message, state: FSMContext) -> None:
    await message.answer('Введите название оборудования')
    await state.set_state(CreateEquipmentForm.name)


@router.message(CreateEquipmentForm.name)
async def set_equipment_name_state(message: Message, state: FSMContext) -> None:
    # TODO: добавить проверку на существующее название оборудование
    name = message.text

    if not (2 <= len(name) <= 100):
        await message.answer(
            'Длина название должна быть от 2 до 100 (включительно) символов'
        )
        return

    await state.update_data(name=name)

    equipment = await state.get_data()

    try:
        await utils.create_equipment(equipment)
        await message.answer('✅ Оборудование успешно добавлено')
    except:
        await message.answer('❌ При добавлении оборудования произошла ошибка')
    finally:
        await state.clear()


@router.message(F.text == '💻 Список оборудования 💻', is_admin)
async def handle_equipments_list_cmd(message: Message) -> None:
    await message.answer('\n'.join(await utils.get_equipments()))


@router.message(F.text == '⌛️ Бронирования ⌛️', is_admin)
async def handle_bookings_admin_cmd(message: Message) -> None:
    await message.answer(
        'Выберите действие',
        reply_markup=keyboards.admin_bookings_kb
    )


@router.message(F.text == '⌛️ Удалить бронирование ⌛️', is_admin)
async def handle_delete_booking_cmd(message: Message, state: FSMContext) -> None:
    await message.answer('Введите ID бронирования')
    await state.set_state(DeleteBookingForm.booking_id)


@router.message(DeleteBookingForm.booking_id)
async def set_booking_id_state(message: Message, state: FSMContext) -> None:
    booking_id = message.text

    if not booking_id.isdigit():
        await message.answer('Введите валидный ID бронирования')
        return

    if int(booking_id) <= 0:
        await message.answer('ID бронирования должен быть больше нуля')
        return

    await state.update_data(booking_id=int(booking_id))
    state_data = await state.get_data()

    try:
        await utils.delete_booking(state_data['booking_id'])
        await message.answer('Бронирование успешно удалено')
    except:
        await message.answer(
            'При попытке удалить бронирование произошла ошибка. Убедитесь, что бронирование с введенным ID существует'
        )
    finally:
        await state.clear()
