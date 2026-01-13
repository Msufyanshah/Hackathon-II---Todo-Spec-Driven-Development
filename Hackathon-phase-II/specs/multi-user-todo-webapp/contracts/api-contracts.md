# API Contracts: Multi-User Secure Todo Web Application

## Overview
This document defines the API contracts for the multi-user secure todo web application based on the functional requirements in the specification.

## Authentication
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

## Base URL
```
https://api.example.com/api/{user_id}
```

## Endpoints

### 1. User Authentication

#### POST /auth/login
**Description**: Authenticate user and return JWT token

**Request**:
```json
{
  "username": "string",
  "password": "string"
}
```

**Response (200 OK)**:
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "username": "string",
    "email": "string"
  }
}
```

**Response (401 Unauthorized)**:
```json
{
  "detail": "Invalid credentials"
}
```

#### POST /auth/register
**Description**: Register a new user

**Request**:
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

**Response (201 Created)**:
```json
{
  "id": "uuid",
  "username": "string",
  "email": "string",
  "created_at": "datetime"
}
```

**Response (400 Bad Request)**:
```json
{
  "detail": "Validation error or username/email already exists"
}
```

### 2. Task Management

#### GET /{user_id}/tasks
**Description**: Get all tasks for the authenticated user

**Response (200 OK)**:
```json
{
  "tasks": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "status": "to-do|in-progress|completed",
      "priority": "low|medium|high",
      "due_date": "datetime",
      "created_at": "datetime",
      "updated_at": "datetime",
      "completed_at": "datetime",
      "category": "string"
    }
  ]
}
```

#### POST /{user_id}/tasks
**Description**: Create a new task for the authenticated user

**Request**:
```json
{
  "title": "string (required)",
  "description": "string (optional)",
  "priority": "low|medium|high (optional, default: medium)",
  "due_date": "datetime (optional)",
  "category": "string (optional)"
}
```

**Response (201 Created)**:
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "status": "to-do",
  "priority": "low|medium|high",
  "due_date": "datetime",
  "created_at": "datetime",
  "updated_at": "datetime",
  "completed_at": "datetime",
  "category": "string",
  "user_id": "uuid"
}
```

**Response (400 Bad Request)**:
```json
{
  "detail": "Validation error"
}
```

#### GET /{user_id}/tasks/{task_id}
**Description**: Get details of a specific task

**Response (200 OK)**:
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "status": "to-do|in-progress|completed",
  "priority": "low|medium|high",
  "due_date": "datetime",
  "created_at": "datetime",
  "updated_at": "datetime",
  "completed_at": "datetime",
  "category": "string",
  "user_id": "uuid"
}
```

**Response (404 Not Found)**:
```json
{
  "detail": "Task not found"
}
```

#### PUT /{user_id}/tasks/{task_id}
**Description**: Update a specific task

**Request**:
```json
{
  "title": "string",
  "description": "string",
  "status": "to-do|in-progress|completed",
  "priority": "low|medium|high",
  "due_date": "datetime",
  "category": "string"
}
```

**Response (200 OK)**:
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "status": "to-do|in-progress|completed",
  "priority": "low|medium|high",
  "due_date": "datetime",
  "created_at": "datetime",
  "updated_at": "datetime",
  "completed_at": "datetime",
  "category": "string",
  "user_id": "uuid"
}
```

**Response (400 Bad Request)**:
```json
{
  "detail": "Validation error"
}
```

**Response (404 Not Found)**:
```json
{
  "detail": "Task not found"
}
```

#### DELETE /{user_id}/tasks/{task_id}
**Description**: Delete a specific task

**Response (204 No Content)**: Task successfully deleted

**Response (404 Not Found)**:
```json
{
  "detail": "Task not found"
}
```

#### PATCH /{user_id}/tasks/{task_id}/complete
**Description**: Toggle task completion status

**Request**:
```json
{
  "completed": "boolean"
}
```

**Response (200 OK)**:
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "status": "to-do|in-progress|completed",
  "priority": "low|medium|high",
  "due_date": "datetime",
  "created_at": "datetime",
  "updated_at": "datetime",
  "completed_at": "datetime",
  "category": "string",
  "user_id": "uuid"
}
```

**Response (400 Bad Request)**:
```json
{
  "detail": "Invalid completion status"
}
```

**Response (404 Not Found)**:
```json
{
  "detail": "Task not found"
}
```

## Error Handling

### Common Error Responses

**401 Unauthorized**: 
- When JWT token is missing, invalid, or expired

**403 Forbidden**: 
- When user tries to access resources that don't belong to them

**404 Not Found**: 
- When requested resource doesn't exist

**422 Unprocessable Entity**: 
- When request validation fails

**500 Internal Server Error**: 
- When an unexpected server error occurs

## Security Considerations

1. All endpoints require valid JWT authentication
2. User ID in the path must match the authenticated user's ID
3. Users can only access their own tasks
4. Proper input validation is required for all request parameters
5. SQL injection prevention through parameterized queries
6. XSS prevention through proper output encoding