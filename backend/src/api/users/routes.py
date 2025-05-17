import uuid
from fastapi import APIRouter, Depends
from pydantic import PositiveInt

from .service import SERVICE_DEP
from .schemas import GetUserSchema, CreateUserSchema
from core.models import User
from api.auth.routes import CURRENT_USER_DEP


router = APIRouter(prefix='/users', tags=['Пользователи'])


@router.get('/', response_model=list[GetUserSchema])
async def get_users(service: SERVICE_DEP):
    return await service.get_users()


@router.get('/me', response_model=GetUserSchema | None)
async def get_me(user: CURRENT_USER_DEP):
    return user


@router.get('/token')
async def get_user_token_by_tg_id(service: SERVICE_DEP, tg_id: PositiveInt) -> dict:
    user = await service.get_user(tg_id=tg_id)
    return {'user_id': user.id}


@router.get('/by-token/{token}')
async def get_user_by_token(service: SERVICE_DEP, token: str) -> dict:
    user = await service.get_user(token=token)
    return {'user_id': user.id}


@router.get('/{user_id}', response_model=GetUserSchema | None)
async def get_user_by_id(service: SERVICE_DEP, user_id: PositiveInt):
    return await service.get_user(id=user_id)


@router.post('/', response_model=GetUserSchema)
async def create_user(service: SERVICE_DEP, user: CreateUserSchema):
    return await service.create_user(user)
