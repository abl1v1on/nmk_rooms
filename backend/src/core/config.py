from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent.parent


class DataBaseSettings(BaseModel):
    url: str = f'sqlite+aiosqlite:///{BASE_DIR / 'db.sqlite3'}'
    echo: bool = False


class ServerSettings(BaseModel):
    app: str = 'main:app'
    reload: bool = True
    host: str = 'localhost'
    port: int = 8000


class AuthJWTSettings(BaseModel):
    algorithm: str = 'RS256'
    private_key_path: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key_path: Path = BASE_DIR / 'certs' / 'jwt-public.pem'
    access_token_expire_minutes: int = 3


class Settings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    server: ServerSettings = ServerSettings()
    auth_jwt: AuthJWTSettings = AuthJWTSettings()


settings = Settings()
