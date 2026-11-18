from datetime import datetime
from typing import List, Optional
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database.session import Base

# Association table for Resource <-> KnowledgeDomain (Many-to-Many)
resource_domains = Table(
    "resource_domains",
    Base.metadata,
    Column("resource_id", Integer, ForeignKey("resources.id", ondelete="CASCADE"), primary_key=True),
    Column("domain_id", Integer, ForeignKey("knowledge_domains.id", ondelete="CASCADE"), primary_key=True),
)


class KnowledgeDomain(Base):
    __tablename__ = "knowledge_domains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, unique=True, index=True)
    slug = Column(String(150), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True)
    parent_id = Column(Integer, ForeignKey("knowledge_domains.id", ondelete="SET NULL"), nullable=True, index=True)
    icon = Column(String(60), nullable=True, default="BookOpen")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Hierarchical relationship
    parent = relationship("KnowledgeDomain", remote_side=[id], backref="subcategories")

    # Associated resources
    resources = relationship("Resource", secondary=resource_domains, back_populates="domains")

    def __repr__(self):
        return f"<KnowledgeDomain(id={self.id}, name='{self.name}', slug='{self.slug}')>"
