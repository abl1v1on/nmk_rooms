from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from core.models import User
from api.users.service import SERVICE_DEP as USERS_SERVICE_DEP
from .service import SERVICE_DEP
from .schemas import AuthUserSchema, AccessTokenSchema, TokenPayload


http_bearer = HTTPBearer()


def get_auth_token(
        service: SERVICE_DEP,
        jwt_credentials: HTTPAuthorizationCredentials = Depends(http_bearer)
    ) -> TokenPayload:
    token = jwt_credentials.credentials
    payload = TokenPayload(**service.decode_jwt(token))
    return payload


async def get_current_user(
        service: USERS_SERVICE_DEP,
        payload: TokenPayload = Depends(get_auth_token)
    ) -> User:
    user = await service.get_user(id=int(payload.sub))
    return user


AUTH_TOKEN_DEP = Annotated[TokenPayload, Depends(get_auth_token)]
CURRENT_USER_DEP = Annotated[User, Depends(get_current_user)]


router = APIRouter(prefix='/auth', tags=['Аутентификация'])


@router.post('/login', response_model=AccessTokenSchema)
async def login_user(service: SERVICE_DEP, credentials: AuthUserSchema):
    return await service.auth_user(credentials)
