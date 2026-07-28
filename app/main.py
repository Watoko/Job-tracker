"""
Main entry point for the Job Tracker API.

Responsibilities:
    - Configure logging.
    - Create the FastAPI application.
    - Register API routers.
"""

# Standard Library Imports
import logging

# Third-Party Imports
from fastapi import FastAPI

# Local Application Imports
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging

# --------------------------------------------------------------------
# Logging Configuration
# --------------------------------------------------------------------

configure_logging()
logger = logging.getLogger(__name__)

# --------------------------------------------------------------------
# FastAPI Application
# --------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend API for tracking job applications.",
)

# Register version 1 routes.
app.include_router(api_router, prefix="/api/v1")


# --------------------------------------------------------------------
# Application Lifecycle Events
# --------------------------------------------------------------------


@app.on_event("startup")
async def startup_event() -> None:
    """
    Execute application startup tasks.
    """
    logger.info("Job Tracker API started successfully.")
