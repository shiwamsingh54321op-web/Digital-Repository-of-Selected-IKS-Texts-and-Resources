from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl, ConfigDict, field_validator
from app.schemas.domain import KnowledgeDomainResponse
from app.schemas.license import LicenseResponse
from app.schemas.institution import InstitutionResponse


class DublinCoreMetadata(BaseModel):
    """
    Standard Dublin Core (15 Elements) Representation for scholarly preservation.
    """
    title: str = Field(..., description="DC.Title: Name given to the resource")
    creator: str = Field(..., description="DC.Creator: Primary entity responsible for making the resource")
    subject: str = Field(..., description="DC.Subject: Topic or scholarly domain of the resource")
    description: str = Field(..., description="DC.Description: Academic account or summary of content")
    publisher: Optional[str] = Field(None, description="DC.Publisher: Entity responsible for making resource available")
    contributor: Optional[str] = Field(None, description="DC.Contributor: Additional contributing scholars or institutions")
    date: Optional[str] = Field(None, description="DC.Date: Point or period associated with creation/publication")
    type: str = Field(..., description="DC.Type: Nature or genre of content (Book, Manuscript, etc.)")
    format: Optional[str] = Field(None, description="DC.Format: File format or physical manifestation")
    identifier: Optional[str] = Field(None, description="DC.Identifier: Unambiguous reference (DOI, ISBN, Shelf-mark)")
    source: str = Field(..., description="DC.Source: Reference to source from which present resource is derived")
    language: str = Field(..., description="DC.Language: Language of the resource")
    relation: Optional[str] = Field(None, description="DC.Relation: Related scholarly work, commentary, or recension")
    coverage: Optional[str] = Field(None, description="DC.Coverage: Spatial/temporal characteristics")
    rights: str = Field(..., description="DC.Rights: Information about rights held in and over the resource")


class ResourceBase(BaseModel):
    title: str = Field(..., max_length=300, description="Primary title of the text/resource")
    subtitle: Optional[str] = Field(None, max_length=300, description="Optional subtitle or alternate name")
    description: str = Field(..., description="Exhaustive academic description")
    abstract: Optional[str] = Field(None, description="Concise scholarly abstract")
    creator: str = Field(..., max_length=250, description="Author, sage, commentator, or compiling scholar")
    contributor: Optional[str] = Field(None, max_length=250, description="Editor, translator, or secondary contributor")
    subject: str = Field(..., max_length=250, description="Subject area or canonical branch")
    language: str = Field("Sanskrit", max_length=100, description="Original primary language")
    translated_language: Optional[str] = Field(None, max_length=100, description="Target language of translation")

    resource_type: str = Field(..., max_length=80, description="Book, Manuscript, Research Paper, Article, Audio, Video, Image, Other")
    knowledge_domain_id: int = Field(..., description="Primary knowledge domain foreign key")
    additional_domain_ids: Optional[List[int]] = Field(default_factory=list, description="Optional secondary domain IDs")

    publisher: Optional[str] = Field(None, max_length=250, description="Publisher or digitizing entity")
    publication_date: Optional[str] = Field(None, max_length=100, description="Historical date or print publication year")
    digitisation_date: Optional[str] = Field(None, max_length=100, description="Year/date of digital archival capture")
    source_institution: str = Field(..., max_length=250, description="Name of holding institution/archive")
    institution_id: Optional[int] = Field(None, description="Foreign key to registered institutions")

    source_url: str = Field(..., max_length=1000, description="Authoritative external page URL")
    access_url: Optional[str] = Field(None, max_length=1000, description="Direct reading/viewer link")
    download_url: Optional[str] = Field(None, max_length=1000, description="Direct file download link, if verified")

    license_id: int = Field(..., description="Foreign key to verified license")
    rights_statement: str = Field(..., description="Human-readable copyright or open access statement")
    access_status: str = Field(
        "Open Access",
        max_length=80,
        description="Open Access, Restricted Access, Metadata Only, Pending Verification, or Read Online"
    )

    file_format: Optional[str] = Field("PDF", max_length=50, description="PDF, EPUB, HTML, Audio, Image")
    file_size: Optional[str] = Field(None, max_length=50, description="Human readable size e.g. '14.2 MB'")
    thumbnail_url: Optional[str] = Field(None, max_length=1000, description="Cover image or manuscript leaf thumbnail")
    isbn_or_identifier: Optional[str] = Field(None, max_length=150, description="DOI, ISBN, or manuscript catalog number")

    keywords: Optional[str] = Field(None, description="Comma-separated keywords")
    citation: Optional[str] = Field(None, description="Suggested scholarly bibliographic citation")
    verification_status: str = Field("Verified", max_length=50, description="Verified, Pending, or Rejected")


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=300)
    subtitle: Optional[str] = Field(None, max_length=300)
    description: Optional[str] = None
    abstract: Optional[str] = None
    creator: Optional[str] = Field(None, max_length=250)
    contributor: Optional[str] = Field(None, max_length=250)
    subject: Optional[str] = Field(None, max_length=250)
    language: Optional[str] = Field(None, max_length=100)
    translated_language: Optional[str] = Field(None, max_length=100)
    resource_type: Optional[str] = Field(None, max_length=80)
    knowledge_domain_id: Optional[int] = None
    additional_domain_ids: Optional[List[int]] = None
    publisher: Optional[str] = Field(None, max_length=250)
    publication_date: Optional[str] = Field(None, max_length=100)
    digitisation_date: Optional[str] = Field(None, max_length=100)
    source_institution: Optional[str] = Field(None, max_length=250)
    institution_id: Optional[int] = None
    source_url: Optional[str] = Field(None, max_length=1000)
    access_url: Optional[str] = Field(None, max_length=1000)
    download_url: Optional[str] = Field(None, max_length=1000)
    license_id: Optional[int] = None
    rights_statement: Optional[str] = None
    access_status: Optional[str] = Field(None, max_length=80)
    file_format: Optional[str] = Field(None, max_length=50)
    file_size: Optional[str] = Field(None, max_length=50)
    thumbnail_url: Optional[str] = Field(None, max_length=1000)
    isbn_or_identifier: Optional[str] = Field(None, max_length=150)
    keywords: Optional[str] = None
    citation: Optional[str] = None
    verification_status: Optional[str] = Field(None, max_length=50)


class VerificationUpdate(BaseModel):
    verification_status: str = Field(..., max_length=50, description="Verified, Pending, or Rejected")
    rights_statement: Optional[str] = None
    verification_notes: Optional[str] = None


class ResourceResponse(ResourceBase):
    id: int
    created_at: datetime
    updated_at: datetime
    verified_at: Optional[datetime] = None

    primary_domain: Optional[KnowledgeDomainResponse] = None
    license: Optional[LicenseResponse] = None
    institution_ref: Optional[InstitutionResponse] = None

    model_config = ConfigDict(from_attributes=True)


class ResourceDetailResponse(ResourceResponse):
    domains: List[KnowledgeDomainResponse] = []
    dublin_core: Optional[DublinCoreMetadata] = None
    can_download: bool = False
    related_resources: List[ResourceResponse] = []

    model_config = ConfigDict(from_attributes=True)


class PaginatedResources(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_prev: bool
    items: List[ResourceResponse]
