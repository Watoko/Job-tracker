"""
Database dependencies for FastAPI.
"""

from collections.abc import Generator

from app.db.session import SessionLocal


def get_db() -> Generator:
    """
    Yield a database session and ensure it is closed afterwards.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
