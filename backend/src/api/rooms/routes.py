from fastapi import APIRouter, Query
from pydantic import PositiveInt
from typing import Annotated

from .service import SERVICE_DEP
from .schemas import (
    GetRoomSchema,
    CreateRoomSchema,
    AddEquipmentsToRoomSchema
)
from api.equipments.schemas import CreateEquipmentSchema


router = APIRouter(prefix='/rooms', tags=['Залы'])


@router.get('/')
async def get_rooms(
        service: SERVICE_DEP,
        q: Annotated[str | None, Query()] = None
    ) -> list[GetRoomSchema]:
    return await service.get_rooms(q)


@router.get('/{room_id}', response_model=GetRoomSchema | None)
async def get_room(service: SERVICE_DEP, room_id: PositiveInt):
    return await service.get_room(id=room_id)


@router.post('/', response_model=GetRoomSchema)
async def create_room(service: SERVICE_DEP, room: CreateRoomSchema):
    return await service.create_room(room)


@router.post('/add-equipments', response_model=None)
async def add_equipments_to_room(
        service: SERVICE_DEP,
        equipments: AddEquipmentsToRoomSchema
    ):
    return await service.add_equipments_to_room(equipments)


# @router.delete('/{room_id}', response_model=None)
# async def delete_room(service: SERVICE_DEP, room_id: PositiveInt):
#     return await service.delete_room(room_id)


@router.delete('/delete-all', response_model=None)
async def delete_all_rooms(service: SERVICE_DEP):
    return await service.delete_all_rooms()
