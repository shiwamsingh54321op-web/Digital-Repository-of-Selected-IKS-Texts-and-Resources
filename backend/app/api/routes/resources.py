from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.resource_repository import ResourceRepository
from app.services.resource_service import ResourceService
from app.schemas.resource import (
    ResourceResponse,
    ResourceDetailResponse,
    PaginatedResources,
)

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.get("", response_model=PaginatedResources)
def list_resources(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(12, ge=1, le=100, description="Items per page"),
    domain_id: Optional[int] = Query(None, description="Filter by domain ID"),
    domain_slug: Optional[str] = Query(None, description="Filter by domain slug"),
    resource_type: Optional[str] = Query(None, description="Filter by resource type"),
    language: Optional[str] = Query(None, description="Filter by language"),
    access_status: Optional[str] = Query(None, description="Filter by access status"),
    license_id: Optional[int] = Query(None, description="Filter by license ID"),
    institution_id: Optional[int] = Query(None, description="Filter by source institution ID"),
    sort_by: str = Query("newest", description="newest, oldest, title_asc, title_desc"),
    db: Session = Depends(get_db)
):
    """
    Public catalogue endpoint to list verified repository resources with pagination and faceted filters.
    """
    skip = (page - 1) * page_size
    items, total = ResourceRepository.get_all(
        db=db,
        skip=skip,
        limit=page_size,
        domain_id=domain_id,
        domain_slug=domain_slug,
        resource_type=resource_type,
        language=language,
        access_status=access_status,
        license_id=license_id,
        institution_id=institution_id,
        verification_status="Verified",
        sort_by=sort_by
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


@router.get("/{resource_id}", response_model=ResourceDetailResponse)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    """
    Get comprehensive details, full Dublin Core metadata, and download eligibility for a resource.
    """
    return ResourceService.get_resource_details(db, resource_id)


@router.get("/{resource_id}/related", response_model=List[ResourceResponse])
def get_related_resources(resource_id: int, limit: int = 4, db: Session = Depends(get_db)):
    """
    Retrieve related resources based on subject or knowledge domain classification.
    """
    resource = ResourceRepository.get_by_id(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return ResourceRepository.get_related(db, resource, limit=limit)


@router.get("/{resource_id}/citation")
def get_resource_citations(resource_id: int, db: Session = Depends(get_db)):
    """
    Generate scholarly bibliographic citations (APA, MLA, Chicago, BibTeX).
    """
    resource = ResourceRepository.get_by_id(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return ResourceService.generate_citations(resource)


@router.get("/{resource_id}/download")
def download_resource(resource_id: int, db: Session = Depends(get_db)):
    """
    Controlled download facility.
    Strictly verifies legal permissions before permitting file retrieval.
    Denies access with 403 Forbidden if rights are unverified or reproduction is prohibited.
    """
    resource = ResourceRepository.get_by_id(db, resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    # Legal Permission Verification
    if resource.verification_status != "Verified":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Download unavailable: This resource is pending legal rights verification."
        )

    if resource.access_status in ("Restricted Access", "Metadata Only", "Pending Verification"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Direct download is prohibited under '{resource.access_status}'. Please consult the original source institution."
        )

    # Check license redistribution permissions
    if resource.license and not resource.license.redistribution_allowed and resource.access_status != "Download Available":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Licensing restriction: The license '{resource.license.name}' does not allow direct redistribution. You may read the text online at the source institution."
        )

    target_url = resource.download_url or resource.access_url or resource.source_url
    if not target_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No download URL is associated with this verified record."
        )

    return {
        "status": "permitted",
        "resource_id": resource.id,
        "title": resource.title,
        "license": resource.license.name if resource.license else "Verified Open Access",
        "download_url": target_url,
        "file_format": resource.file_format or "PDF"
    }
