# Phase I Console Todo Application

This is the Phase I implementation of the Todo Management System, developed as part of the Hackathon II - Todo Spec-Driven Development project. This is a console-based, single-user todo application with in-memory storage.

## Overview

The Phase I Console Todo Application provides a simple, command-line interface for managing personal tasks. It operates entirely in memory and does not persist data between application runs.

## Features

- **Add Task**: Create new tasks with titles and optional descriptions
- **View Task List**: Display all tasks with their completion status
- **Update Task**: Modify existing task details
- **Delete Task**: Remove tasks from the list
- **Mark Complete/Incomplete**: Toggle the completion status of tasks
- **Simple CLI Interface**: Easy-to-use command-line interface with clear prompts

## Commands

- `add`: Add a new task with title and optional description
- `list`: View all tasks with their completion status
- `update`: Update an existing task's title or description
- `delete`: Remove a task from the list
- `complete`: Toggle a task's completion status
- `exit`: Quit the application

## Technical Details

- **Language**: Python 3.13+
- **Architecture**: Console-only, single-user application
- **Storage**: In-memory only (no persistence between runs)
- **Pattern**: Clean separation of concerns (models, storage, CLI interface)

## File Structure

```
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Application entry point
│   ├── task.py                  # Task model definition
│   ├── storage.py               # In-memory storage implementation
│   └── cli.py                   # Command-line interface
├── test_app.py                  # Test script to verify functionality
└── README.md                    # This file
```

## How to Run

1. Ensure Python 3.13+ is installed on your system
2. Navigate to this directory (`phase-1-console`)
3. Run the application:
   ```bash
   python src/main.py
   ```
4. Follow the on-screen prompts to interact with the application

## Architecture

The application follows a clean architecture pattern:

- **Task Model**: Defines the structure and behavior of a task
- **Storage Module**: Handles in-memory storage of tasks
- **CLI Module**: Manages user interactions and command processing
- **Main Module**: Entry point that orchestrates the application

## Limitations

- Data is stored only in memory and will be lost when the application closes
- Single-user only (no authentication required)
- No persistence between application runs
- Console-based interface only

## Next Phases

This application serves as the foundation for future phases of the Todo Management System:

- Phase II: Full-stack web application with persistent storage
- Phase III: AI-powered chatbot interface
- Phase IV: Local Kubernetes deployment
- Phase V: Cloud-native, event-driven production system

## Development Approach

This application was developed following the Spec-Driven Development (SDD) methodology, where all implementation is generated from detailed specifications.