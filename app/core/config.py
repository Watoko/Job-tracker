"""
Application configuration.

Loads application settings from environment variables and the .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    # --------------------------------------------------------------------
    # Application
    # --------------------------------------------------------------------

    APP_NAME: str = "Job Tracker API"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    # --------------------------------------------------------------------
    # Database
    # --------------------------------------------------------------------

    DATABASE_URL: str

    # --------------------------------------------------------------------
    # JWT Authentication
    # --------------------------------------------------------------------

    SECRET_KEY: str = (
        "4d2f9d0a9b3245f8b8d6a0c1e7f9b6d2"
        "a4c5e8f1b2d3c6f7a8b9c0d1e2f3a4b5"
    )

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # --------------------------------------------------------------------
    # Pydantic Settings
    # --------------------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()