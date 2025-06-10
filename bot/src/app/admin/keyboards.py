from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👥 Пользователи 👥')
        ],
        [
            KeyboardButton(text='🗺 Локации 🗺')
        ],
        [
            KeyboardButton(text='🏠 Конференц залы 🏠')
        ],
        [
            KeyboardButton(text='💻 Оборудование 💻')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)


admin_users_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 Добавить пользователя 👤'),
            KeyboardButton(text='👥 Список пользователей 👥')
        ],
        [
            KeyboardButton(text='🏠 Забронированые залы пользователя 🏠')
        ],
        [
            KeyboardButton(text='⬅️ Назад ⬅️')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)


admin_locations_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗺 Добавить локацию 🗺'),
            KeyboardButton(text='🗺 Список локаций 🗺')
        ],
        [
            KeyboardButton(text='⬅️ Назад ⬅️')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)


admin_rooms_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏠 Добавить конференц зал 🏠'),
            KeyboardButton(text='🏠 Список конференц залов 🏠')
        ],
        [
            KeyboardButton(text='💻 Добавить оборудование в зал 💻'),
        ],
        [
            KeyboardButton(text='⬅️ Назад ⬅️')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)


admin_equipments_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💻 Добавить оборудование 💻'),
            KeyboardButton(text='💻 Список оборудования 💻'),
        ],
        [
            KeyboardButton(text='⬅️ Назад ⬅️')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
