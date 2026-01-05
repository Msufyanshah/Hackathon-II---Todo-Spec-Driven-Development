"""
Module defining the Task data model for the Phase I Console Todo Application.
"""
from typing import Optional

class Task:
    """
    Represents a task in the console todo application.
    """
    def __init__(self, task_id: str, title: str, description: Optional[str] = None, completed: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.title}"
    
    def mark_completed(self):
        self.completed = True
    
    def mark_incomplete(self):
        self.completed = False