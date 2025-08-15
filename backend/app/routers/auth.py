from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .. import models, schemas, auth
from ..deps import get_session

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
async def login(user: schemas.UserLogin, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(models.User).where(models.User.username == user.username))
    db_user = result.scalar_one_or_none()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = auth.create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserRead)
async def me(current_user: models.User = Depends(auth.get_current_active_user)):
    return current_user
