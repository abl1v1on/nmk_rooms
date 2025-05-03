from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from .rooms_equipments import rooms_equipments

if TYPE_CHECKING:
    from . import Location, Equipment, Booking


class Room(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(nullable=False, unique=True)
    capacity: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    image: Mapped[str] = mapped_column(String(1000), nullable=True)
    location_id: Mapped[int] = mapped_column(
        ForeignKey('locations.id', ondelete='CASCADE')
    )

    location: Mapped['Location'] = relationship(back_populates='rooms')
    equipments: Mapped[list['Equipment']] = relationship(
        secondary=rooms_equipments,
        back_populates='rooms'
    )
    booking: Mapped[list['Booking']] = relationship(back_populates='room')

    __table_args__ = (
        CheckConstraint('number >= 1', name='check_room_number_ge_1'),
        CheckConstraint('capacity >= 1', name='check_room_capacity_ge_1'),
        CheckConstraint(
            'LENGTH(description) >= 5',
            name='check_room_description_length_ge_1'
        ),
    )
