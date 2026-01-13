from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config.jwt_config import jwt_config

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password against a hashed password
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Generate a hash for a plaintext password
    """
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create a new access token with the provided data
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=jwt_config.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_config.SECRET_KEY, algorithm=jwt_config.ALGORITHM)
    
    return encoded_jwt

def verify_token(token: str) -> Optional[dict]:
    """
    Verify a token and return the payload if valid
    """
    try:
        payload = jwt.decode(token, jwt_config.SECRET_KEY, algorithms=[jwt_config.ALGORITHM])
        return payload
    except JWTError:
        return None