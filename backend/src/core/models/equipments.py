from typing import TYPE_CHECKING
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from .rooms_equipments import rooms_equipments

if TYPE_CHECKING:
    from . import Room


class Equipment(Base):
    __tablename__ = 'equipments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    rooms: Mapped[list['Room']] = relationship(
        secondary=rooms_equipments,
        back_populates='equipments'
    )

    __table_args__ = (
        CheckConstraint('LENGTH(name) >= 2', name='check_equipment_name_length'),
    )
