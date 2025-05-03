from typing import TYPE_CHECKING
from datetime import date
from enum import Enum as PyEnum
from sqlalchemy import ForeignKey, Enum as SQLAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from . import Room, User


class BookingTimeEnum(PyEnum):
    TIME_9_10 = '9:00 - 10:00'
    TIME_10_11 = '10:00 - 11:00'
    TIME_11_12 = '11:00 - 12:00'
    TIME_12_13 = '12:00 - 13:00'
    TIME_13_14 = '13:00 - 14:00'
    TIME_14_15 = '14:00 - 15:00'
    TIME_15_16 = '15:00 - 16:00'
    TIME_16_17 = '16:00 - 17:00'
    TIME_17_18 = '17:00 - 18:00'


class Booking(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(
        ForeignKey('rooms.id', ondelete='CASCADE')
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE')
    )
    booking_date: Mapped[date] = mapped_column(nullable=False)
    booking_time: Mapped[BookingTimeEnum] = mapped_column(
        SQLAEnum(BookingTimeEnum), nullable=False
    )

    room: Mapped['Room'] = relationship(back_populates='bookings')
    user: Mapped['User'] = relationship(back_populates='bookings')
