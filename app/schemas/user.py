"""
Pydantic schemas for user requests and responses.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    """Shared user fields."""

    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    """Schema for user registration."""

    password: str


class UserLogin(BaseModel):
    """Schema for user login."""

    email: EmailStr
    password: str


class UserRead(UserBase):
    """Schema returned by the API."""

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)