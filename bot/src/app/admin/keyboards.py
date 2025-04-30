from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='👤 Добавить пользователя 👤')]
    ], resize_keyboard=True, one_time_keyboard=True
)
