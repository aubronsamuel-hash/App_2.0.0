import enum
from sqlalchemy import Column, DateTime, Enum, Integer, JSON, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import Base


class RoleEnum(str, enum.Enum):
    admin = "admin"
    intermittent = "intermittent"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.intermittent, nullable=False)
    prefs = Column(JSON, default=dict)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    assignments = relationship("Assignment", back_populates="user")
