# Phase I Console Todo Application

This is a simple, console-based todo application that operates entirely in memory. It allows users to manage tasks through command-line interactions.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Simple command-line interface

## Commands

- `add` - Add a new task
- `list` - View all tasks
- `update` - Update an existing task
- `delete` - Remove a task
- `complete` - Mark a task as complete/incomplete
- `exit` - Quit the application

## How to Run

1. Make sure you have Python 3.13+ installed
2. Navigate to the `phase-1-console` directory
3. Run the application:
   ```
   python src/main.py
   ```
4. Follow the on-screen prompts to interact with the application

## Notes

- All data is stored in memory only and will be lost when the application closes
- No external dependencies are required beyond Python standard library
- This is a single-user application with no authentication required