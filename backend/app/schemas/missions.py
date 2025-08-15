from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, field_validator


class Position(BaseModel):
    label: str
    count: int = Field(ge=1)
    skills: Dict[str, str] = {}


class MissionIn(BaseModel):
    title: str
    start: datetime
    end: datetime
    location: str
    call_time: Optional[datetime] = None
    positions: List[Position] = []
    documents: List[str] = []
    status: str = "draft"
    created_by: int

    @field_validator("end")
    @classmethod
    def validate_dates(cls, v, info):
        start = info.data.get("start")
        if start and v <= start:
            raise ValueError("end must be after start")
        return v

    @field_validator("positions")
    @classmethod
    def unique_labels(cls, v: List[Position]):
        labels = [p.label for p in v]
        if len(labels) != len(set(labels)):
            raise ValueError("duplicate position labels")
        return v


class MissionOut(MissionIn):
    id: int

    class Config:
        from_attributes = True
