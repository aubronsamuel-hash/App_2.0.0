from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .. import models, schemas
from ..deps import get_session
from ..auth import get_current_active_user, get_current_admin

router = APIRouter()

@router.get("/", response_model=list[schemas.MissionRead])
async def list_missions(session: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_active_user)):
    result = await session.execute(select(models.Mission))
    return result.scalars().all()

@router.post("/", response_model=schemas.MissionRead)
async def create_mission(data: schemas.MissionCreate, session: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_admin)):
    mission = models.Mission(**data.dict())
    session.add(mission)
    await session.commit()
    await session.refresh(mission)
    return mission

@router.put("/{mission_id}", response_model=schemas.MissionRead)
async def update_mission(mission_id: int, data: schemas.MissionUpdate, session: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_admin)):
    result = await session.execute(select(models.Mission).where(models.Mission.id == mission_id))
    mission = result.scalar_one_or_none()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    for k, v in data.dict(exclude_unset=True).items():
        setattr(mission, k, v)
    session.add(mission)
    await session.commit()
    await session.refresh(mission)
    return mission

@router.delete("/{mission_id}")
async def delete_mission(mission_id: int, session: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_admin)):
    result = await session.execute(select(models.Mission).where(models.Mission.id == mission_id))
    mission = result.scalar_one_or_none()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    await session.delete(mission)
    await session.commit()
    return {"ok": True}

@router.post("/{mission_id}/publish", response_model=schemas.MissionRead)
async def publish_mission(mission_id: int, session: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_admin)):
    result = await session.execute(select(models.Mission).where(models.Mission.id == mission_id))
    mission = result.scalar_one_or_none()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    mission.published = True
    await session.commit()
    await session.refresh(mission)
    return mission

@router.post("/{mission_id}/duplicate", response_model=schemas.MissionRead)
async def duplicate_mission(mission_id: int, session: AsyncSession = Depends(get_session), user: models.User = Depends(get_current_admin)):
    result = await session.execute(select(models.Mission).where(models.Mission.id == mission_id))
    mission = result.scalar_one_or_none()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    new_mission = models.Mission(title=mission.title, description=mission.description, published=False)
    session.add(new_mission)
    await session.commit()
    await session.refresh(new_mission)
    return new_mission
