from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from app.database.session import Base


class Institution(Base):
    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True, index=True)
    institution_name = Column(String(200), nullable=False, unique=True, index=True)
    website_url = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    country = Column(String(100), default="India", nullable=False)
    institution_type = Column(String(100), nullable=True)  # e.g., National Digital Library, University, Museum
    contact_information = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    resources = relationship("Resource", back_populates="institution_ref")

    def __repr__(self):
        return f"<Institution(id={self.id}, name='{self.institution_name}')>"
