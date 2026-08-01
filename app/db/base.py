"""
Base class for all SQLAlchemy ORM models.

Every model in the application should inherit from Base.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy models.
    """

    pass



