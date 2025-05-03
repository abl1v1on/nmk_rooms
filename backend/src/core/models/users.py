from typing import TYPE_CHECKING
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base

if TYPE_CHECKING:
    from . import Booking


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    tg_id: Mapped[int] = mapped_column(nullable=False)

    booking: Mapped[list['Booking']] = relationship(back_populates='user')

    __table_args__ = (
        CheckConstraint(
            'LENGTH(first_name) >= 2',
            name='check_user_first_name_length'
        ),
        CheckConstraint(
            'LENGTH(last_name) >= 2',
            name='check_user_last_name_length'
        ),
    )
