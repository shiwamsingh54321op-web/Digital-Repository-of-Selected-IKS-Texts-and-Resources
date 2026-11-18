import csv
import io
import json
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.models.resource import Resource


class ExportService:

    @staticmethod
    def export_resources_csv(db: Session) -> str:
        """
        Export all repository resources as structured Dublin Core-compliant CSV data.
        """
        output = io.StringIO()
        fieldnames = [
            "id",
            "dc_title",
            "subtitle",
            "dc_creator",
            "dc_contributor",
            "dc_subject",
            "knowledge_domain",
            "dc_type",
            "dc_language",
            "translated_language",
            "dc_publisher",
            "dc_date",
            "digitisation_date",
            "dc_source_institution",
            "dc_source_url",
            "access_url",
            "download_url",
            "license_identifier",
            "license_name",
            "dc_rights",
            "access_status",
            "verification_status",
            "dc_format",
            "file_size",
            "dc_identifier",
            "keywords",
            "citation",
            "created_at"
        ]

        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        resources = db.query(Resource).order_by(Resource.id.asc()).all()
        for r in resources:
            writer.writerow({
                "id": r.id,
                "dc_title": r.title,
                "subtitle": r.subtitle or "",
                "dc_creator": r.creator,
                "dc_contributor": r.contributor or "",
                "dc_subject": r.subject,
                "knowledge_domain": r.primary_domain.name if r.primary_domain else "",
                "dc_type": r.resource_type,
                "dc_language": r.language,
                "translated_language": r.translated_language or "",
                "dc_publisher": r.publisher or "",
                "dc_date": r.publication_date or "",
                "digitisation_date": r.digitisation_date or "",
                "dc_source_institution": r.source_institution,
                "dc_source_url": r.source_url,
                "access_url": r.access_url or "",
                "download_url": r.download_url or "",
                "license_identifier": r.license.identifier if r.license else "",
                "license_name": r.license.name if r.license else "",
                "dc_rights": r.rights_statement,
                "access_status": r.access_status,
                "verification_status": r.verification_status,
                "dc_format": r.file_format or "",
                "file_size": r.file_size or "",
                "dc_identifier": r.isbn_or_identifier or "",
                "keywords": r.keywords or "",
                "citation": r.citation or "",
                "created_at": r.created_at.isoformat() if r.created_at else ""
            })

        return output.getvalue()

    @staticmethod
    def export_resources_json(db: Session) -> List[Dict[str, Any]]:
        """
        Export all repository resources as academic Dublin Core JSON records.
        """
        resources = db.query(Resource).order_by(Resource.id.asc()).all()
        data = []
        for r in resources:
            data.append({
                "id": r.id,
                "title": r.title,
                "subtitle": r.subtitle,
                "description": r.description,
                "abstract": r.abstract,
                "creator": r.creator,
                "contributor": r.contributor,
                "subject": r.subject,
                "knowledge_domain": {
                    "id": r.primary_domain.id if r.primary_domain else None,
                    "name": r.primary_domain.name if r.primary_domain else None,
                    "slug": r.primary_domain.slug if r.primary_domain else None,
                },
                "secondary_domains": [
                    {"id": d.id, "name": d.name, "slug": d.slug}
                    for d in r.domains if r.primary_domain and d.id != r.primary_domain.id
                ],
                "resource_type": r.resource_type,
                "language": r.language,
                "translated_language": r.translated_language,
                "publisher": r.publisher,
                "publication_date": r.publication_date,
                "digitisation_date": r.digitisation_date,
                "source_institution": r.source_institution,
                "institution_id": r.institution_id,
                "source_url": r.source_url,
                "access_url": r.access_url,
                "download_url": r.download_url,
                "license": {
                    "id": r.license.id if r.license else None,
                    "name": r.license.name if r.license else None,
                    "identifier": r.license.identifier if r.license else None,
                    "commercial_use_allowed": r.license.commercial_use_allowed if r.license else False,
                    "redistribution_allowed": r.license.redistribution_allowed if r.license else False,
                },
                "rights_statement": r.rights_statement,
                "access_status": r.access_status,
                "verification_status": r.verification_status,
                "file_format": r.file_format,
                "file_size": r.file_size,
                "isbn_or_identifier": r.isbn_or_identifier,
                "keywords": [k.strip() for k in (r.keywords or "").split(",") if k.strip()],
                "citation": r.citation,
                "dublin_core": {
                    "title": r.title,
                    "creator": r.creator,
                    "subject": r.subject,
                    "description": r.description,
                    "publisher": r.publisher or r.source_institution,
                    "contributor": r.contributor,
                    "date": r.publication_date,
                    "type": r.resource_type,
                    "format": r.file_format,
                    "identifier": r.isbn_or_identifier,
                    "source": r.source_url,
                    "language": r.language,
                    "rights": r.rights_statement
                },
                "created_at": r.created_at.isoformat() if r.created_at else None,
                "updated_at": r.updated_at.isoformat() if r.updated_at else None
            })
        return data
