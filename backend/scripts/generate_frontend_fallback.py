import sys
import json
from pathlib import Path

# Add backend directory to path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from app.database.session import SessionLocal
from app.repositories.domain_repository import DomainRepository
from app.repositories.resource_repository import ResourceRepository
from app.services.resource_service import ResourceService
from app.models import License, Institution
from app.data.domain_profiles import DOMAIN_PROFILES
from app.data.resource_education import RESOURCE_EDUCATION

db = SessionLocal()

# 1. Domains
hierarchy = DomainRepository.get_hierarchy(db)
counts = DomainRepository.get_resource_counts(db)

domains_list = []
for d in hierarchy:
    subs = []
    for s in getattr(d, 'subcategories', []):
        s_prof = DOMAIN_PROFILES.get(s.slug, {})
        subs.append({
            'id': s.id,
            'name': s.name,
            'slug': s.slug,
            'sanskrit_name': s_prof.get('sanskrit_name') or s.name,
            'description': s.description,
            'parent_id': s.parent_id,
            'icon': s.icon,
            'resource_count': counts.get(s.id, 0),
            'profile': s_prof or None,
        })
    d_prof = DOMAIN_PROFILES.get(d.slug, {})
    domains_list.append({
        'id': d.id,
        'name': d.name,
        'slug': d.slug,
        'sanskrit_name': d_prof.get('sanskrit_name') or d.name,
        'description': d.description,
        'parent_id': d.parent_id,
        'icon': d.icon,
        'resource_count': counts.get(d.id, 0),
        'profile': d_prof or None,
        'subcategories': subs,
    })

# 2. Licenses
licenses = db.query(License).all()
licenses_list = [
    {
        'id': l.id,
        'name': l.name,
        'identifier': l.identifier,
        'description': l.description,
        'commercial_use_allowed': l.commercial_use_allowed,
        'redistribution_allowed': l.redistribution_allowed,
        'attribution_required': l.attribution_required,
        'license_url': l.license_url,
    }
    for l in licenses
]

# 3. Institutions
institutions = db.query(Institution).all()
institutions_list = [
    {
        'id': i.id,
        'name': i.institution_name,
        'institution_name': i.institution_name,
        'slug': i.institution_name.lower().replace(' ', '-'),
        'location': i.country,
        'website': i.website_url,
        'description': i.description,
        'resource_count': len(i.resources) if hasattr(i, 'resources') else 0,
    }
    for i in institutions
]

# 4. Resources
resources, total = ResourceRepository.get_all(db, skip=0, limit=100)
resources_list = []
for r in resources:
    dc = ResourceService.build_dublin_core(r)
    citations = ResourceService.generate_citations(r)
    can_download = ResourceService.can_download_resource(r)
    reason = None if can_download else f"Direct download restricted under '{r.access_status}'."
    
    primary_dom = {
        'id': r.primary_domain.id,
        'name': r.primary_domain.name,
        'slug': r.primary_domain.slug,
    } if r.primary_domain else None

    lic = {
        'id': r.license.id,
        'name': r.license.name,
        'identifier': r.license.identifier,
        'commercial_use_allowed': r.license.commercial_use_allowed,
        'redistribution_allowed': r.license.redistribution_allowed,
        'attribution_required': r.license.attribution_required,
    } if r.license else None

    inst = {
        'id': r.institution_ref.id,
        'institution_name': r.institution_ref.institution_name,
        'slug': r.institution_ref.institution_name.lower().replace(' ', '-'),
        'location': r.institution_ref.country,
        'website': r.institution_ref.website_url,
        'description': r.institution_ref.description,
    } if r.institution_ref else None

    resources_list.append({
        'id': r.id,
        'title': r.title,
        'subtitle': r.subtitle,
        'description': r.description,
        'abstract': r.abstract,
        'creator': r.creator,
        'contributor': r.contributor,
        'subject': r.subject,
        'language': r.language,
        'translated_language': r.translated_language,
        'resource_type': r.resource_type,
        'knowledge_domain_id': r.knowledge_domain_id,
        'publisher': r.publisher,
        'publication_date': r.publication_date,
        'digitisation_date': r.digitisation_date,
        'source_institution': r.source_institution,
        'institution_id': r.institution_id,
        'source_url': r.source_url,
        'access_url': r.access_url,
        'download_url': r.download_url,
        'license_id': r.license_id,
        'rights_statement': r.rights_statement,
        'access_status': r.access_status,
        'file_format': r.file_format,
        'file_size': r.file_size,
        'thumbnail_url': r.thumbnail_url,
        'isbn_or_identifier': r.isbn_or_identifier,
        'keywords': r.keywords,
        'citation': citations.get('apa', ''),
        'verification_status': r.verification_status,
        'verified_at': r.verified_at.isoformat() if r.verified_at else None,
        'created_at': r.created_at.isoformat() if r.created_at else '',
        'updated_at': r.updated_at.isoformat() if r.updated_at else '',
        'primary_domain': primary_dom,
        'license': lic,
        'institution_ref': inst,
        'dublin_core': dc.model_dump(),
        'citations': citations,
        'can_download': can_download,
        'download_allowed': can_download,
        'download_restriction_reason': reason,
        'educational_guide': RESOURCE_EDUCATION.get(r.id),
        'domains': [
            {'id': dom.id, 'name': dom.name, 'slug': dom.slug}
            for dom in (r.domains or ([r.primary_domain] if r.primary_domain else []))
        ],
    })

# 5. Statistics
stats = {
    'total_resources': len(resources_list),
    'total_domains': 52,
    'total_languages': len(set(r['language'] for r in resources_list)),
    'total_institutions': len(institutions_list),
    'total_licenses': len(licenses_list),
    'access_status_distribution': {},
    'resource_type_distribution': {},
    'language_distribution': {},
}

for r in resources_list:
    rt = r['resource_type']
    stats['resource_type_distribution'][rt] = stats['resource_type_distribution'].get(rt, 0) + 1
    lang = r['language']
    stats['language_distribution'][lang] = stats['language_distribution'].get(lang, 0) + 1
    status = r['access_status']
    stats['access_status_distribution'][status] = stats['access_status_distribution'].get(status, 0) + 1

db.close()

# Write TypeScript file
out_path = Path(__file__).resolve().parent.parent.parent / 'frontend' / 'src' / 'data' / 'fallbackData.ts'
out_path.parent.mkdir(parents=True, exist_ok=True)

ts_content = f"""// Auto-generated fallback repository data for standalone & offline reliability
import {{ KnowledgeDomain, Resource, ResourceDetail, RepositoryStatistics, License, Institution }} from '../types';

export const FALLBACK_DOMAINS: KnowledgeDomain[] = {json.dumps(domains_list, indent=2)};

export const FALLBACK_RESOURCES: ResourceDetail[] = {json.dumps(resources_list, indent=2)};

export const FALLBACK_LICENSES: License[] = {json.dumps(licenses_list, indent=2)};

export const FALLBACK_INSTITUTIONS: Institution[] = {json.dumps(institutions_list, indent=2)};

export const FALLBACK_STATISTICS: RepositoryStatistics = {json.dumps(stats, indent=2)};
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(ts_content)

print(f"Generated {out_path} successfully!")
print(f"Exported: {len(domains_list)} primary domains, {len(resources_list)} resources, {len(licenses_list)} licenses, {len(institutions_list)} institutions.")
