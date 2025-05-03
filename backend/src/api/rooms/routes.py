from fastapi import APIRouter
from pydantic import PositiveInt

from .service import SERVICE_DEP
from .schemas import GetRoomSchema, CreateRoomSchema


router = APIRouter(prefix='/rooms', tags=['Залы'])


@router.get('/', response_model=list[GetRoomSchema])
async def get_rooms(service: SERVICE_DEP):
    return await service.get_rooms()


@router.get('/{room_id}', response_model=GetRoomSchema | None)
async def get_room(service: SERVICE_DEP, room_id: PositiveInt):
    return await service.get_room(id=room_id)


@router.post('/', response_model=GetRoomSchema)
async def create_room(service: SERVICE_DEP, room: CreateRoomSchema):
    return await service.create_room(room)


# @router.delete('/{room_id}', response_model=None)
# async def delete_room(service: SERVICE_DEP, room_id: PositiveInt):
#     return await service.delete_room(room_id)


@router.delete('/delete-all', response_model=None)
async def delete_all_rooms(service: SERVICE_DEP):
    return await service.delete_all_rooms()
