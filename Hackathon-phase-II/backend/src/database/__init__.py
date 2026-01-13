from sqlmodel import create_engine
from typing import Generator

# Database URL - using environment variable
import os
from pydantic_settings import Settings

class DatabaseSettings(Settings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

settings = DatabaseSettings()

# Create the engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # Set to False in production
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

def get_session():
    from sqlmodel import Session
    with Session(engine) as session:
        yield session