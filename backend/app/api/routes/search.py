from typing import Optional, List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.search_service import SearchService
from app.schemas.search import SearchResponse, SearchSuggestionItem

router = APIRouter(prefix="/search", tags=["Information Retrieval Engine"])


@router.get("", response_model=SearchResponse)
def execute_search(
    q: Optional[str] = Query(None, description="Keywords, natural language phrases, or creator names"),
    domain_id: Optional[int] = Query(None, description="Filter by domain ID"),
    domain_slug: Optional[str] = Query(None, description="Filter by domain slug"),
    resource_type: Optional[str] = Query(None, description="Filter by resource type"),
    language: Optional[str] = Query(None, description="Filter by original language"),
    access_status: Optional[str] = Query(None, description="Filter by access status"),
    license_id: Optional[int] = Query(None, description="Filter by license ID"),
    institution_id: Optional[int] = Query(None, description="Filter by institution ID"),
    sort_by: str = Query("relevance", description="relevance, title_asc, title_desc, newest, oldest"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(12, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db)
):
    """
    Execute full-text information retrieval using SQLite FTS5 and BM25 relevance ranking.
    Prioritizes matches in title, subject, creator, and keywords with column weighting.
    """
    return SearchService.execute_search(
        db=db,
        query=q,
        domain_id=domain_id,
        domain_slug=domain_slug,
        resource_type=resource_type,
        language=language,
        access_status=access_status,
        license_id=license_id,
        institution_id=institution_id,
        verification_status="Verified",
        sort_by=sort_by,
        page=page,
        page_size=page_size,
        log_history=True
    )


@router.get("/suggestions", response_model=List[SearchSuggestionItem])
def search_suggestions(
    q: str = Query(..., min_length=2, description="Prefix text for keyword or title suggestion"),
    limit: int = Query(8, ge=1, le=20),
    db: Session = Depends(get_db)
):
    """
    Retrieve instant autocompletion suggestions matching keywords, titles, or authors.
    """
    return SearchService.get_suggestions(db=db, prefix=q, limit=limit)
