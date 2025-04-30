from typing import TYPE_CHECKING
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from . import Room


class Location(Base):
    __tablename__ = 'locations'

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(255), unique=True)

    rooms: Mapped[list['Room']] = relationship(back_populates='location')

    __table_args__ = (
        CheckConstraint(
            'LENGTH(address) >= 5',
            name='check_location_address_length_ge_5'
        ),
    )
