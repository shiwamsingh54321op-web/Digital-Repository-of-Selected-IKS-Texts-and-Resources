import json
from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app.database.session import get_db
from app.security.deps import get_current_admin
from app.models.user import AdminUser
from app.models.resource import Resource
from app.models.domain import KnowledgeDomain
from app.models.license import License
from app.models.institution import Institution
from app.models.search_history import SearchHistory
from app.repositories.resource_repository import ResourceRepository
from app.repositories.domain_repository import DomainRepository
from app.repositories.license_repository import LicenseRepository
from app.repositories.institution_repository import InstitutionRepository
from app.services.export_service import ExportService
from app.schemas.resource import (
    ResourceCreate,
    ResourceUpdate,
    VerificationUpdate,
    ResourceResponse,
    PaginatedResources,
)
from app.schemas.domain import KnowledgeDomainCreate, KnowledgeDomainUpdate, KnowledgeDomainResponse
from app.schemas.license import LicenseCreate, LicenseResponse
from app.schemas.institution import InstitutionCreate, InstitutionResponse

router = APIRouter(prefix="/admin", tags=["Administrative Control Panel"])


# --- DASHBOARD & ANALYTICS ---

@router.get("/dashboard")
def get_admin_dashboard(
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Overview statistics and metrics for the administration dashboard.
    """
    total_resources = db.query(func.count(Resource.id)).scalar() or 0
    published_resources = db.query(func.count(Resource.id)).filter(Resource.verification_status == "Verified").scalar() or 0
    pending_verification = db.query(func.count(Resource.id)).filter(Resource.verification_status == "Pending").scalar() or 0
    rejected_resources = db.query(func.count(Resource.id)).filter(Resource.verification_status == "Rejected").scalar() or 0
    total_domains = db.query(func.count(KnowledgeDomain.id)).scalar() or 0
    total_institutions = db.query(func.count(Institution.id)).scalar() or 0
    total_licenses = db.query(func.count(License.id)).scalar() or 0

    # Access status distribution
    access_counts = (
        db.query(Resource.access_status, func.count(Resource.id))
        .group_by(Resource.access_status)
        .all()
    )

    # Resource type distribution
    type_counts = (
        db.query(Resource.resource_type, func.count(Resource.id))
        .group_by(Resource.resource_type)
        .all()
    )

    # Verification distribution
    verification_counts = (
        db.query(Resource.verification_status, func.count(Resource.id))
        .group_by(Resource.verification_status)
        .all()
    )

    return {
        "overview": {
            "total_resources": total_resources,
            "published_resources": published_resources,
            "pending_verification": pending_verification,
            "rejected_resources": rejected_resources,
            "total_domains": total_domains,
            "total_institutions": total_institutions,
            "total_licenses": total_licenses
        },
        "distributions": {
            "access_statuses": {r[0]: r[1] for r in access_counts},
            "resource_types": {r[0]: r[1] for r in type_counts},
            "verification_statuses": {r[0]: r[1] for r in verification_counts}
        }
    }


@router.get("/analytics")
def get_admin_analytics(
    limit: int = Query(50, ge=1, le=200),
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Retrieve anonymized search queries, filter patterns, and retrieval trends.
    """
    recent_searches = (
        db.query(SearchHistory)
        .order_by(desc(SearchHistory.created_at))
        .limit(limit)
        .all()
    )

    # Frequent search queries
    top_queries = (
        db.query(SearchHistory.query, func.count(SearchHistory.id).label("freq"))
        .group_by(SearchHistory.query)
        .order_by(desc("freq"))
        .limit(10)
        .all()
    )

    return {
        "recent_searches": [
            {
                "id": s.id,
                "query": s.query,
                "filters_used": json.loads(s.filters_used) if s.filters_used else {},
                "result_count": s.result_count,
                "created_at": s.created_at
            }
            for s in recent_searches
        ],
        "top_queries": [{"query": t[0], "count": t[1]} for t in top_queries]
    }


# --- RESOURCE CRUD & VERIFICATION ---

@router.get("/resources", response_model=PaginatedResources)
def list_admin_resources(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    verification_status: Optional[str] = Query(None),
    resource_type: Optional[str] = Query(None),
    domain_id: Optional[int] = Query(None),
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    List all resources for administrative management, including unverified and pending records.
    """
    skip = (page - 1) * page_size
    items, total = ResourceRepository.get_all(
        db=db,
        skip=skip,
        limit=page_size,
        domain_id=domain_id,
        resource_type=resource_type,
        verification_status=verification_status,
        sort_by="newest"
    )

    total_pages = (total + page_size - 1) // page_size if total > 0 else 1

    return PaginatedResources(
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        has_next=page < total_pages,
        has_prev=page > 1,
        items=items
    )


@router.post("/resources", response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
def create_resource(
    resource_in: ResourceCreate,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Add a new IKS resource record into the repository.
    Validates knowledge domain and license integrity.
    """
    # Verify domain exists
    domain = DomainRepository.get_by_id(db, resource_in.knowledge_domain_id)
    if not domain:
        raise HTTPException(status_code=400, detail="Specified knowledge domain does not exist")

    # Verify license exists
    lic = LicenseRepository.get_by_id(db, resource_in.license_id)
    if not lic:
        raise HTTPException(status_code=400, detail="Specified license does not exist")

    return ResourceRepository.create(db, resource_in)


@router.put("/resources/{resource_id}", response_model=ResourceResponse)
def update_resource(
    resource_id: int,
    resource_in: ResourceUpdate,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Update metadata or categorization for an existing resource record.
    """
    resource = ResourceRepository.get_by_id(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    if resource_in.knowledge_domain_id is not None:
        if not DomainRepository.get_by_id(db, resource_in.knowledge_domain_id):
            raise HTTPException(status_code=400, detail="Specified knowledge domain does not exist")

    if resource_in.license_id is not None:
        if not LicenseRepository.get_by_id(db, resource_in.license_id):
            raise HTTPException(status_code=400, detail="Specified license does not exist")

    return ResourceRepository.update(db, resource, resource_in)


@router.delete("/resources/{resource_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resource(
    resource_id: int,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Permanently delete a resource record from the repository.
    """
    resource = ResourceRepository.get_by_id(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    ResourceRepository.delete(db, resource)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/resources/{resource_id}/verification", response_model=ResourceResponse)
def verify_resource_status(
    resource_id: int,
    verification: VerificationUpdate,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Administrative review workflow: Approve, verify or reject resource rights and licensing.
    """
    resource = ResourceRepository.get_by_id(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    resource.verification_status = verification.verification_status
    if verification.rights_statement:
        resource.rights_statement = verification.rights_statement

    if verification.verification_status == "Verified":
        resource.verified_at = datetime.utcnow()
    else:
        resource.verified_at = None

    resource.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(resource)
    return resource


# --- DOMAIN MANAGEMENT ---

@router.post("/domains", response_model=KnowledgeDomainResponse, status_code=status.HTTP_201_CREATED)
def create_domain(
    domain_in: KnowledgeDomainCreate,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Create a new knowledge domain or subcategory."""
    if DomainRepository.get_by_slug(db, domain_in.slug):
        raise HTTPException(status_code=400, detail="Domain with this slug already exists")
    return DomainRepository.create(db, domain_in)


@router.put("/domains/{domain_id}", response_model=KnowledgeDomainResponse)
def update_domain(
    domain_id: int,
    domain_in: KnowledgeDomainUpdate,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Update a knowledge domain."""
    domain = DomainRepository.get_by_id(db, domain_id)
    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")
    return DomainRepository.update(db, domain, domain_in)


@router.delete("/domains/{domain_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_domain(
    domain_id: int,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Delete a knowledge domain if no resources are associated with it."""
    domain = DomainRepository.get_by_id(db, domain_id)
    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")

    res_count = db.query(Resource).filter(Resource.knowledge_domain_id == domain_id).count()
    if res_count > 0:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot delete domain: {res_count} resources are currently assigned to it."
        )

    DomainRepository.delete(db, domain)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- LICENSE & INSTITUTION CREATION ---

@router.post("/licenses", response_model=LicenseResponse, status_code=status.HTTP_201_CREATED)
def create_license(
    license_in: LicenseCreate,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Register a new license classification."""
    if LicenseRepository.get_by_identifier(db, license_in.identifier):
        raise HTTPException(status_code=400, detail="License with this identifier already exists")
    return LicenseRepository.create(db, license_in)


@router.post("/institutions", response_model=InstitutionResponse, status_code=status.HTTP_201_CREATED)
def create_institution(
    institution_in: InstitutionCreate,
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """Register a new source institution or archive."""
    return InstitutionRepository.create(db, institution_in)


# --- METADATA EXPORT ---

@router.get("/export/csv")
@router.get("/export/resources.csv")
def export_csv(
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Export all repository metadata in Dublin Core-compliant CSV format.
    """
    csv_data = ExportService.export_resources_csv(db)
    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=iks_repository_resources.csv"}
    )


@router.get("/export/json")
@router.get("/export/resources.json")
def export_json(
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Export all repository metadata in structured JSON format.
    """
    data = ExportService.export_resources_json(db)
    return Response(
        content=json.dumps(data, indent=2),
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=iks_repository_resources.json"}
    )


@router.get("/export/bibtex")
@router.get("/export/resources.bibtex")
def export_bibtex(
    current_admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Export all repository metadata in BibTeX format.
    """
    resources = db.query(Resource).order_by(Resource.id.asc()).all()
    entries = []
    for r in resources:
        year = r.publication_date or "n.d."
        entries.append(
            f"@misc{{iks_{r.id},\n"
            f"  author = {{{r.creator}}},\n"
            f"  title = {{{r.title}}},\n"
            f"  year = {{{year}}},\n"
            f"  publisher = {{{r.source_institution}}},\n"
            f"  url = {{{r.source_url}}},\n"
            f"  note = {{Accessed via IKS Digital Repository}}\n"
            f"}}"
        )
    bibtex_data = "\n\n".join(entries)
    return Response(
        content=bibtex_data,
        media_type="application/x-bibtex",
        headers={"Content-Disposition": "attachment; filename=iks_repository_resources.bib"}
    )
