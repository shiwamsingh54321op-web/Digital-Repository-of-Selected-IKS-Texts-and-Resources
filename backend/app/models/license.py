from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database.session import Base


class License(Base):
    __tablename__ = "licenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, unique=True, index=True)
    identifier = Column(String(100), nullable=False, unique=True, index=True)
    license_url = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    permissions = Column(Text, nullable=True)
    commercial_use_allowed = Column(Boolean, default=False, nullable=False)
    redistribution_allowed = Column(Boolean, default=False, nullable=False)
    attribution_required = Column(Boolean, default=True, nullable=False)
    verification_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    resources = relationship("Resource", back_populates="license")

    def __repr__(self):
        return f"<License(id={self.id}, identifier='{self.identifier}')>"
