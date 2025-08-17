from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_session
from ..models import Mission
from ..schemas import MissionIn, MissionOut
from ..security import require_auth
from ..rate_limit import rate_limit_dependency

router = APIRouter(prefix="/missions", tags=["missions"], dependencies=[Depends(require_auth)])


@router.get("/", response_model=List[MissionOut])
async def list_missions(session: AsyncSession = Depends(get_session)):
    result = await session.scalars(select(Mission))
    return result.all()


@router.post("/", response_model=MissionOut, dependencies=[Depends(rate_limit_dependency)])
async def create_mission(
    data: MissionIn, session: AsyncSession = Depends(get_session)
):
    mission = Mission(**data.model_dump())
    session.add(mission)
    await session.commit()
    await session.refresh(mission)
    return mission


@router.get("/{mission_id}", response_model=MissionOut)
async def get_mission(mission_id: int, session: AsyncSession = Depends(get_session)):
    mission = await session.get(Mission, mission_id)
    return mission
