"""
Authentication API endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.deps import get_db
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.auth import LoginRequest, Token
from app.schemas.user import UserCreate
from app.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register", status_code=201)
def register_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
):
    """
    Register a new user.
    """
    service = AuthService(UserRepository(db))

    try:
        user = service.register_user(user_in)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active,
    }


@router.post("/login", response_model=Token)
def login_user(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
):
    """
    Authenticate a user and return JWT token.
    """

    service = AuthService(UserRepository(db))

    try:
        return service.login_user(login_data)

    except ValueError as exc:
        raise HTTPException(
            status_code=401,
            detail=str(exc),
        )


@router.get("/me")
def get_current_user_profile(
    current_user: User = Depends(get_current_user),
):
    """
    Return the currently authenticated user.
    """

    return {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "is_active": current_user.is_active,
    }
