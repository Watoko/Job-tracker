"""
Authentication service.
"""

from app.core.security import create_access_token
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.auth import LoginRequest, Token
from app.schemas.user import UserCreate


class AuthService:
    """Authentication business logic."""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user_in: UserCreate) -> User:
        """
        Register a new user.
        """

        existing = self.user_repository.get_by_email(user_in.email)

        if existing:
            raise ValueError("Email already registered.")

        return self.user_repository.create(user_in)

    def login_user(self, login_data: LoginRequest) -> Token:
        """
        Authenticate a user and return JWT token.
        """

        user = self.user_repository.authenticate_user(
            login_data.email,
            login_data.password,
        )

        if not user:
            raise ValueError("Invalid email or password.")

        access_token = create_access_token(user.email)

        return Token(
            access_token=access_token,
            token_type="bearer",
        )
