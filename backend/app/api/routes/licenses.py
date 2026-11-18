from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.license_repository import LicenseRepository
from app.schemas.license import LicenseResponse

router = APIRouter(prefix="/licenses", tags=["Licenses"])


@router.get("", response_model=List[LicenseResponse])
def get_licenses(db: Session = Depends(get_db)):
    """
    List all supported licensing classifications with legal permission boundaries.
    """
    licenses = LicenseRepository.get_all(db)
    counts = LicenseRepository.get_resource_counts(db)

    results = []
    for lic in licenses:
        resp = LicenseResponse(
            id=lic.id,
            name=lic.name,
            identifier=lic.identifier,
            license_url=lic.license_url,
            description=lic.description,
            permissions=lic.permissions,
            commercial_use_allowed=lic.commercial_use_allowed,
            redistribution_allowed=lic.redistribution_allowed,
            attribution_required=lic.attribution_required,
            verification_notes=lic.verification_notes,
            created_at=lic.created_at,
            resource_count=counts.get(lic.id, 0)
        )
        results.append(resp)

    return results
