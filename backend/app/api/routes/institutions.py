from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.institution_repository import InstitutionRepository
from app.schemas.institution import InstitutionResponse

router = APIRouter(prefix="/institutions", tags=["Institutions"])


@router.get("", response_model=List[InstitutionResponse])
def get_institutions(db: Session = Depends(get_db)):
    """
    List registered source archives, libraries, and universities.
    """
    institutions = InstitutionRepository.get_all(db)
    counts = InstitutionRepository.get_resource_counts(db)

    results = []
    for inst in institutions:
        resp = InstitutionResponse(
            id=inst.id,
            institution_name=inst.institution_name,
            website_url=inst.website_url,
            description=inst.description,
            country=inst.country,
            institution_type=inst.institution_type,
            contact_information=inst.contact_information,
            created_at=inst.created_at,
            resource_count=counts.get(inst.id, 0)
        )
        results.append(resp)

    return results
