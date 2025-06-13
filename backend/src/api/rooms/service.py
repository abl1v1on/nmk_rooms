from typing import Annotated
from fastapi import Depends, Response, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Room, Equipment, SESSION_DEP
from api.base_api_service import BaseAPIService
from api.locations.service import LocationAPIService
from api.equipments.service import EquipmentAPIService
from .schemas import CreateRoomSchema, AddEquipmentsToRoomSchema
from . import exceptions


class RoomAPIService(BaseAPIService[Room]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, model=Room)

    async def get_rooms(self, q: str | None) -> list[Room]:
        query = select(Room)

        if q:
            query = query.filter(Room.number.icontains(q))

        query = query.options(selectinload(Room.location))
        rooms = (await self.session.execute(query)).scalars().all()
        return rooms

    async def get_room(self, **by) -> Room | None:
        query = select(Room) \
            .filter_by(**by) \
            .options(
                selectinload(Room.location),
                selectinload(Room.equipments)
            )
        room = (await self.session.execute(query)).scalar_one_or_none()

        if not room:
            raise exceptions.RoomNotFoundException()

        return room
    
    async def get_room_equipments(self, room_id: int) -> list[Equipment]:
        query = select(Room) \
            .filter(Room.id == room_id) \
            .options(selectinload(Room.equipments))
        result = await self.session.execute(query)
        room = result.scalar_one_or_none()

        if not room:
            raise exceptions.RoomNotFoundException()
        
        return room.equipments

    async def create_room(self, room: CreateRoomSchema) -> Room:
        if await self._is_exists(number=room.number):
            raise exceptions.RoomAlreadyExistsException('number')

        location_service = LocationAPIService(self.session)
        await location_service.get_location(room.location_id)

        new_room = Room(**room.model_dump())
        self.session.add(new_room)
        await self.session.commit()

        query = select(Room) \
            .options(selectinload(Room.location)) \
            .where(Room.id == new_room.id)
        room_with_location = (await self.session.execute(query)).scalar()

        return room_with_location

    async def add_equipments_to_room(
            self,
            equipments: AddEquipmentsToRoomSchema
        ) -> None:
        room = await self.get_room(id=equipments.room_id)
        equipment_service = EquipmentAPIService(self.session)

        for equipment in equipments.equipments:
            equipment_obj = await equipment_service.get_equipment(
                name=equipment.name
            )
            room.equipments.append(equipment_obj)

        await self.session.commit()
        return room

    async def delete_room(self, room_id: int) -> Response:
        deletable_room = await self.get_room(id=room_id)
        await self.session.delete(deletable_room)
        await self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    async def delete_all_rooms(self) -> Response:
        rooms = await self.get_rooms()

        for room in rooms:
            await self.session.delete(room)

        await self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_service(session: SESSION_DEP) -> RoomAPIService:
    return RoomAPIService(session=session)


SERVICE_DEP = Annotated[
    RoomAPIService,
    Depends(get_service)
]
