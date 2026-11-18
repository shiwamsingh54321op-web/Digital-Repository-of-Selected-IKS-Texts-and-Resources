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


def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        init_fts_index(db)
        AuthService.ensure_default_admin(db)
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
