# Multi-User Secure Todo Web Application

This is a secure, multi-user todo application with JWT-based authentication and strict user-level data isolation. The implementation follows a spec-first, agentic development approach using Claude Code, with a Next.js frontend and FastAPI backend connected to Neon PostgreSQL via SQLModel ORM.

## Features

- Secure JWT-based authentication with Better Auth
- Multi-user support with strict data isolation
- Full CRUD operations for tasks
- Task prioritization and categorization
- Responsive design for desktop, tablet, and mobile
- RESTful API with comprehensive endpoints
- Comprehensive error handling and validation

## Tech Stack

- **Frontend**: Next.js 16+, TypeScript, Tailwind CSS
- **Backend**: Python 3.11, FastAPI
- **Database**: Neon Serverless PostgreSQL
- **ORM**: SQLModel
- **Authentication**: Better Auth with JWT
- **Testing**: pytest (backend), Jest/React Testing Library (frontend)

## Setup

### Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL (or access to Neon Serverless PostgreSQL)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file with your configuration:
   ```env
   DATABASE_URL="postgresql://username:password@localhost:5432/todo_app"
   SECRET_KEY="your-super-secret-jwt-key-here"
   ALGORITHM="HS256"
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file with your configuration:
   ```env
   NEXT_PUBLIC_API_URL="http://localhost:8000"
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

### Authentication

- `POST /auth/login` - Authenticate user and return JWT token
- `POST /auth/register` - Register a new user

### Tasks

- `GET /api/{user_id}/tasks` - Get all tasks for the authenticated user
- `POST /api/{user_id}/tasks` - Create a new task for the authenticated user
- `GET /api/{user_id}/tasks/{task_id}` - Get details of a specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a specific task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a specific task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Toggle task completion status

## Security

- All endpoints require valid JWT authentication
- Users can only access their own tasks
- Passwords are securely hashed using bcrypt
- SQL injection prevention through parameterized queries
- Input validation on all endpoints

## Testing

### Backend Tests

Run backend tests with pytest:
```bash
cd backend
pytest
```

### Frontend Tests

Run frontend tests with Jest:
```bash
cd frontend
npm test
```

## Environment Variables

### Backend

- `DATABASE_URL` - Connection string for the PostgreSQL database
- `SECRET_KEY` - Secret key for JWT token signing
- `ALGORITHM` - Algorithm used for JWT signing (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Number of minutes before JWT tokens expire

### Frontend

- `NEXT_PUBLIC_API_URL` - Base URL for the backend API

## Architecture

The application follows a clean architecture pattern with clear separation of concerns:

- **Models**: Define data structures and validation rules
- **Services**: Contain business logic and interact with the database
- **API Routes**: Handle HTTP requests and responses
- **Middleware**: Handle authentication and authorization
- **Frontend Components**: Presentational and container components

## Data Model

### User Entity
- `id` (UUID): Unique identifier for the user (Primary Key)
- `username` (String): Unique username for login
- `email` (String): User's email address (must be unique and valid)
- `password_hash` (String): Hashed password using secure algorithm (e.g., bcrypt)
- `created_at` (DateTime): Timestamp when the user account was created
- `last_login` (DateTime): Timestamp of the last successful login

### Task Entity
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

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.