import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Setting(BaseSettings):
    redis_url: str = os.getenv("RD_URL", "redis://redis:6379")

settings = Setting()
