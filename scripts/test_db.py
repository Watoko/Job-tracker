"""
Simple script to verify the application's database connection.

Run with:
    python scripts/test_db.py
"""

# SQLAlchemy Imports
from sqlalchemy import text

# Local Imports
from app.db.session import engine


def test_connection() -> None:
    """
    Connect to PostgreSQL and execute a simple query.
    """
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database();"))

        database_name = result.scalar()

        print("=" * 50)
        print("Database connection successful!")
        print(f"Connected database: {database_name}")
        print("=" * 50)


if __name__ == "__main__":
    test_connection()