"""
Module for CLI interactions in the Phase I Console Todo Application.
"""
from task import Task
from storage import TaskStorage

class TodoCLI:
    """
    Handles command-line interface for the todo application.
    """
    def __init__(self):
        self.storage = TaskStorage()
        self.running = True
        
    def run(self):
        """
        Main application loop.
        """
        print("Welcome to the Phase I Console Todo Application!")
        
        while self.running:
            command = input("\nEnter command (add/list/update/delete/complete/exit): ").strip().lower()
            
            if command == "add":
                self.add_task()
            elif command == "list":
                self.list_tasks()
            elif command == "update":
                self.update_task()
            elif command == "delete":
                self.delete_task()
            elif command == "complete":
                self.toggle_complete()
            elif command == "exit":
                self.exit_app()
            else:
                print("Invalid command. Please try again.")
    
    def add_task(self):
        """
        Adds a new task.
        """
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            return
            
        description = input("Enter task description (optional): ").strip()
        if not description:
            description = None
            
        task_id = str(len(self.storage.tasks) + 1)
        task = Task(task_id, title, description)
        self.storage.add_task(task)
        print(f"Task '{title}' added with ID {task_id}.")
    
    def list_tasks(self):
        """
        Lists all tasks.
        """
        tasks = self.storage.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour tasks:")
            for task in tasks:
                print(task)
    
    def update_task(self):
        """
        Updates an existing task.
        """
        task_id = input("Enter task ID to update: ").strip()
        task = self.storage.get_task_by_id(task_id)
        
        if not task:
            print(f"No task found with ID {task_id}.")
            return
            
        new_title = input(f"Enter new title (current: {task.title}): ").strip()
        if new_title:
            task.title = new_title
            
        new_description = input(f"Enter new description (current: {task.description or 'None'}): ").strip()
        if new_description:
            task.description = new_description
        elif new_description == "":
            task.description = None
            
        print(f"Task {task_id} updated.")
    
    def delete_task(self):
        """
        Deletes a task.
        """
        task_id = input("Enter task ID to delete: ").strip()
        task = self.storage.get_task_by_id(task_id)
        
        if not task:
            print(f"No task found with ID {task_id}.")
            return
            
        self.storage.remove_task(task)
        print(f"Task {task_id} deleted.")
    
    def toggle_complete(self):
        """
        Toggles task completion status.
        """
        task_id = input("Enter task ID to toggle: ").strip()
        task = self.storage.get_task_by_id(task_id)
        
        if not task:
            print(f"No task found with ID {task_id}.")
            return
            
        if task.completed:
            task.mark_incomplete()
            print(f"Task {task_id} marked as incomplete.")
        else:
            task.mark_completed()
            print(f"Task {task_id} marked as complete.")
    
    def exit_app(self):
        """
        Exits the application.
        """
        print("Exiting application. Goodbye!")
        self.running = False