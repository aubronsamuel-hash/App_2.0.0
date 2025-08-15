import asyncio
from redis.asyncio import from_url
from app.config import settings

async def main():
    redis = from_url(settings.redis_url, encoding="utf8", decode_responses=True)
    while True:
        msg = await redis.lpop("notifications")
        if msg:
            print(f"Notification: {msg}")
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
