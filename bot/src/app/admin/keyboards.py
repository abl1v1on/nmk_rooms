from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👤 Добавить пользователя 👤'),
            KeyboardButton(text='👥 Список пользователей 👥')
        ],
        [
            KeyboardButton(text='🗺 Добавить локацию 🗺'),
            KeyboardButton(text='🗺 Список локаций 🗺')
        ],
        [
            KeyboardButton(text='🏠 Добавить конференц зал 🏠'),
            KeyboardButton(text='🏠 Список конференц залов 🏠')
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)
