from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.license import License
from app.models.resource import Resource
from app.schemas.license import LicenseCreate, LicenseUpdate


class LicenseRepository:

    @staticmethod
    def get_by_id(db: Session, license_id: int) -> Optional[License]:
        return db.query(License).filter(License.id == license_id).first()

    @staticmethod
    def get_by_identifier(db: Session, identifier: str) -> Optional[License]:
        return db.query(License).filter(License.identifier == identifier).first()

    @staticmethod
    def get_all(db: Session) -> List[License]:
        return db.query(License).order_by(License.name.asc()).all()

    @staticmethod
    def get_resource_counts(db: Session) -> dict:
        rows = (
            db.query(
                Resource.license_id,
                func.count(Resource.id).label("count")
            )
            .group_by(Resource.license_id)
            .all()
        )
        return {r[0]: r[1] for r in rows}

    @staticmethod
    def create(db: Session, schema: LicenseCreate) -> License:
        lic = License(**schema.model_dump())
        db.add(lic)
        db.commit()
        db.refresh(lic)
        return lic

    @staticmethod
    def update(db: Session, lic: License, schema: LicenseUpdate) -> License:
        for field, value in schema.model_dump(exclude_unset=True).items():
            setattr(lic, field, value)
        db.commit()
        db.refresh(lic)
        return lic
