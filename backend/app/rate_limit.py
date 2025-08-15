import time
from typing import Optional

from fastapi import Depends, HTTPException, Request, status

from .cache import redis
from .config import settings
from .security import get_current_user_optional
from .models.users import User

WINDOW = 60


async def _rate_limit(identifier: str, limit: int) -> None:
    now = time.time()
    key = f"rl:{identifier}"
    async with redis.pipeline() as pipe:
        await pipe.zremrangebyscore(key, 0, now - WINDOW)
        await pipe.zadd(key, {str(now): now})
        await pipe.zcard(key)
        await pipe.expire(key, WINDOW)
        _, _, count, _ = await pipe.execute()
    if count > limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Too many requests"
        )


async def rate_limit_dependency(
    request: Request, user: Optional[User] = Depends(get_current_user_optional)
) -> None:
    identifier = str(user.id) if user else request.client.host
    await _rate_limit(identifier, settings.rate_limit_per_min)
