import secrets
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from sqlalchemy import select

from .cache import redis
from .config import settings
from .db import async_session
from .models.users import User, RoleEnum


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
token_scheme = HTTPBearer(auto_error=False)


async def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


async def create_access_token(user_id: int) -> str:
    token = secrets.token_urlsafe(32)
    await redis.setex(f"token:{token}", settings.token_ttl_min * 60, str(user_id))
    return token


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(token_scheme),
) -> User:
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    token = credentials.credentials
    user_id = await redis.get(f"token:{token}")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    async with async_session() as session:
        user = await session.get(User, int(user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user


async def get_current_user_optional(
    credentials: HTTPAuthorizationCredentials = Depends(token_scheme),
) -> Optional[User]:
    if credentials is None:
        return None
    token = credentials.credentials
    user_id = await redis.get(f"token:{token}")
    if user_id is None:
        return None
    async with async_session() as session:
        return await session.get(User, int(user_id))


async def require_auth(user: User = Depends(get_current_user)) -> User:
    return user


async def require_admin(user: User = Depends(get_current_user)) -> User:
    if user.role != RoleEnum.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return user
