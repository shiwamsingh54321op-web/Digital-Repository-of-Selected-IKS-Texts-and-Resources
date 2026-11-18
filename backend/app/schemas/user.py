from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class AdminUserBase(BaseModel):
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=120)
    role: str = Field("administrator", max_length=50)
    is_active: bool = True


class AdminUserCreate(AdminUserBase):
    password: str = Field(..., min_length=8)


class AdminUserResponse(AdminUserBase):
    id: int
    created_at: datetime
    last_login: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: AdminUserResponse
