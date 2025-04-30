import jwt
import bcrypt

from core import settings


class AuthAPIService:
    def __init__(self) -> None:
        self.algorithm = settings.auth_jwt.algorithm
        self.private_key = settings.auth_jwt.private_key_path.read_text()
        self.public_key = settings.auth_jwt.public_key_path.read_text()

    def encode_jwt(self, payload: dict) -> str:
        token = jwt.encode(
            payload=payload,
            key=self.private_key,
            algorith=self.algorithm
        )
        return token

    def decode_jwt(self, token: str | bytes) -> dict:
        data = jwt.decode(
            jwt=token,
            key=self.public_key,
            algorithms=[self.algorithm]
        )
        return data

    @staticmethod
    def __verify_password(pwd: str, hashed_pwd: bytes) -> bool:
        return bcrypt.checkpw(
            pwd.encode(),
            hashed_pwd
        )

    @staticmethod
    def __hash_password(pwd: str) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(
            pwd.encode(),
            salt
        )
