# Quickstart Guide: Todo System Evolution

## Phase I: Console Todo Application

### Prerequisites
- Python 3.13+
- pip package manager

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the console application:
   ```bash
   python -m todo.console_app
   ```

### Usage
- Add a task: `add "Task title" "Optional description"`
- List tasks: `list`
- Update a task: `update <task_id> "New title" "New description"`
- Delete a task: `delete <task_id>`
- Mark task complete: `complete <task_id>`
- Mark task incomplete: `incomplete <task_id>`

## Phase II: Full-Stack Web Application

### Prerequisites
- Python 3.13+ (backend)
- Node.js 18+ (frontend)
- PostgreSQL 12+
- Docker (optional, for containerization)

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Run database migrations:
   ```bash
   python -m alembic upgrade head
   ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

### API Documentation
The API documentation is available at `http://localhost:8000/docs` when the backend is running.

## Phase III: AI Chatbot Interface

### Prerequisites
- Backend server running (Phase II)
- OpenAI API key
- MCP tools configured

### Setup
1. Configure the AI agent:
   ```bash
   # Set your OpenAI API key in the environment
   export OPENAI_API_KEY=your_api_key_here
   ```

2. Start the AI agent service:
   ```bash
   cd backend
   python -m ai_agent.run
   ```

### Usage
Interact with the AI agent through the web interface or via the API endpoints.

## Phase IV: Local Kubernetes Deployment

### Prerequisites
- Docker Desktop with Kubernetes enabled
- Helm 3+
- kubectl

### Setup
1. Ensure Kubernetes is running in Docker Desktop

2. Install the application using Helm:
   ```bash
   helm install todo-system ./helm/todo-system
   ```

3. Check the status of deployed resources:
   ```bash
   kubectl get pods
   kubectl get services
   ```

4. Access the application:
   ```bash
   minikube service todo-system-frontend --url
   ```

## Phase V: Cloud-Native Event-Driven System

### Prerequisites
- Kubernetes cluster (AKS/GKE/EKS)
- Dapr installed on the cluster
- Kafka-compatible service
- Helm 3+

### Deployment
1. Install Dapr on your cluster:
   ```bash
   dapr init -k
   ```

2. Deploy the application:
   ```bash
   helm install todo-system-prod ./helm/todo-system --set environment=production
   ```

3. Verify deployment:
   ```bash
   kubectl get pods
   kubectl get services
   dapr list
   ```

## Common Development Tasks

### Running Tests
- Backend: `pytest`
- Frontend: `npm run test`

### Code Formatting
- Backend: `black . && isort .`
- Frontend: `npm run format`

### Linting
- Backend: `flake8 .`
- Frontend: `npm run lint`

### Building Docker Images
```bash
docker build -t todo-system-backend -f backend/Dockerfile .
docker build -t todo-system-frontend -f frontend/Dockerfile .
```