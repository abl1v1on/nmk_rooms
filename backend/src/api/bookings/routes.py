from fastapi import APIRouter
from pydantic import PositiveInt
from datetime import date

from .service import SERVICE_DEP
from .schemas import GetBookingSchema, CreateBookingSchema


router = APIRouter(prefix='/bookings', tags=['Бронирования'])


@router.get('/', response_model=list[GetBookingSchema])
async def get_bookings(service: SERVICE_DEP):
    return await service.get_bookings()


@router.get('/busy')
async def get_busy_bookings(
        service: SERVICE_DEP,
        room_id: PositiveInt,
        booking_date: date
    ):
    return await service.get_busy_bookings(room_id, booking_date)


@router.get('/{booking_id}', response_model=GetBookingSchema | None)
async def get_booking_by_id(service: SERVICE_DEP, booking_id: PositiveInt):
    return await service.get_booking(id=booking_id)



@router.post('/', response_model=GetBookingSchema)
async def create_booking(service: SERVICE_DEP, booking: CreateBookingSchema):
    return await service.create_booking(booking)
