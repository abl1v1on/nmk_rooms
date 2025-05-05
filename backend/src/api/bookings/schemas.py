from pydantic import BaseModel
from typing import Annotated
from annotated_types import Gt, MinLen, MaxLen
from datetime import date

from core.models import BookingTimeEnum
from api.rooms.schemas import GetRoomSchema


class BaseBookingSchema(BaseModel):
    room_id: Annotated[int, Gt(0)]
    user_id: Annotated[int, Gt(0)]
    goal: Annotated[str | None, MinLen(2), MaxLen(100)] = None
    booking_date: date
    booking_time: BookingTimeEnum


class GetBookingSchema(BaseBookingSchema):
    id: Annotated[int, Gt(0)]


class GetBookingWithRoomSchema(BaseModel):
    id: Annotated[int, Gt(0)]
    room: GetRoomSchema
    user_id: Annotated[int, Gt(0)]
    goal: Annotated[str | None, MinLen(2), MaxLen(100)] = None
    booking_date: date
    booking_time: BookingTimeEnum


class CreateBookingSchema(BaseBookingSchema):
    pass
