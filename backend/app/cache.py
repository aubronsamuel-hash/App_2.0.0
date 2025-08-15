import json
from functools import wraps
from typing import Any, Awaitable, Callable, Coroutine

from redis.asyncio import Redis

from .config import settings


redis = Redis.from_url(settings.redis_url, decode_responses=True)


def cache(ttl: int):
    def decorator(func: Callable[..., Awaitable[Any]]):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = f"cache:{func.__name__}:{args}:{kwargs}"
            cached = await redis.get(key)
            if cached is not None:
                return json.loads(cached)
            result = await func(*args, **kwargs)
            await redis.setex(key, ttl, json.dumps(result))
            return result

        return wrapper

    return decorator
