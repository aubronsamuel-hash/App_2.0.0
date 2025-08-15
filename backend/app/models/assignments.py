import enum
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import Base


class AssignmentStatus(str, enum.Enum):
    invited = "invited"
    confirmed = "confirmed"
    declined = "declined"
    removed = "removed"


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey("missions.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    role_label = Column(String, nullable=False)
    status = Column(Enum(AssignmentStatus), default=AssignmentStatus.invited)
    channel = Column(String, nullable=True)
    responded_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    mission = relationship("Mission", back_populates="assignments")
    user = relationship("User", back_populates="assignments")
