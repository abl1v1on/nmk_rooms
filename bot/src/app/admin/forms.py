from aiogram.fsm.state import StatesGroup, State


class CreateUserForm(StatesGroup):
    email = State()
    first_name = State()
    last_name = State()
    tg_id = State()
    password = State()
