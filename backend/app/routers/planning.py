from fastapi import APIRouter

from ..cache import cache

router = APIRouter(prefix="/planning", tags=["planning"])


@router.get("/{week}")
@cache(ttl=60)
async def get_planning(week: int):
    return {"week": week, "missions": []}
