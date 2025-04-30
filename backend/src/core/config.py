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


class Settings(BaseSettings):
    db: DataBaseSettings = DataBaseSettings()
    server: ServerSettings = ServerSettings()


settings = Settings()
