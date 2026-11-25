from typing import List, Optional, Tuple, Dict, Any
from datetime import datetime
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, or_, desc, asc
from app.models.resource import Resource
from app.models.domain import KnowledgeDomain
from app.models.keyword import Keyword
from app.schemas.resource import ResourceCreate, ResourceUpdate


class ResourceRepository:

    @staticmethod
    def get_by_id(db: Session, resource_id: int) -> Optional[Resource]:
        return (
            db.query(Resource)
            .options(
                joinedload(Resource.primary_domain),
                joinedload(Resource.license),
                joinedload(Resource.institution_ref),
                joinedload(Resource.domains),
                joinedload(Resource.keyword_items)
            )
            .filter(Resource.id == resource_id)
            .first()
        )

    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 20,
        domain_id: Optional[int] = None,
        domain_slug: Optional[str] = None,
        resource_type: Optional[str] = None,
        language: Optional[str] = None,
        access_status: Optional[str] = None,
        license_id: Optional[int] = None,
        institution_id: Optional[int] = None,
        verification_status: Optional[str] = "Verified",
        sort_by: str = "newest"
    ) -> Tuple[List[Resource], int]:
        query = db.query(Resource).options(
            joinedload(Resource.primary_domain),
            joinedload(Resource.license),
            joinedload(Resource.institution_ref)
        )

        if verification_status:
            query = query.filter(Resource.verification_status == verification_status)

        if domain_id is not None or domain_slug:
            target_domain = (
                db.query(KnowledgeDomain).filter(KnowledgeDomain.id == domain_id).first()
                if domain_id is not None
                else db.query(KnowledgeDomain).filter(KnowledgeDomain.slug == domain_slug).first()
            )
            if target_domain:
                sub_ids = [s.id for s in db.query(KnowledgeDomain.id).filter(KnowledgeDomain.parent_id == target_domain.id).all()]
                match_ids = [target_domain.id] + sub_ids
                query = query.filter(
                    or_(
                        Resource.knowledge_domain_id.in_(match_ids),
                        Resource.domains.any(KnowledgeDomain.id.in_(match_ids))
                    )
                )
            elif domain_id is not None:
                query = query.filter(Resource.knowledge_domain_id == domain_id)
            else:
                query = query.filter(Resource.id == -1)

        if resource_type:
            query = query.filter(Resource.resource_type == resource_type)

        if language:
            query = query.filter(Resource.language == language)

        if access_status:
            query = query.filter(Resource.access_status == access_status)

        if license_id is not None:
            query = query.filter(Resource.license_id == license_id)

        if institution_id is not None:
            query = query.filter(Resource.institution_id == institution_id)

        total = query.count()

        if sort_by == "title_asc":
            query = query.order_by(asc(Resource.title))
        elif sort_by == "title_desc":
            query = query.order_by(desc(Resource.title))
        elif sort_by == "oldest":
            query = query.order_by(asc(Resource.created_at))
        else:  # newest
            query = query.order_by(desc(Resource.created_at))

        items = query.offset(skip).limit(limit).all()
        return items, total

    @staticmethod
    def create(db: Session, schema: ResourceCreate) -> Resource:
        data = schema.model_dump(exclude={"additional_domain_ids"})
        additional_domain_ids = schema.additional_domain_ids or []

        resource = Resource(**data)

        # Primary domain is set via knowledge_domain_id.
        # Also associate any secondary domains.
        domains = []
        primary_domain = db.query(KnowledgeDomain).filter(KnowledgeDomain.id == schema.knowledge_domain_id).first()
        if primary_domain:
            domains.append(primary_domain)

        for did in additional_domain_ids:
            if did != schema.knowledge_domain_id:
                sec_dom = db.query(KnowledgeDomain).filter(KnowledgeDomain.id == did).first()
                if sec_dom and sec_dom not in domains:
                    domains.append(sec_dom)
        resource.domains = domains

        # Handle keywords
        if schema.keywords:
            kw_list = [k.strip() for k in schema.keywords.split(",") if k.strip()]
            for kw_name in kw_list:
                slug = kw_name.lower().replace(" ", "-")
                kw_obj = db.query(Keyword).filter(Keyword.slug == slug).first()
                if not kw_obj:
                    kw_obj = Keyword(keyword=kw_name, slug=slug)
                    db.add(kw_obj)
                resource.keyword_items.append(kw_obj)

        if schema.verification_status == "Verified":
            resource.verified_at = datetime.utcnow()

        db.add(resource)
        db.commit()
        db.refresh(resource)
        return resource

    @staticmethod
    def update(db: Session, resource: Resource, schema: ResourceUpdate) -> Resource:
        update_data = schema.model_dump(exclude_unset=True, exclude={"additional_domain_ids"})
        for field, value in update_data.items():
            setattr(resource, field, value)

        if schema.additional_domain_ids is not None:
            domains = []
            target_domain_id = schema.knowledge_domain_id or resource.knowledge_domain_id
            primary_domain = db.query(KnowledgeDomain).filter(KnowledgeDomain.id == target_domain_id).first()
            if primary_domain:
                domains.append(primary_domain)
            for did in schema.additional_domain_ids:
                if did != target_domain_id:
                    sec_dom = db.query(KnowledgeDomain).filter(KnowledgeDomain.id == did).first()
                    if sec_dom and sec_dom not in domains:
                        domains.append(sec_dom)
            resource.domains = domains

        if schema.keywords is not None:
            resource.keyword_items = []
            kw_list = [k.strip() for k in schema.keywords.split(",") if k.strip()]
            for kw_name in kw_list:
                slug = kw_name.lower().replace(" ", "-")
                kw_obj = db.query(Keyword).filter(Keyword.slug == slug).first()
                if not kw_obj:
                    kw_obj = Keyword(keyword=kw_name, slug=slug)
                    db.add(kw_obj)
                resource.keyword_items.append(kw_obj)

        if schema.verification_status == "Verified" and not resource.verified_at:
            resource.verified_at = datetime.utcnow()

        resource.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(resource)
        return resource

    @staticmethod
    def delete(db: Session, resource: Resource) -> None:
        db.delete(resource)
        db.commit()

    @staticmethod
    def get_related(db: Session, resource: Resource, limit: int = 4) -> List[Resource]:
        """Fetch related resources matching same domain or subject, excluding self."""
        return (
            db.query(Resource)
            .filter(
                Resource.id != resource.id,
                Resource.verification_status == "Verified",
                or_(
                    Resource.knowledge_domain_id == resource.knowledge_domain_id,
                    Resource.subject == resource.subject
                )
            )
            .limit(limit)
            .all()
        )
