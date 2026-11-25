from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class KnowledgeDomainBase(BaseModel):
    name: str = Field(..., max_length=150, description="Domain display name")
    slug: str = Field(..., max_length=150, description="URL-friendly slug")
    description: Optional[str] = Field(None, description="Detailed scope of the domain")
    parent_id: Optional[int] = Field(None, description="Parent domain ID for subcategories")
    icon: Optional[str] = Field("BookOpen", max_length=60, description="Lucide icon identifier")


class KnowledgeDomainCreate(KnowledgeDomainBase):
    pass


class KnowledgeDomainUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=150)
    slug: Optional[str] = Field(None, max_length=150)
    description: Optional[str] = None
    parent_id: Optional[int] = None
    icon: Optional[str] = Field(None, max_length=60)


class KnowledgeDomainResponse(KnowledgeDomainBase):
    id: int
    created_at: datetime
    resource_count: Optional[int] = 0
    sanskrit_name: Optional[str] = None
    profile: Optional[Dict[str, Any]] = None

    model_config = ConfigDict(from_attributes=True)


class KnowledgeDomainHierarchy(KnowledgeDomainResponse):
    subcategories: List[KnowledgeDomainResponse] = []

    model_config = ConfigDict(from_attributes=True)
