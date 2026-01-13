from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from datetime import timedelta
from uuid import UUID
from sqlmodel import Session
from .database import get_session
from .models.user import User, UserCreate, UserRead
from .services.auth_service import AuthService
from .utils.jwt_utils import verify_token
from .utils.logging import get_logger

auth_router = APIRouter()
security = HTTPBearer()
logger = get_logger(__name__)

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
) -> User:
    """
    Get the current authenticated user from the token
    """
    token = credentials.credentials
    payload = verify_token(token)
    
    if payload is None:
        logger.warning("Invalid token provided")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_id = payload.get("sub")
    if user_id is None:
        logger.warning("Token does not contain user ID")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        user_id_uuid = UUID(user_id)
    except ValueError:
        logger.warning(f"Invalid user ID format in token: {user_id}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    auth_service = AuthService(session)
    user = auth_service.get_user_by_id(user_id_uuid)
    
    if user is None:
        logger.warning(f"User not found for ID: {user_id_uuid}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

@auth_router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, session: Session = Depends(get_session)):
    """
    Register a new user
    """
    auth_service = AuthService(session)
    try:
        user = auth_service.register_user(user_data)
        logger.info(f"New user registered: {user.id}")
        return user
    except Exception as e:
        logger.error(f"Error registering user: {str(e)}")
        raise e

@auth_router.post("/login")
def login_user(username: str, password: str, session: Session = Depends(get_session)):
    """
    Authenticate user and return access token
    """
    auth_service = AuthService(session)
    user = auth_service.authenticate_user(username, password)
    
    if not user:
        logger.warning(f"Failed login attempt for username: {username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = auth_service.create_access_token_for_user(user)
    logger.info(f"User logged in: {user.id}")
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }