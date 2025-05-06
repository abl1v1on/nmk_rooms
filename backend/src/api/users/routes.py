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


@router.get('/{user_id}', response_model=GetUserSchema | None)
async def get_user_by_id(service: SERVICE_DEP, user_id: PositiveInt):
    return await service.get_user(id=user_id)


@router.post('/', response_model=GetUserSchema)
async def create_user(service: SERVICE_DEP, user: CreateUserSchema):
    return await service.create_user(user)
