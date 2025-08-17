from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_session
from ..models import User
from ..schemas import UserIn, UserOut
from ..security import require_admin, hash_password
from ..rate_limit import rate_limit_dependency

router = APIRouter(
    prefix="/admin/users",
    tags=["admin"],
    dependencies=[Depends(require_admin)],
)


@router.get("/", response_model=List[UserOut])
async def list_users(session: AsyncSession = Depends(get_session)):
    result = await session.scalars(select(User))
    return result.all()


@router.post("/", response_model=UserOut, dependencies=[Depends(rate_limit_dependency)])
async def create_user(data: UserIn, session: AsyncSession = Depends(get_session)):
    hashed = await hash_password(data.password)
    user = User(
        email=data.email,
        username=data.username,
        hashed_password=hashed,
        role=data.role,
        prefs=data.prefs,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
