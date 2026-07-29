"""
Centralised application configuration.

All settings are loaded from environment variables.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from .env.
    """

    APP_NAME: str = "Job Tracker API"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()