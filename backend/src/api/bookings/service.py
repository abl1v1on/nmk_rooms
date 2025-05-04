from datetime import date
from typing import Annotated
from fastapi import Depends, Response, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from . import exceptions
from .schemas import CreateBookingSchema
from api.base_api_service import BaseAPIService
from api.rooms.service import RoomAPIService
from api.users.service import UserAPIService
from core.models import (
    Booking,
    SESSION_DEP,
    BookingTimeEnum,
    Room,
)


class BookingAPIService(BaseAPIService[Booking]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, model=Booking)

    async def get_bookings(self) -> list[Booking]:
        query = select(Booking)
        bookings = (await self.session.execute(query)).scalars().all()
        return bookings

    async def get_booking(self, **by) -> Booking | None:
        query = select(Booking).filter_by(**by)
        booking = (await self.session.execute(query)).scalar_one_or_none()

        if not booking:
            raise exceptions.BookingNotFoundException()

        return booking

    async def create_booking(self, booking: CreateBookingSchema) -> Booking:
        room_service = RoomAPIService(self.session)
        user_service = UserAPIService(self.session)

        await room_service.get_room(id=booking.room_id)
        await user_service.get_user(id=booking.user_id)

        if await self._is_exists(
                room_id=booking.room_id,
                booking_date=booking.booking_date,
                booking_time=booking.booking_time
            ):
            raise exceptions.BookingAlreadyExistsException()

        new_booking = Booking(**booking.model_dump())
        self.session.add(new_booking)
        await self.session.commit()
        return new_booking

    async def get_busy_bookings(self, room_id: int, booking_date: date):
        room_service = RoomAPIService(self.session)
        await room_service.get_room(id=room_id)

        query = select(Booking.booking_time).filter(
            Booking.room_id == room_id,
            Booking.booking_date == booking_date
        )
        busy_bookings = [
            booking.value for booking in
            (await self.session.execute(query)).scalars().all()
        ]
        bookings_time = [b_time.value for b_time in BookingTimeEnum]

        return [b_time for b_time in bookings_time if b_time not in busy_bookings]

    async def get_user_bookings(self, user_id: int) -> list[Booking]:
        query = select(Booking) \
            .filter(Booking.user_id == user_id) \
            .options(selectinload(Booking.room).selectinload(Room.location))
        bookings = (await self.session.execute(query)).scalars().all()
        return bookings

    async def delete_booking(self, booking_id: int) -> Response:
        deletable_booking = await self.get_booking(id=booking_id)
        await self.session.delete(deletable_booking)
        await self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_service(session: SESSION_DEP) -> BookingAPIService:
    return BookingAPIService(session=session)


SERVICE_DEP = Annotated[
    BookingAPIService,
    Depends(get_service)
]
