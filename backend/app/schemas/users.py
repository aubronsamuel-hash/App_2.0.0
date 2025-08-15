from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    email: EmailStr
    username: str
    password: str
    role: str = "intermittent"
    prefs: Dict[str, Optional[str]] = {}


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: str
    prefs: Dict[str, Optional[str]]
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
