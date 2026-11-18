from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, distinct
from app.database.session import get_db
from app.models.resource import Resource
from app.models.domain import KnowledgeDomain
from app.models.institution import Institution

router = APIRouter(prefix="/statistics", tags=["Statistics"])


@router.get("")
def get_repository_statistics(db: Session = Depends(get_db)):
    """
    Provide live database-calculated statistics for the public portal and hero section.
    """
    total_resources = db.query(func.count(Resource.id)).filter(Resource.verification_status == "Verified").scalar() or 0
    total_domains = db.query(func.count(KnowledgeDomain.id)).filter(KnowledgeDomain.parent_id.is_(None)).scalar() or 0
    total_languages = db.query(func.count(distinct(Resource.language))).filter(Resource.verification_status == "Verified").scalar() or 0
    total_institutions = db.query(func.count(distinct(Resource.source_institution))).filter(Resource.verification_status == "Verified").scalar() or 0

    # Resource type breakdown
    type_counts = (
        db.query(Resource.resource_type, func.count(Resource.id))
        .filter(Resource.verification_status == "Verified")
        .group_by(Resource.resource_type)
        .all()
    )

    # Access status breakdown
    status_counts = (
        db.query(Resource.access_status, func.count(Resource.id))
        .filter(Resource.verification_status == "Verified")
        .group_by(Resource.access_status)
        .all()
    )

    # Top languages breakdown
    language_counts = (
        db.query(Resource.language, func.count(Resource.id))
        .filter(Resource.verification_status == "Verified")
        .group_by(Resource.language)
        .order_by(func.count(Resource.id).desc())
        .limit(6)
        .all()
    )

    return {
        "total_resources": total_resources,
        "total_domains": total_domains,
        "total_languages": total_languages,
        "total_institutions": total_institutions,
        "resource_types": {t[0]: t[1] for t in type_counts},
        "access_statuses": {s[0]: s[1] for s in status_counts},
        "top_languages": {l[0]: l[1] for l in language_counts}
    }
