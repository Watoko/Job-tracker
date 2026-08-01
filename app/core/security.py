"""
Security utilities.

Provides:
- Password hashing
- Password verification
- JWT creation
"""

from datetime import datetime, timedelta, UTC
from typing import Any

from jose import jwt
from pwdlib import PasswordHash

from app.core.config import settings

# --------------------------------------------------------------------
# Password Hashing
# --------------------------------------------------------------------

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Hash a plain-text password."""
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return password_hash.verify(password, hashed_password)


# --------------------------------------------------------------------
# JWT Tokens
# --------------------------------------------------------------------

def create_access_token(
    subject: str | Any,
    expires_delta: timedelta | None = None,
) -> str:
    """
    Create a JWT access token.
    """

    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    payload = {
        "sub": str(subject),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )