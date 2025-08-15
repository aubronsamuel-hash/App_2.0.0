from fastapi import APIRouter

from .. import __version__
from ..db import check_db
from ..cache import redis

router = APIRouter()


@router.get("/healthz")
async def healthz():
    db_ok = await check_db()
    try:
        await redis.ping()
        redis_ok = True
    except Exception:
        redis_ok = False
    return {"ok": True, "db": db_ok, "redis": redis_ok, "version": __version__}
