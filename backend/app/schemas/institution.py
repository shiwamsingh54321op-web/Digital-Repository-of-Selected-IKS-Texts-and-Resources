from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class InstitutionBase(BaseModel):
    institution_name: str = Field(..., max_length=200, description="Official name of the holding institution")
    website_url: Optional[str] = Field(None, max_length=500, description="Institutional portal URL")
    description: Optional[str] = Field(None, description="Overview of the repository or archive")
    country: str = Field("India", max_length=100, description="Country of institution")
    institution_type: Optional[str] = Field(None, max_length=100, description="Type: University, National Archive, etc.")
    contact_information: Optional[str] = Field(None, description="Public inquiry details")


class InstitutionCreate(InstitutionBase):
    pass


class InstitutionUpdate(BaseModel):
    institution_name: Optional[str] = Field(None, max_length=200)
    website_url: Optional[str] = Field(None, max_length=500)
    description: Optional[str] = None
    country: Optional[str] = Field(None, max_length=100)
    institution_type: Optional[str] = Field(None, max_length=100)
    contact_information: Optional[str] = None


class InstitutionResponse(InstitutionBase):
    id: int
    created_at: datetime
    resource_count: Optional[int] = 0

    model_config = ConfigDict(from_attributes=True)
