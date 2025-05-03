from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Equipment(Base):
    __tablename__ = 'equipments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    __table_args__ = (
        CheckConstraint('LENGTH(name) >= 2', name='check_equipment_name_length'),
    )
