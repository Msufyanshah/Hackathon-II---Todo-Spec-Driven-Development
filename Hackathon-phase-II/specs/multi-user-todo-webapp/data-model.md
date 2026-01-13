# Data Model: Multi-User Secure Todo Web Application

## Overview
This document defines the data model for the multi-user secure todo web application, including entities, attributes, relationships, and validation rules based on the feature specification.

## Entities

### User Entity
**Description**: Represents an authenticated user in the system

**Attributes**:
- `id` (UUID): Unique identifier for the user (Primary Key)
- `username` (String): Unique username for login
- `email` (String): User's email address (must be unique and valid)
- `password_hash` (String): Hashed password using secure algorithm (e.g., bcrypt)
- `created_at` (DateTime): Timestamp when the user account was created
- `last_login` (DateTime): Timestamp of the last successful login

**Validation Rules**:
- Username must be 3-30 characters, alphanumeric with underscores allowed
- Email must be a valid email format
- Password must meet complexity requirements (min 8 chars, 1 uppercase, 1 lowercase, 1 number)
- Username and email must be unique across the system

### Task Entity
**Description**: Represents a user's task with various properties and metadata

**Attributes**:
- `id` (UUID): Unique identifier for the task (Primary Key)
- `title` (String): Task title (required, max 200 characters)
- `description` (Text): Optional detailed description of the task
- `status` (Enum): Task status (to-do, in-progress, completed)
- `priority` (Enum): Task priority level (low, medium, high)
- `due_date` (DateTime, optional): Optional deadline for the task
- `created_at` (DateTime): Timestamp when the task was created
- `updated_at` (DateTime): Timestamp when the task was last updated
- `completed_at` (DateTime, optional): Timestamp when the task was marked as completed
- `category` (String, optional): Optional category/tag for organizing tasks
- `user_id` (UUID): Foreign key linking to the user who owns this task

**Validation Rules**:
- Title is required and must be 1-200 characters
- Status must be one of the allowed values (to-do, in-progress, completed)
- Priority must be one of the allowed values (low, medium, high)
- Due date, if provided, must be a future date
- User_id must reference an existing user

## Relationships

### User → Task (One-to-Many)
- A user can own multiple tasks
- Each task belongs to exactly one user
- Foreign key: `user_id` in the Task entity references `id` in the User entity
- When a user is deleted, all their tasks are also deleted (CASCADE delete)

## State Transitions

### Task Status Transitions
- `to-do` → `in-progress`: When user starts working on the task
- `in-progress` → `completed`: When user marks the task as done
- `completed` → `in-progress`: When user needs to make changes to a completed task
- `in-progress` → `to-do`: When user decides to defer the task

### Task Priority Transitions
- Priority can be changed at any time between low, medium, and high
- Changing priority does not affect the task's status

## Database Schema

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- Tasks table
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    status VARCHAR(20) NOT NULL DEFAULT 'to-do',
    priority VARCHAR(10) NOT NULL DEFAULT 'medium',
    due_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    category VARCHAR(50),
    user_id UUID NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Indexes for performance
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);
CREATE INDEX idx_tasks_priority ON tasks(priority);
```

## Security Considerations

### Data Isolation
- All queries must filter by the authenticated user's ID to ensure data isolation
- The foreign key relationship ensures referential integrity
- CASCADE delete ensures that when a user is removed, their tasks are also removed

### Access Control
- Users can only access tasks that belong to them (identified by user_id)
- API endpoints must validate that the authenticated user matches the task owner
- No cross-user access is allowed under any circumstances