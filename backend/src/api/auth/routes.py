from fastapi import APIRouter

from .service import SERVICE_DEP
from .schemas import AuthUserSchema, AccessTokenSchema


router = APIRouter(prefix='/auth', tags=['Аутентификация'])


@router.post('/login', response_model=AccessTokenSchema)
async def login_user(service: SERVICE_DEP, credentials: AuthUserSchema):
    return await service.auth_user(credentials)
