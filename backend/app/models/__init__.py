from app.models.domain import KnowledgeDomain, resource_domains
from app.models.license import License
from app.models.institution import Institution
from app.models.keyword import Keyword, resource_keywords
from app.models.user import AdminUser
from app.models.search_history import SearchHistory
from app.models.resource import Resource

__all__ = [
    "KnowledgeDomain",
    "resource_domains",
    "License",
    "Institution",
    "Keyword",
    "resource_keywords",
    "AdminUser",
    "SearchHistory",
    "Resource",
]
