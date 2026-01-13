from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime
import uuid
from enum import Enum

if TYPE_CHECKING:
    from .user import User

class TaskStatus(str, Enum):
    TODO = "to-do"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: TaskStatus = Field(default=TaskStatus.TODO)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM)
    due_date: Optional[datetime] = Field(default=None)
    category: Optional[str] = Field(default=None, max_length=50)

class Task(TaskBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = Field(default=None)
    
    # Foreign key to User
    user_id: uuid.UUID = Field(foreign_key="user.id", ondelete="CASCADE")
    
    # Relationship
    user: "User" = Relationship(back_populates="tasks")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Complete project proposal",
                "description": "Finish the project proposal document and submit it",
                "status": "to-do",
                "priority": "high",
                "due_date": "2023-12-31T23:59:59",
                "category": "work"
            }
        }

class TaskCreate(TaskBase):
    title: str = Field(min_length=1, max_length=200)
    due_date: Optional[datetime] = Field(default=None)
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Complete project proposal",
                "description": "Finish the project proposal document and submit it",
                "status": "to-do",
                "priority": "high",
                "due_date": "2023-12-31T23:59:59",
                "category": "work"
            }
        }

class TaskRead(TaskBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime]
    user_id: uuid.UUID
    
    class Config:
        from_attributes = True

class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: Optional[TaskStatus] = Field(default=None)
    priority: Optional[TaskPriority] = Field(default=None)
    due_date: Optional[datetime] = Field(default=None)
    category: Optional[str] = Field(default=None, max_length=50)
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "in-progress",
                "priority": "high"
            }
        }