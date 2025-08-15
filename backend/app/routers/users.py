from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .. import models, schemas
from ..deps import get_session
from ..auth import get_current_admin

router = APIRouter()

@router.get("/", response_model=list[schemas.UserRead])
async def list_users(session: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_admin)):
    result = await session.execute(select(models.User))
    return result.scalars().all()
