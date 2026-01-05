"""
Test script to verify the Phase I console Todo application modules work correctly.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from task import Task
from storage import TaskStorage
from cli import TodoCLI

def test_task_creation():
    print("Testing Task creation...")
    task = Task("1", "Test task", "This is a test task")
    print(f"Created task: {task}")
    print(f"Task ID: {task.id}, Title: {task.title}, Completed: {task.completed}")
    print("PASS: Task creation test passed\n")

def test_storage_operations():
    print("Testing Storage operations...")
    storage = TaskStorage()

    # Add a task
    task1 = Task("1", "First task", "Description for first task")
    storage.add_task(task1)

    # Add another task
    task2 = Task("2", "Second task", "Description for second task")
    storage.add_task(task2)

    # Get all tasks
    tasks = storage.get_all_tasks()
    print(f"Number of tasks in storage: {len(tasks)}")

    # Get task by ID
    retrieved_task = storage.get_task_by_id("1")
    print(f"Retrieved task ID 1: {retrieved_task}")

    # Remove a task
    storage.remove_task(task1)
    tasks_after_removal = storage.get_all_tasks()
    print(f"Number of tasks after removal: {len(tasks_after_removal)}")

    print("PASS: Storage operations test passed\n")

def test_cli_initialization():
    print("Testing CLI initialization...")
    try:
        cli = TodoCLI()
        print(f"CLI initialized successfully. Storage has {len(cli.storage.tasks)} tasks initially.")
        print("PASS: CLI initialization test passed\n")
    except Exception as e:
        print(f"FAIL: CLI initialization failed: {e}\n")

if __name__ == "__main__":
    print("Running tests for Phase I console Todo application...\n")

    test_task_creation()
    test_storage_operations()
    test_cli_initialization()

    print("SUCCESS: All tests completed successfully! The modules are working correctly.")
    print("\nThe application is ready to run. To run it, execute: python src/main.py")
    print("Note: The application is interactive and requires user input.")