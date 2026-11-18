from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class LicenseBase(BaseModel):
    name: str = Field(..., max_length=150, description="Full human-readable license name")
    identifier: str = Field(..., max_length=100, description="Unique license slug/identifier")
    license_url: Optional[str] = Field(None, max_length=500, description="Official legal text URL")
    description: Optional[str] = Field(None, description="Summary of rights granted")
    permissions: Optional[str] = Field(None, description="Granular permissions summary")
    commercial_use_allowed: bool = Field(False, description="Whether commercial reuse is permitted")
    redistribution_allowed: bool = Field(False, description="Whether distribution or download is permitted")
    attribution_required: bool = Field(True, description="Whether creator attribution is required")
    verification_notes: Optional[str] = Field(None, description="Scholarly or institutional notes on verification")


class LicenseCreate(LicenseBase):
    pass


class LicenseUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=150)
    identifier: Optional[str] = Field(None, max_length=100)
    license_url: Optional[str] = Field(None, max_length=500)
    description: Optional[str] = None
    permissions: Optional[str] = None
    commercial_use_allowed: Optional[bool] = None
    redistribution_allowed: Optional[bool] = None
    attribution_required: Optional[bool] = None
    verification_notes: Optional[str] = None


class LicenseResponse(LicenseBase):
    id: int
    created_at: datetime
    resource_count: Optional[int] = 0

    model_config = ConfigDict(from_attributes=True)
