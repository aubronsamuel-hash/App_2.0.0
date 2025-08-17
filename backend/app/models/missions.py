import enum
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, JSON, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import Base


class MissionStatus(str, enum.Enum):
    draft = "draft"
    published = "published"


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    start = Column(DateTime, nullable=False, index=True)
    end = Column(DateTime, nullable=False, index=True)
    location = Column(String, nullable=False)
    call_time = Column(DateTime, nullable=True)
    positions = Column(JSON, default=list)
    documents = Column(JSON, default=list)
    status = Column(Enum(MissionStatus), default=MissionStatus.draft)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    assignments = relationship("Assignment", back_populates="mission")
