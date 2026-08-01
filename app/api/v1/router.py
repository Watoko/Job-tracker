"""
Main router for API version 1.

All version 1 endpoints are registered here.
"""

# Third-Party Imports
from fastapi import APIRouter

# Local Application Imports
from app.api.v1.auth import router as auth_router
from app.api.v1.health import router as health_router

# --------------------------------------------------------------------
# API Router
# --------------------------------------------------------------------

api_router = APIRouter()

# Register feature routers.
api_router.include_router(health_router)
api_router.include_router(auth_router)
