"""
Health and root endpoints for API version 1.

This module provides simple endpoints used to verify that the API
is running and reachable.

Responsibilities:
    - Root endpoint
    - Health check endpoint
"""

# Third-Party Imports
from fastapi import APIRouter

# Local Application Imports
from app.core.config import settings

# --------------------------------------------------------------------
# Router Configuration
# --------------------------------------------------------------------

router = APIRouter(tags=["Health"])


@router.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint.

    Returns:
        dict[str, str]: Welcome message confirming the API is running.
    """
    return {"message": f"Welcome to {settings.APP_NAME}!"}


@router.get("/health")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns:
        dict[str, str]: Current API health status.
    """
    return {"status": "healthy"}
