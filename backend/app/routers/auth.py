from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_session
from ..models import User
from ..schemas import LoginIn, Token, UserIn, UserOut
from ..security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
async def login(data: LoginIn, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.email == data.email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = await create_access_token(user.id)
    return Token(access_token=token)


@router.post("/register", response_model=UserOut)
async def register(data: UserIn, session: AsyncSession = Depends(get_session)):
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
