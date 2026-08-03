"""
Database engine and session configuration.

This module creates the SQLAlchemy engine and provides
a session factory for interacting with PostgreSQL.
"""

# SQLAlchemy Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# Local Imports
from app.core.config import settings

# --------------------------------------------------------------------
# Database Engine
# --------------------------------------------------------------------

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
)

# --------------------------------------------------------------------
# Session Factory
# --------------------------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    class_=Session,
)
