import json
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session
from app.search.engine import SearchEngine
from app.models.search_history import SearchHistory


class SearchService:

    @staticmethod
    def execute_search(
        db: Session,
        query: Optional[str] = None,
        domain_id: Optional[int] = None,
        domain_slug: Optional[str] = None,
        resource_type: Optional[str] = None,
        language: Optional[str] = None,
        access_status: Optional[str] = None,
        license_id: Optional[int] = None,
        institution_id: Optional[int] = None,
        verification_status: Optional[str] = "Verified",
        sort_by: str = "relevance",
        page: int = 1,
        page_size: int = 12,
        log_history: bool = True
    ) -> Dict[str, Any]:
        """
        Execute FTS5 search with BM25 ranking and optionally log anonymized query analytics.
        """
        results = SearchEngine.search(
            db=db,
            query_str=query,
            domain_id=domain_id,
            domain_slug=domain_slug,
            resource_type=resource_type,
            language=language,
            access_status=access_status,
            license_id=license_id,
            institution_id=institution_id,
            verification_status=verification_status,
            sort_by=sort_by,
            page=page,
            page_size=page_size
        )

        if log_history and query and query.strip():
            try:
                filters = {
                    "domain_id": domain_id,
                    "domain_slug": domain_slug,
                    "resource_type": resource_type,
                    "language": language,
                    "access_status": access_status,
                    "sort_by": sort_by
                }
                cleaned_filters = {k: v for k, v in filters.items() if v is not None}
                history_record = SearchHistory(
                    query=query.strip()[:300],
                    filters_used=json.dumps(cleaned_filters) if cleaned_filters else None,
                    result_count=results["total"]
                )
                db.add(history_record)
                db.commit()
            except Exception:
                db.rollback()

        return results

    @staticmethod
    def get_suggestions(db: Session, prefix: str, limit: int = 8) -> List[Dict[str, str]]:
        return SearchEngine.get_suggestions(db, prefix=prefix, limit=limit)
