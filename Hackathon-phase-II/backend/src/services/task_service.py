from sqlmodel import Session, select, func
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from ..models.task import Task, TaskCreate, TaskUpdate, TaskStatus
from ..models.user import User
from ..exceptions.custom_exceptions import TaskNotFoundException, InsufficientPermissionsException
from ..utils.logging import get_logger

logger = get_logger(__name__)

class TaskService:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, task_data: TaskCreate, user_id: UUID) -> Task:
        """
        Create a new task for the specified user
        """
        task = Task.model_validate(task_data)
        task.user_id = user_id
        
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        
        logger.info(f"Task created with ID: {task.id} for user: {user_id}")
        return task

    def get_tasks(self, user_id: UUID, skip: int = 0, limit: int = 100) -> List[Task]:
        """
        Get all tasks for the specified user with pagination
        """
        statement = (
            select(Task)
            .where(Task.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .order_by(Task.created_at.desc())
        )
        tasks = self.session.exec(statement).all()
        
        logger.info(f"Retrieved {len(tasks)} tasks for user: {user_id}")
        return tasks

    def get_task(self, task_id: UUID, user_id: UUID) -> Task:
        """
        Get a specific task by ID for the specified user
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = self.session.exec(statement).first()
        
        if not task:
            logger.warning(f"Task with ID: {task_id} not found for user: {user_id}")
            raise TaskNotFoundException(str(task_id))
        
        return task

    def update_task(self, task_id: UUID, task_update: TaskUpdate, user_id: UUID) -> Task:
        """
        Update a specific task by ID for the specified user
        """
        task = self.get_task(task_id, user_id)
        
        # Update only the fields that are provided
        update_data = task_update.model_dump(exclude_unset=True)
        
        # If status is being updated to completed, set completed_at
        if "status" in update_data and update_data["status"] == TaskStatus.COMPLETED:
            update_data["completed_at"] = datetime.utcnow()
        # If status is being updated from completed to something else, clear completed_at
        elif "status" in update_data and update_data["status"] != TaskStatus.COMPLETED and task.status == TaskStatus.COMPLETED:
            update_data["completed_at"] = None
            
        task.sqlmodel_update(update_data)
        
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        
        logger.info(f"Task updated with ID: {task.id} for user: {user_id}")
        return task

    def delete_task(self, task_id: UUID, user_id: UUID) -> bool:
        """
        Delete a specific task by ID for the specified user
        """
        task = self.get_task(task_id, user_id)
        
        self.session.delete(task)
        self.session.commit()
        
        logger.info(f"Task deleted with ID: {task.id} for user: {user_id}")
        return True

    def toggle_task_completion(self, task_id: UUID, user_id: UUID) -> Task:
        """
        Toggle the completion status of a task
        """
        task = self.get_task(task_id, user_id)
        
        if task.status == TaskStatus.COMPLETED:
            task.status = TaskStatus.IN_PROGRESS
            task.completed_at = None
        else:
            task.status = TaskStatus.COMPLETED
            task.completed_at = datetime.utcnow()
            
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        
        logger.info(f"Task completion toggled for ID: {task.id} for user: {user_id}")
        return task

    def get_user_statistics(self, user_id: UUID) -> dict:
        """
        Get statistics for a user's tasks
        """
        # Count all tasks
        all_count = self.session.scalar(
            select(func.count(Task.id)).where(Task.user_id == user_id)
        )
        
        # Count completed tasks
        completed_count = self.session.scalar(
            select(func.count(Task.id)).where(
                Task.user_id == user_id,
                Task.status == TaskStatus.COMPLETED
            )
        )
        
        # Count in-progress tasks
        in_progress_count = self.session.scalar(
            select(func.count(Task.id)).where(
                Task.user_id == user_id,
                Task.status == TaskStatus.IN_PROGRESS
            )
        )
        
        # Count to-do tasks
        todo_count = self.session.scalar(
            select(func.count(Task.id)).where(
                Task.user_id == user_id,
                Task.status == TaskStatus.TODO
            )
        )
        
        stats = {
            "total": all_count,
            "completed": completed_count,
            "in_progress": in_progress_count,
            "todo": todo_count
        }
        
        logger.info(f"Retrieved statistics for user: {user_id}")
        return stats