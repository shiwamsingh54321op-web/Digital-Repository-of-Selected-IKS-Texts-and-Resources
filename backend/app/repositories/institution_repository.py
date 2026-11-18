from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.institution import Institution
from app.models.resource import Resource
from app.schemas.institution import InstitutionCreate, InstitutionUpdate


class InstitutionRepository:

    @staticmethod
    def get_by_id(db: Session, inst_id: int) -> Optional[Institution]:
        return db.query(Institution).filter(Institution.id == inst_id).first()

    @staticmethod
    def get_all(db: Session) -> List[Institution]:
        return db.query(Institution).order_by(Institution.institution_name.asc()).all()

    @staticmethod
    def get_resource_counts(db: Session) -> dict:
        rows = (
            db.query(
                Resource.institution_id,
                func.count(Resource.id).label("count")
            )
            .group_by(Resource.institution_id)
            .all()
        )
        return {r[0]: r[1] for r in rows if r[0] is not None}

    @staticmethod
    def create(db: Session, schema: InstitutionCreate) -> Institution:
        inst = Institution(**schema.model_dump())
        db.add(inst)
        db.commit()
        db.refresh(inst)
        return inst

    @staticmethod
    def update(db: Session, inst: Institution, schema: InstitutionUpdate) -> Institution:
        for field, value in schema.model_dump(exclude_unset=True).items():
            setattr(inst, field, value)
        db.commit()
        db.refresh(inst)
        return inst
