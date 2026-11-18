from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.database.session import Base
from app.models.domain import resource_domains
from app.models.keyword import resource_keywords


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)

    # Core Descriptive Metadata (Dublin Core alignment)
    title = Column(String(300), nullable=False, index=True)
    subtitle = Column(String(300), nullable=True)
    description = Column(Text, nullable=False)
    abstract = Column(Text, nullable=True)
    creator = Column(String(250), nullable=False, index=True)  # Author, scholar, or institution
    contributor = Column(String(250), nullable=True)
    subject = Column(String(250), nullable=False, index=True)
    language = Column(String(100), nullable=False, default="Sanskrit", index=True)
    translated_language = Column(String(100), nullable=True)

    # Classification
    resource_type = Column(String(80), nullable=False, index=True)  # Book, Manuscript, Research Paper, etc.
    knowledge_domain_id = Column(Integer, ForeignKey("knowledge_domains.id", ondelete="RESTRICT"), nullable=False, index=True)

    # Provenance and Publishing
    publisher = Column(String(250), nullable=True)
    publication_date = Column(String(100), nullable=True)  # e.g., "circa 5th century CE", "1915"
    digitisation_date = Column(String(100), nullable=True)
    source_institution = Column(String(250), nullable=False, index=True)
    institution_id = Column(Integer, ForeignKey("institutions.id", ondelete="SET NULL"), nullable=True, index=True)

    # Retrieval and Access Links
    source_url = Column(String(1000), nullable=False)
    access_url = Column(String(1000), nullable=True)
    download_url = Column(String(1000), nullable=True)

    # Rights, Licensing and Legal Status
    license_id = Column(Integer, ForeignKey("licenses.id", ondelete="RESTRICT"), nullable=False, index=True)
    rights_statement = Column(Text, nullable=False)
    access_status = Column(String(80), nullable=False, default="Open Access", index=True)
    # Options: "Open Access", "Restricted Access", "Metadata Only", "Pending Verification", "Read Online"

    # Technical Specifications
    file_format = Column(String(50), nullable=True, default="PDF")
    file_size = Column(String(50), nullable=True)
    thumbnail_url = Column(String(1000), nullable=True)
    isbn_or_identifier = Column(String(150), nullable=True, index=True)  # DOI, ISBN, accession number

    # Keywords and Scholarly Citation
    keywords = Column(Text, nullable=True)  # Comma-separated or JSON string for fast indexing
    citation = Column(Text, nullable=True)  # Scholarly suggested citation

    # Verification & Audit
    verification_status = Column(String(50), nullable=False, default="Verified", index=True)
    # Options: "Verified", "Pending", "Rejected"
    verified_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    primary_domain = relationship("KnowledgeDomain", foreign_keys=[knowledge_domain_id])
    domains = relationship("KnowledgeDomain", secondary=resource_domains, back_populates="resources")
    license = relationship("License", back_populates="resources")
    institution_ref = relationship("Institution", back_populates="resources")
    keyword_items = relationship("Keyword", secondary=resource_keywords, back_populates="resources")

    # Composite indexes for high-frequency filtering combinations
    __table_args__ = (
        Index("idx_resource_domain_status", "knowledge_domain_id", "access_status", "verification_status"),
        Index("idx_resource_type_lang", "resource_type", "language"),
    )

    def __repr__(self):
        return f"<Resource(id={self.id}, title='{self.title[:30]}...', creator='{self.creator}')>"
