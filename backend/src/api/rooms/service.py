from typing import Annotated
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Room, SESSION_DEP
from api.base_api_service import BaseAPIService
from api.locations.service import LocationAPIService
from .schemas import CreateRoomSchema
from . import exceptions


class RoomAPIService(BaseAPIService[Room]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, model=Room)

    async def get_rooms(self) -> list[Room]:
        query = select(Room).options(selectinload(Room.location))
        rooms = (await self.session.execute(query)).scalars().all()
        return rooms

    async def get_room(self, **by) -> Room | None:
        query = select(Room).filter_by(**by).options(selectinload(Room.location))
        room = (await self.session.execute(query)).scalar_one_or_none()

        if not room:
            raise exceptions.RoomNotFoundException()

        return room

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


def get_service(session: SESSION_DEP) -> RoomAPIService:
    return RoomAPIService(session=session)


SERVICE_DEP = Annotated[
    RoomAPIService,
    Depends(get_service)
]
