from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_session
from ..models import Assignment
from ..schemas import AssignmentIn, AssignmentOut
from ..security import require_auth
from ..rate_limit import rate_limit_dependency

router = APIRouter(prefix="/assignments", tags=["assignments"], dependencies=[Depends(require_auth)])


@router.get("/", response_model=List[AssignmentOut])
async def list_assignments(session: AsyncSession = Depends(get_session)):
    result = await session.scalars(select(Assignment))
    return result.all()


@router.post("/", response_model=AssignmentOut, dependencies=[Depends(rate_limit_dependency)])
async def create_assignment(
    data: AssignmentIn, session: AsyncSession = Depends(get_session)
):
    assignment = Assignment(**data.model_dump())
    session.add(assignment)
    await session.commit()
    await session.refresh(assignment)
    return assignment


@router.get("/{assignment_id}", response_model=AssignmentOut)
async def get_assignment(
    assignment_id: int, session: AsyncSession = Depends(get_session)
):
    assignment = await session.get(Assignment, assignment_id)
    return assignment
