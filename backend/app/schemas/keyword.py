from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class KeywordBase(BaseModel):
    keyword: str = Field(..., max_length=100)
    slug: str = Field(..., max_length=100)


class KeywordCreate(KeywordBase):
    pass


class KeywordResponse(KeywordBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
