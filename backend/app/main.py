import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.session import engine, Base, SessionLocal
from app.search.engine import init_fts_index
from app.services.auth_service import AuthService

# Import all models to ensure registered with Base.metadata
from app.models import (
    KnowledgeDomain,
    License,
    Institution,
    Keyword,
    AdminUser,
    SearchHistory,
    Resource
)

# Route imports
from app.api.routes import (
    health,
    resources,
    search,
    domains,
    licenses,
    institutions,
    statistics,
    auth,
    admin
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def sync_domain_resource_links(db):
    """Ensure all 52 domains and subcategories are linked to their relevant resources."""
    from app.data.domain_profiles import DOMAIN_PROFILES
    from app.models.domain import resource_domains
    from sqlalchemy import insert

    domains_by_slug = {d.slug: d.id for d in db.query(KnowledgeDomain).all()}
    existing_resource_ids = {r.id for r in db.query(Resource.id).all()}
    existing_links = set(db.execute(resource_domains.select()).fetchall())

    added = 0
    for slug, profile in DOMAIN_PROFILES.items():
        dom_id = domains_by_slug.get(slug)
        if not dom_id:
            continue
        for res_id in profile.get("linked_resource_ids", []):
            if res_id in existing_resource_ids and (res_id, dom_id) not in existing_links:
                db.execute(insert(resource_domains).values(resource_id=res_id, domain_id=dom_id))
                existing_links.add((res_id, dom_id))
                added += 1
    if added > 0:
        db.commit()
        logger.info(f"Synchronized {added} domain-resource associations across 52 domains.")


def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        init_fts_index(db)
        AuthService.ensure_default_admin(db)
        sync_domain_resource_links(db)
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Academic digital repository prototype for Indian Knowledge System texts, metadata, categorization, and retrieval.",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include public and administrative API routers
app.include_router(health.router, prefix=settings.API_V1_STR)
app.include_router(resources.router, prefix=settings.API_V1_STR)
app.include_router(search.router, prefix=settings.API_V1_STR)
app.include_router(domains.router, prefix=settings.API_V1_STR)
app.include_router(licenses.router, prefix=settings.API_V1_STR)
app.include_router(institutions.router, prefix=settings.API_V1_STR)
app.include_router(statistics.router, prefix=settings.API_V1_STR)
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(admin.router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    return {
        "repository": settings.PROJECT_FULL_NAME,
        "tagline": settings.TAGLINE,
        "api_documentation": "/docs",
        "health_check": f"{settings.API_V1_STR}/health"
    }
