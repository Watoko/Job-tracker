"""
Repository for user database operations.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:
    """Repository for User model."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email.
        """
        statement = select(User).where(User.email == email)
        return self.db.scalar(statement)

    def create(self, user_in: UserCreate) -> User:
        """
        Create a new user.
        """
        db_user = User(
            email=user_in.email,
            hashed_password=hash_password(user_in.password),
            full_name=user_in.full_name,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def authenticate_user(self, email: str, password: str) -> User | None:
        """
        Authenticate a user by email and password.
        """
        user = self.get_by_email(email)

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return user
