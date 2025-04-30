import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


load_dotenv()


class BotSettings(BaseModel):
    token: str = os.getenv('API_TOKEN')


class Settings(BaseSettings):
    bot: BotSettings = BotSettings()


settings = Settings()
