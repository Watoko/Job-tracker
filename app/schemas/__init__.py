"""
Application Pydantic schemas.
"""

from app.schemas.auth import LoginRequest, Token
from app.schemas.job import (
    JobApplicationCreate,
    JobApplicationRead,
    JobApplicationUpdate,
)
from app.schemas.user import UserBase, UserCreate, UserLogin, UserRead

__all__ = [
    "JobApplicationCreate",
    "JobApplicationRead",
    "JobApplicationUpdate",
    "LoginRequest",
    "Token",
    "UserBase",
    "UserCreate",
    "UserLogin",
    "UserRead",
]
