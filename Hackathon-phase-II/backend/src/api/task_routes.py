from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from sqlmodel import Session
from .api.auth_routes import get_current_user
from .database import get_session
from .models.user import User
from .models.task import Task, TaskCreate, TaskRead, TaskUpdate
from .services.task_service import TaskService
from .utils.logging import get_logger

task_router = APIRouter()
logger = get_logger(__name__)

@task_router.get("/{user_id}/tasks", response_model=List[TaskRead])
def get_tasks(
    user_id: UUID,
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get all tasks for the specified user
    """
    if current_user.id != user_id:
        logger.warning(f"User {current_user.id} attempted to access tasks for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access these tasks"
        )
    
    task_service = TaskService(session)
    tasks = task_service.get_tasks(user_id, skip=skip, limit=limit)
    logger.info(f"Retrieved {len(tasks)} tasks for user: {user_id}")
    return tasks

@task_router.post("/{user_id}/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: UUID,
    task_data: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the specified user
    """
    if current_user.id != user_id:
        logger.warning(f"User {current_user.id} attempted to create task for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create tasks for this user"
        )
    
    task_service = TaskService(session)
    task = task_service.create_task(task_data, user_id)
    logger.info(f"Created task {task.id} for user: {user_id}")
    return task

@task_router.get("/{user_id}/tasks/{task_id}", response_model=TaskRead)
def get_task(
    user_id: UUID,
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get a specific task by ID for the specified user
    """
    if current_user.id != user_id:
        logger.warning(f"User {current_user.id} attempted to access task {task_id} for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this task"
        )
    
    task_service = TaskService(session)
    task = task_service.get_task(task_id, user_id)
    logger.info(f"Retrieved task {task.id} for user: {user_id}")
    return task

@task_router.put("/{user_id}/tasks/{task_id}", response_model=TaskRead)
def update_task(
    user_id: UUID,
    task_id: UUID,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific task by ID for the specified user
    """
    if current_user.id != user_id:
        logger.warning(f"User {current_user.id} attempted to update task {task_id} for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )
    
    task_service = TaskService(session)
    task = task_service.update_task(task_id, task_update, user_id)
    logger.info(f"Updated task {task.id} for user: {user_id}")
    return task

@task_router.delete("/{user_id}/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    user_id: UUID,
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task by ID for the specified user
    """
    if current_user.id != user_id:
        logger.warning(f"User {current_user.id} attempted to delete task {task_id} for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task"
        )
    
    task_service = TaskService(session)
    task_service.delete_task(task_id, user_id)
    logger.info(f"Deleted task {task_id} for user: {user_id}")
    return

@task_router.patch("/{user_id}/tasks/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion(
    user_id: UUID,
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a task
    """
    if current_user.id != user_id:
        logger.warning(f"User {current_user.id} attempted to toggle completion for task {task_id} for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this task"
        )
    
    task_service = TaskService(session)
    task = task_service.toggle_task_completion(task_id, user_id)
    logger.info(f"Toggled completion for task {task.id} for user: {user_id}")
    return task