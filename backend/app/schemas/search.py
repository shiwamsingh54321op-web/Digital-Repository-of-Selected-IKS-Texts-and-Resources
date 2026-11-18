from typing import Optional, List, Any, Dict
from pydantic import BaseModel, Field
from app.schemas.resource import ResourceResponse


class SearchQuery(BaseModel):
    q: Optional[str] = Field(None, description="Keywords, natural language phrases, or creator names")
    domain_id: Optional[int] = Field(None, description="Knowledge domain ID")
    domain_slug: Optional[str] = Field(None, description="Knowledge domain slug")
    resource_type: Optional[str] = Field(None, description="Resource type filter")
    language: Optional[str] = Field(None, description="Language filter")
    access_status: Optional[str] = Field(None, description="Access status filter")
    license_id: Optional[int] = Field(None, description="License ID filter")
    institution_id: Optional[int] = Field(None, description="Source institution ID filter")
    sort_by: str = Field("relevance", description="relevance, title_asc, title_desc, newest, oldest")
    page: int = Field(1, ge=1)
    page_size: int = Field(12, ge=1, le=100)


class SearchResultItem(BaseModel):
    id: int
    title: str
    subtitle: Optional[str] = None
    description: str
    abstract: Optional[str] = None
    creator: str
    subject: str
    language: str
    resource_type: str
    knowledge_domain_id: int
    domain_name: str
    domain_slug: str
    source_institution: str
    institution_id: Optional[int] = None
    institution_name_ref: Optional[str] = None
    license_id: int
    license_name: str
    license_identifier: str
    license_redistribution_allowed: bool = False
    rights_statement: str
    access_status: str
    file_format: Optional[str] = None
    thumbnail_url: Optional[str] = None
    source_url: str
    access_url: Optional[str] = None
    download_url: Optional[str] = None
    citation: Optional[str] = None
    bm25_rank: Optional[float] = 0.0
    search_snippet: Optional[str] = None


class SearchResponse(BaseModel):
    query: str
    sanitized_query: str
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool
    results: List[SearchResultItem]


class SearchSuggestionItem(BaseModel):
    text: str
    type: str  # 'keyword', 'title', 'creator'
