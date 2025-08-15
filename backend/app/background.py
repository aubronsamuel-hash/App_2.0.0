from .cache import redis

QUEUE = "notifications"


async def enqueue_notification(payload: str) -> None:
    await redis.lpush(QUEUE, payload)


async def dequeue_notification() -> str | None:
    return await redis.rpop(QUEUE)
