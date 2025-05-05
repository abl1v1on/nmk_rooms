import jwt
import bcrypt
from typing import Annotated
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core import settings
from core.models import SESSION_DEP, User
from .schemas import AccessTokenSchema, AuthUserSchema
from .exceptions import InvalidCredentialsException


class AuthAPIService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.algorithm = settings.auth_jwt.algorithm
        self.private_key = settings.auth_jwt.private_key_path.read_text()
        self.public_key = settings.auth_jwt.public_key_path.read_text()

    async def auth_user(self, credentials: AuthUserSchema) -> AccessTokenSchema:
        query = select(User).filter(User.email == credentials.email)
        user = (await self.session.execute(query)).scalar_one_or_none()

        if not user or not self.__verify_password(credentials.password, user.password):
            raise InvalidCredentialsException()

        payload = self.__generate_payload(user)
        token = self.encode_jwt(payload)
        return AccessTokenSchema(token=token)

    def encode_jwt(self, payload: dict) -> str:
        token = jwt.encode(
            payload=payload,
            key=self.private_key,
            algorithm=self.algorithm
        )
        return token

    def decode_jwt(self, token: str | bytes) -> dict:
        try:
            data = jwt.decode(
                jwt=token,
                key=self.public_key,
                algorithms=[self.algorithm]
            )
            return data
        except jwt.exceptions.ExpiredSignatureError:
            raise HTTPException(
                detail='Token has expired',
                status_code=status.HTTP_403_FORBIDDEN
            )
        except jwt.exceptions.DecodeError:
            raise HTTPException(
                detail='Decode error',
                status_code=status.HTTP_403_FORBIDDEN
            )

    @staticmethod
    def __verify_password(pwd: str, hashed_pwd: bytes) -> bool:
        return bcrypt.checkpw(
            pwd.encode(),
            hashed_pwd
        )

    def __generate_payload(self, user: User) -> dict:
        now = datetime.now(tz=timezone.utc)
        exp = self.__get_expire(now)
        payload = {
            'sub': str(user.id),
            'email': user.email,
            'iat': now,
            'exp': exp
        }
        return payload

    @staticmethod
    def __get_expire(now: datetime):
        offset = timedelta(minutes=settings.auth_jwt.access_token_expire_minutes)
        return now + offset


def get_service(session: SESSION_DEP) -> AuthAPIService:
    return AuthAPIService(session=session)


SERVICE_DEP = Annotated[
    AuthAPIService,
    Depends(get_service)
]
