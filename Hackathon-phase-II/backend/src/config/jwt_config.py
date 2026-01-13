import os
from datetime import datetime, timedelta
from typing import Optional
from pydantic_settings import BaseSettings

class JWTConfig(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"

jwt_config = JWTConfig()