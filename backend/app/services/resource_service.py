from typing import Dict, Any, List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.resource import Resource
from app.repositories.resource_repository import ResourceRepository
from app.schemas.resource import (
    DublinCoreMetadata,
    ResourceDetailResponse,
    ResourceResponse,
    ResourceCreate,
    ResourceUpdate,
)


class ResourceService:

    @staticmethod
    def build_dublin_core(resource: Resource) -> DublinCoreMetadata:
        """
        Maps a Resource entity into an academic Dublin Core (15 Elements) structure.
        """
        return DublinCoreMetadata(
            title=resource.title,
            creator=resource.creator,
            subject=resource.subject,
            description=resource.description,
            publisher=resource.publisher or resource.source_institution,
            contributor=resource.contributor,
            date=resource.publication_date,
            type=resource.resource_type,
            format=resource.file_format or "Digital Document",
            identifier=resource.isbn_or_identifier or f"IKS-RES-{resource.id}",
            source=resource.source_url,
            language=resource.language,
            relation=f"Knowledge Domain: {resource.primary_domain.name if resource.primary_domain else 'IKS'}",
            coverage="Ancient / Classical India",
            rights=resource.rights_statement
        )

    @staticmethod
    def generate_citations(resource: Resource) -> Dict[str, str]:
        """
        Generate scholarly citations in multiple academic styles.
        """
        year = resource.publication_date or "n.d."
        title = resource.title
        creator = resource.creator
        inst = resource.source_institution
        url = resource.source_url

        apa = f"{creator}. ({year}). {title}. {inst}. {url}"
        mla = f'{creator}. "{title}." {inst}, {year}, {url}.'
        chicago = f'{creator}. {title}. {inst}, {year}. {url}.'
        bibtex = f"""@misc{{iks_{resource.id},
  author = {{{creator}}},
  title = {{{title}}},
  year = {{{year}}},
  publisher = {{{inst}}},
  url = {{{url}}},
  note = {{Accessed via IKS Digital Repository}}
}}"""

        return {
            "apa": apa,
            "mla": mla,
            "chicago": chicago,
            "bibtex": bibtex.strip()
        }

    @classmethod
    def can_download_resource(cls, resource: Resource) -> bool:
        if resource.verification_status != "Verified":
            return False
        if resource.access_status in ("Restricted Access", "Metadata Only", "Pending Verification"):
            return False
        if resource.license and resource.license.redistribution_allowed:
            return True
        if resource.access_status == "Download Available":
            return True
        return False

    @classmethod
    def get_resource_details(cls, db: Session, resource_id: int) -> ResourceDetailResponse:
        resource = ResourceRepository.get_by_id(db, resource_id)
        if not resource:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Resource with ID {resource_id} not found"
            )

        dc = cls.build_dublin_core(resource)
        can_download = cls.can_download_resource(resource)
        related = ResourceRepository.get_related(db, resource, limit=4)

        return ResourceDetailResponse(
            id=resource.id,
            title=resource.title,
            subtitle=resource.subtitle,
            description=resource.description,
            abstract=resource.abstract,
            creator=resource.creator,
            contributor=resource.contributor,
            subject=resource.subject,
            language=resource.language,
            translated_language=resource.translated_language,
            resource_type=resource.resource_type,
            knowledge_domain_id=resource.knowledge_domain_id,
            publisher=resource.publisher,
            publication_date=resource.publication_date,
            digitisation_date=resource.digitisation_date,
            source_institution=resource.source_institution,
            institution_id=resource.institution_id,
            source_url=resource.source_url,
            access_url=resource.access_url,
            download_url=resource.download_url,
            license_id=resource.license_id,
            rights_statement=resource.rights_statement,
            access_status=resource.access_status,
            file_format=resource.file_format,
            file_size=resource.file_size,
            thumbnail_url=resource.thumbnail_url,
            isbn_or_identifier=resource.isbn_or_identifier,
            keywords=resource.keywords,
            citation=resource.citation or cls.generate_citations(resource)["apa"],
            verification_status=resource.verification_status,
            verified_at=resource.verified_at,
            created_at=resource.created_at,
            updated_at=resource.updated_at,
            primary_domain=resource.primary_domain,
            domains=resource.domains or [resource.primary_domain],
            license=resource.license,
            institution_ref=resource.institution_ref,
            dublin_core=dc,
            can_download=can_download,
            related_resources=related
        )
