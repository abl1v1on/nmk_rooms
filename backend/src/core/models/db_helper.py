from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from core import settings


class DataBaseHelper:
    def __init__(self) -> None:
        self.engine = create_async_engine(
            url=settings.db.url,
            echo=settings.db.echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DataBaseHelper()

SESSION_DEP = Annotated[
    AsyncSession,
    Depends(db_helper.get_session)
]
