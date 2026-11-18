from app.schemas.domain import (
    KnowledgeDomainBase,
    KnowledgeDomainCreate,
    KnowledgeDomainUpdate,
    KnowledgeDomainResponse,
    KnowledgeDomainHierarchy,
)
from app.schemas.license import (
    LicenseBase,
    LicenseCreate,
    LicenseUpdate,
    LicenseResponse,
)
from app.schemas.institution import (
    InstitutionBase,
    InstitutionCreate,
    InstitutionUpdate,
    InstitutionResponse,
)
from app.schemas.keyword import (
    KeywordBase,
    KeywordCreate,
    KeywordResponse,
)
from app.schemas.user import (
    AdminUserBase,
    AdminUserCreate,
    AdminUserResponse,
    LoginRequest,
    Token,
)
from app.schemas.resource import (
    DublinCoreMetadata,
    ResourceBase,
    ResourceCreate,
    ResourceUpdate,
    VerificationUpdate,
    ResourceResponse,
    ResourceDetailResponse,
    PaginatedResources,
)
from app.schemas.search import (
    SearchQuery,
    SearchResultItem,
    SearchResponse,
    SearchSuggestionItem,
)

__all__ = [
    "KnowledgeDomainBase",
    "KnowledgeDomainCreate",
    "KnowledgeDomainUpdate",
    "KnowledgeDomainResponse",
    "KnowledgeDomainHierarchy",
    "LicenseBase",
    "LicenseCreate",
    "LicenseUpdate",
    "LicenseResponse",
    "InstitutionBase",
    "InstitutionCreate",
    "InstitutionUpdate",
    "InstitutionResponse",
    "KeywordBase",
    "KeywordCreate",
    "KeywordResponse",
    "AdminUserBase",
    "AdminUserCreate",
    "AdminUserResponse",
    "LoginRequest",
    "Token",
    "DublinCoreMetadata",
    "ResourceBase",
    "ResourceCreate",
    "ResourceUpdate",
    "VerificationUpdate",
    "ResourceResponse",
    "ResourceDetailResponse",
    "PaginatedResources",
    "SearchQuery",
    "SearchResultItem",
    "SearchResponse",
    "SearchSuggestionItem",
]
