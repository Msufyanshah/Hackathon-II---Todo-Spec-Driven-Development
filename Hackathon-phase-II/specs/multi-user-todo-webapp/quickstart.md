# Quickstart Guide: Multi-User Secure Todo Web Application

## Overview
This guide provides instructions for setting up and running the multi-user secure todo web application locally.

## Prerequisites
- Node.js 18+ (for frontend)
- Python 3.11+ (for backend)
- PostgreSQL (or access to Neon Serverless PostgreSQL)
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Backend Setup
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
   JWT_SECRET="your-super-secret-jwt-key-here"
   JWT_ALGORITHM="HS256"
   JWT_EXPIRATION_HOURS=24
   BETTER_AUTH_SECRET="your-better-auth-secret"
   ```

5. Run database migrations:
   ```bash
   python -m src.database.migrate
   ```

6. Start the backend server:
   ```bash
   python -m src.main
   ```

### 3. Frontend Setup
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
   NEXT_PUBLIC_JWT_SECRET="your-super-secret-jwt-key-here"
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

## Running the Application
1. Make sure both the backend and frontend servers are running
2. Open your browser and navigate to `http://localhost:3000`
3. Register a new account or log in with an existing account
4. Start creating and managing your tasks

## API Testing
The API documentation is available at `http://localhost:8000/docs` when the backend is running.

## Environment Configuration
- `DATABASE_URL`: Connection string for the PostgreSQL database
- `JWT_SECRET`: Secret key for JWT token signing
- `JWT_ALGORITHM`: Algorithm used for JWT signing (default: HS256)
- `JWT_EXPIRATION_HOURS`: Number of hours before JWT tokens expire
- `BETTER_AUTH_SECRET`: Secret for Better Auth integration

## Troubleshooting
- If you encounter database connection issues, verify your PostgreSQL server is running and credentials are correct
- If authentication fails, ensure the JWT_SECRET is the same in both frontend and backend environments
- For frontend build issues, try clearing the cache: `npm run clean` then `npm install`

## Next Steps
1. Explore the API endpoints in the documentation
2. Customize the UI to match your preferences
3. Add additional features as needed
4. Set up automated tests
5. Deploy to a production environment