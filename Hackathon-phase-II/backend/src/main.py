from fastapi import FastAPI
from .api.auth_routes import auth_router
from .api.task_routes import task_router
from .database import engine
from .models.user import User
from .models.task import Task

# Create the FastAPI app
app = FastAPI(
    title="Todo API",
    description="A secure, multi-user todo application API",
    version="1.0.0"
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(task_router, prefix="/api", tags=["Tasks"])

@app.on_event("startup")
def on_startup():
    # Create database tables
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}