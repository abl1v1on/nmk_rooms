from aiogram.fsm.state import StatesGroup, State


class CreateUserForm(StatesGroup):
    email = State()
    first_name = State()
    last_name = State()
    tg_id = State()
    password = State()


class CreateLocationForm(StatesGroup):
    address = State()


class CreateRoomForm(StatesGroup):
    number = State()
    capacity = State()
    description = State()
    image = State()
    location_id = State()


class CreateEquipmentForm(StatesGroup):
    name = State()


class AddEquipmentsToRoomForm(StatesGroup):
    room_id = State()
    equipments = State()


class GetUserBookings(StatesGroup):
    user_id = State()


class DeleteBookingForm(StatesGroup):
    booking_id = State()
