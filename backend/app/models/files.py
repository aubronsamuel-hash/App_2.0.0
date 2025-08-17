from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from ..db import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    mission_id = Column(Integer, ForeignKey("missions.id"), nullable=True)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
