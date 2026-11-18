import pytest
from app.database.session import SessionLocal
from app.models.resource import Resource
from app.models.domain import KnowledgeDomain
from app.models.license import License
from app.models.institution import Institution
from app.models.user import AdminUser


@pytest.fixture(scope="module")
def db():
    session = SessionLocal()
    yield session
    session.close()


def test_knowledge_domains_seeded(db):
    domains = db.query(KnowledgeDomain).filter(KnowledgeDomain.parent_id.is_(None)).all()
    assert len(domains) >= 12
    domain_names = [d.name for d in domains]
    assert "Indian Mathematics" in domain_names
    assert "Vedic Literature" in domain_names
    assert "Ayurveda and Traditional Medicine" in domain_names


def test_domain_hierarchy(db):
    vedic = db.query(KnowledgeDomain).filter(KnowledgeDomain.slug == "vedic-literature").first()
    assert vedic is not None
    assert len(vedic.subcategories) >= 4
    sub_slugs = [s.slug for s in vedic.subcategories]
    assert "rigveda-traditions" in sub_slugs
    assert "samaveda-traditions" in sub_slugs


def test_licenses_seeded(db):
    licenses = db.query(License).all()
    assert len(licenses) >= 9
    identifiers = [l.identifier for l in licenses]
    assert "public-domain" in identifiers
    assert "cc-by-4.0" in identifiers
    assert "in-copyright-read-only" in identifiers


def test_institutions_seeded(db):
    institutions = db.query(Institution).all()
    assert len(institutions) >= 10
    names = [i.institution_name for i in institutions]
    assert any("IGNCA" in n for n in names)
    assert any("NDLI" in n for n in names)


def test_resources_seeded(db):
    resources = db.query(Resource).all()
    assert len(resources) >= 30
    for r in resources:
        assert r.title
        assert r.creator
        assert r.subject
        assert r.source_url
        assert r.rights_statement
        assert r.verification_status in ("Verified", "Pending", "Rejected")
        assert r.access_status in ("Open Access", "Restricted Access", "Metadata Only", "Pending Verification", "Read Online", "Download Available")


def test_admin_user_seeded(db):
    admin = db.query(AdminUser).filter(AdminUser.username == "admin").first()
    assert admin is not None
    assert admin.role == "administrator"
    assert admin.is_active is True
