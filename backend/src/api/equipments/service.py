from typing import Annotated
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Equipment, SESSION_DEP
from api.base_api_service import BaseAPIService
from .schemas import CreateEquipmentSchema
from . import exceptions


class EquipmentAPIService(BaseAPIService[Equipment]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, model=Equipment)

    async def get_equipments(self) -> list[Equipment]:
        query = select(Equipment)
        equipments = (await self.session.execute(query)).scalars().all()
        return equipments

    async def get_equipment(self, **by) -> Equipment | None:
        query = select(Equipment).filter_by(**by)
        equipment = (await self.session.execute(query)).scalar_one_or_none()

        if not equipment:
            raise exceptions.EquipmentNotFoundException()

        return equipment

    async def create_equipment(self, equipment: CreateEquipmentSchema) -> Equipment:
        if await self._is_exists(name=equipment.name):
            raise exceptions.EquipmentAlreadyExistsException('name')

        new_equipment = Equipment(**equipment.model_dump())
        self.session.add(new_equipment)
        await self.session.commit()
        return new_equipment



def get_service(session: SESSION_DEP) -> EquipmentAPIService:
    return EquipmentAPIService(session=session)


SERVICE_DEP = Annotated[
    EquipmentAPIService,
    Depends(get_service)
]
