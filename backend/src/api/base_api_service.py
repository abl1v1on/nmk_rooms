from typing import TypeVar, Type, Generic
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Base


ModelType = TypeVar('ModelType', bound=Base)


class BaseAPIService(Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: Type[ModelType]) -> None:
        self.session = session
        self.model = model

    async def _is_exists(self, **by) -> bool:
        query = select(select(self.model).filter_by(**by).exists())
        return (await self.session.execute(query)).scalar()
