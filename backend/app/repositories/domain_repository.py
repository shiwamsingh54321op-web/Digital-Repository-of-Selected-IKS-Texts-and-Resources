from typing import List, Optional, Tuple
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from app.models.domain import KnowledgeDomain
from app.models.resource import Resource
from app.schemas.domain import KnowledgeDomainCreate, KnowledgeDomainUpdate


class DomainRepository:

    @staticmethod
    def get_by_id(db: Session, domain_id: int) -> Optional[KnowledgeDomain]:
        return db.query(KnowledgeDomain).filter(KnowledgeDomain.id == domain_id).first()

    @staticmethod
    def get_by_slug(db: Session, slug: str) -> Optional[KnowledgeDomain]:
        return db.query(KnowledgeDomain).filter(KnowledgeDomain.slug == slug).first()

    @staticmethod
    def get_all(db: Session, parent_only: bool = False) -> List[KnowledgeDomain]:
        query = db.query(KnowledgeDomain)
        if parent_only:
            query = query.filter(KnowledgeDomain.parent_id.is_(None))
        return query.order_by(KnowledgeDomain.name.asc()).all()

    @staticmethod
    def get_hierarchy(db: Session) -> List[KnowledgeDomain]:
        """Fetch all top-level domains with their subcategories preloaded."""
        return (
            db.query(KnowledgeDomain)
            .filter(KnowledgeDomain.parent_id.is_(None))
            .options(joinedload(KnowledgeDomain.subcategories))
            .order_by(KnowledgeDomain.name.asc())
            .all()
        )

    @staticmethod
    def get_resource_counts(db: Session) -> dict:
        """Calculate verified resource counts per domain (primary + secondary associations)."""
        from app.models.domain import resource_domains
        from sqlalchemy import union_all, select

        primary_q = (
            select(
                Resource.knowledge_domain_id.label("domain_id"),
                Resource.id.label("resource_id")
            )
            .where(Resource.verification_status == "Verified")
        )
        secondary_q = (
            select(
                resource_domains.c.domain_id.label("domain_id"),
                resource_domains.c.resource_id.label("resource_id")
            )
            .select_from(
                resource_domains.join(Resource, resource_domains.c.resource_id == Resource.id)
            )
            .where(Resource.verification_status == "Verified")
        )
        combined = union_all(primary_q, secondary_q).subquery()
        rows = (
            db.query(
                combined.c.domain_id,
                func.count(func.distinct(combined.c.resource_id)).label("count")
            )
            .group_by(combined.c.domain_id)
            .all()
        )
        return {r[0]: r[1] for r in rows}

    @staticmethod
    def create(db: Session, schema: KnowledgeDomainCreate) -> KnowledgeDomain:
        domain = KnowledgeDomain(**schema.model_dump())
        db.add(domain)
        db.commit()
        db.refresh(domain)
        return domain

    @staticmethod
    def update(db: Session, domain: KnowledgeDomain, schema: KnowledgeDomainUpdate) -> KnowledgeDomain:
        for field, value in schema.model_dump(exclude_unset=True).items():
            setattr(domain, field, value)
        db.commit()
        db.refresh(domain)
        return domain

    @staticmethod
    def delete(db: Session, domain: KnowledgeDomain) -> None:
        db.delete(domain)
        db.commit()
