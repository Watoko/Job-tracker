"""
SQLAlchemy ORM models.
"""

from app.models.job import JobApplication
from app.models.user import User

__all__ = [
    "JobApplication",
    "User",
]
