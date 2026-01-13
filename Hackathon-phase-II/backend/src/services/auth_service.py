from sqlmodel import Session, select
from typing import Optional
from datetime import timedelta, datetime
from uuid import UUID
from ..models.user import User, UserCreate
from ..utils.jwt_utils import verify_password, get_password_hash, create_access_token
from ..exceptions.custom_exceptions import InvalidCredentialsException, DuplicateResourceException
from ..utils.logging import get_logger

logger = get_logger(__name__)

class AuthService:
    def __init__(self, session: Session):
        self.session = session

    def register_user(self, user_data: UserCreate) -> User:
        """
        Register a new user with the provided data
        """
        # Check if user with this username or email already exists
        existing_user = self.get_user_by_username_or_email(user_data.username, user_data.email)
        if existing_user:
            if existing_user.username == user_data.username:
                raise DuplicateResourceException("User", "username", user_data.username)
            else:
                raise DuplicateResourceException("User", "email", user_data.email)

        # Create new user
        user = User.model_validate(user_data)
        user.password_hash = get_password_hash(user_data.password)
        
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        
        logger.info(f"User registered with ID: {user.id}")
        return user

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """
        Authenticate a user with the provided credentials
        """
        user = self.get_user_by_username(username)
        if not user or not verify_password(password, user.password_hash):
            logger.warning(f"Failed authentication attempt for username: {username}")
            return None
        
        # Update last login
        user.last_login = datetime.utcnow()
        self.session.add(user)
        self.session.commit()
        
        logger.info(f"User authenticated with ID: {user.id}")
        return user

    def create_access_token_for_user(self, user: User) -> str:
        """
        Create an access token for the authenticated user
        """
        data = {"sub": str(user.id), "username": user.username}
        token = create_access_token(data=data)
        
        logger.info(f"Access token created for user: {user.id}")
        return token

    def get_user_by_username(self, username: str) -> Optional[User]:
        """
        Retrieve a user by their username
        """
        statement = select(User).where(User.username == username)
        user = self.session.exec(statement).first()
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by their email
        """
        statement = select(User).where(User.email == email)
        user = self.session.exec(statement).first()
        return user

    def get_user_by_username_or_email(self, username: str, email: str) -> Optional[User]:
        """
        Retrieve a user by either username or email
        """
        statement = select(User).where((User.username == username) | (User.email == email))
        user = self.session.exec(statement).first()
        return user

    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        """
        Retrieve a user by their ID
        """
        statement = select(User).where(User.id == user_id)
        user = self.session.exec(statement).first()
        return user