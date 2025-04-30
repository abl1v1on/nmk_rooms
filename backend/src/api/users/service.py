from typing import Annotated
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User, SESSION_DEP
from .schemas import CreateUserSchema
from .exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)


class UserAPIService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_users(self) -> list[User]:
        query = select(User)
        users = (await self.session.execute(query)).scalars().all()
        return users

    async def get_user(self, **by) -> User | None:
        query = select(User).filter_by(**by)
        user = (await self.session.execute(query)).scalar_one_or_none()

        if not user:
            raise UserNotFoundException()

        return user

    async def create_user(self, user: CreateUserSchema) -> User:
        if await self.__is_exists(email=user.email):
            raise UserAlreadyExistsException('email')

        if await self.__is_exists(tg_id=user.tg_id):
            raise UserAlreadyExistsException('tg_id')

        new_user = User(**user.model_dump())
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def __is_exists(self, **by) -> bool:
        query = select(select(User).filter_by(**by).exists())
        return (await self.session.execute(query)).scalar()


def get_service(session: SESSION_DEP) -> UserAPIService:
    return UserAPIService(session)


SERVICE_DEP = Annotated[
    UserAPIService,
    Depends(get_service)
]
