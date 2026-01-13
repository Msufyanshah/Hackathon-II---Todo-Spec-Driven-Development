from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class UserBase(SQLModel):
    username: str = Field(min_length=3, max_length=30, regex=r'^[a-zA-Z0-9_]+$')
    email: str = Field(regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    first_name: Optional[str] = Field(default=None, max_length=50)
    last_name: Optional[str] = Field(default=None, max_length=50)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = Field(default=None)
    is_active: bool = Field(default=True)
    
    # Add constraints
    __table_args__ = (
        {'sqlite_autoincrement': True},
    )

class UserCreate(UserBase):
    password: str = Field(min_length=8)
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "strongpassword123"
            }
        }

class UserRead(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime]
    is_active: bool
    
    class Config:
        from_attributes = True

class UserUpdate(SQLModel):
    username: Optional[str] = Field(default=None, min_length=3, max_length=30)
    email: Optional[str] = Field(default=None)
    first_name: Optional[str] = Field(default=None, max_length=50)
    last_name: Optional[str] = Field(default=None, max_length=50)
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe_updated",
                "email": "john.updated@example.com",
                "first_name": "John",
                "last_name": "Doe"
            }
        }