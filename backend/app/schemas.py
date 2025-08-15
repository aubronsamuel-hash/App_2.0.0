from pydantic import BaseModel, ConfigDict

class MissionBase(BaseModel):
    title: str
    description: str | None = None

class MissionCreate(MissionBase):
    pass

class MissionUpdate(MissionBase):
    published: bool | None = None

class MissionRead(MissionBase):
    id: int
    published: bool
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserRead(BaseModel):
    id: int
    username: str
    role: str
    model_config = ConfigDict(from_attributes=True)
