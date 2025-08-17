from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AssignmentIn(BaseModel):
    mission_id: int
    user_id: Optional[int] = None
    role_label: str
    status: str = "invited"
    channel: Optional[str] = None


class AssignmentOut(AssignmentIn):
    id: int
    responded_at: Optional[datetime] = None

    class Config:
        from_attributes = True
