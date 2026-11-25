from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.domain_repository import DomainRepository
from app.repositories.resource_repository import ResourceRepository
from app.schemas.domain import KnowledgeDomainResponse, KnowledgeDomainHierarchy
from app.schemas.resource import ResourceResponse
from app.data.domain_profiles import DOMAIN_PROFILES

router = APIRouter(prefix="/domains", tags=["Knowledge Domains"])


@router.get("", response_model=List[KnowledgeDomainHierarchy])
def get_domains(
    hierarchy: bool = Query(True, description="Return hierarchical parent-child category tree"),
    db: Session = Depends(get_db)
):
    """
    List all Indian Knowledge System domains with real database-calculated resource counts.
    """
    counts = DomainRepository.get_resource_counts(db)
    domains = DomainRepository.get_hierarchy(db) if hierarchy else DomainRepository.get_all(db)

    results = []
    for d in domains:
        sub_list = []
        for sub in getattr(d, "subcategories", []):
            sub_profile = DOMAIN_PROFILES.get(sub.slug, {})
            sub_resp = KnowledgeDomainResponse(
                id=sub.id,
                name=sub.name,
                slug=sub.slug,
                description=sub.description,
                parent_id=sub.parent_id,
                icon=sub.icon,
                created_at=sub.created_at,
                resource_count=counts.get(sub.id, 0),
                sanskrit_name=sub_profile.get("sanskrit_name"),
                profile=sub_profile or None
            )
            sub_list.append(sub_resp)

        d_profile = DOMAIN_PROFILES.get(d.slug, {})
        domain_resp = KnowledgeDomainHierarchy(
            id=d.id,
            name=d.name,
            slug=d.slug,
            description=d.description,
            parent_id=d.parent_id,
            icon=d.icon,
            created_at=d.created_at,
            resource_count=counts.get(d.id, 0),
            sanskrit_name=d_profile.get("sanskrit_name"),
            profile=d_profile or None,
            subcategories=sub_list
        )
        results.append(domain_resp)

    return results


@router.get("/{slug}")
def get_domain_by_slug(slug: str, db: Session = Depends(get_db)):
    """
    Get detailed domain information along with encyclopedic profile and associated resources.
    """
    domain = DomainRepository.get_by_slug(db, slug)
    if not domain:
        raise HTTPException(status_code=404, detail="Knowledge domain not found")

    counts = DomainRepository.get_resource_counts(db)
    resources, total = ResourceRepository.get_all(
        db=db,
        domain_id=domain.id,
        limit=32,
        verification_status="Verified"
    )

    profile = DOMAIN_PROFILES.get(domain.slug, {})
    parent_domain = None
    if domain.parent_id:
        p_obj = DomainRepository.get_by_id(db, domain.parent_id)
        if p_obj:
            parent_domain = {
                "id": p_obj.id,
                "name": p_obj.name,
                "slug": p_obj.slug,
                "sanskrit_name": DOMAIN_PROFILES.get(p_obj.slug, {}).get("sanskrit_name")
            }

    subcategories = [
        {
            "id": sub.id,
            "name": sub.name,
            "slug": sub.slug,
            "sanskrit_name": DOMAIN_PROFILES.get(sub.slug, {}).get("sanskrit_name"),
            "description": sub.description,
            "resource_count": counts.get(sub.id, 0)
        }
        for sub in getattr(domain, "subcategories", [])
    ]

    return {
        "domain": {
            "id": domain.id,
            "name": domain.name,
            "slug": domain.slug,
            "sanskrit_name": profile.get("sanskrit_name"),
            "description": domain.description,
            "icon": domain.icon,
            "parent_id": domain.parent_id,
            "resource_count": counts.get(domain.id, 0),
            "profile": profile or None
        },
        "parent_domain": parent_domain,
        "subcategories": subcategories,
        "total_resources": total,
        "resources": [ResourceResponse.model_validate(r) for r in resources]
    }
