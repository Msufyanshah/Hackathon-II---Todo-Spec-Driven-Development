"""
Module for in-memory storage of tasks in the Phase I Console Todo Application.
"""
from task import Task
from typing import List, Optional

class TaskStorage:
    """
    Handles in-memory storage of tasks.
    """
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task):
        """
        Adds a task to storage.
        """
        self.tasks.append(task)
    
    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in storage.
        """
        return self.tasks[:]
    
    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Returns a task by its ID, or None if not found.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def remove_task(self, task: Task):
        """
        Removes a task from storage.
        """
        if task in self.tasks:
            self.tasks.remove(task)
    
    def update_task(self, task_id: str, title: str = None, description: str = None, completed: bool = None):
        """
        Updates a task's properties.
        """
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if completed is not None:
                task.completed = completed