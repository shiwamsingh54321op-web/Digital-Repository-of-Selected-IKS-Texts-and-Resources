export interface KnowledgeDomainSimple {
  id: number;
  name: string;
  slug: string;
  sanskrit_name?: string | null;
}

export interface LicenseSimple {
  id: number;
  name: string;
  identifier: string;
  commercial_use_allowed: boolean;
  redistribution_allowed: boolean;
  attribution_required: boolean;
}

export interface InstitutionSimple {
  id: number;
  institution_name: string;
  slug: string;
  location?: string | null;
  website?: string | null;
  description?: string | null;
}

export interface DublinCoreMetadata {
  title: string;
  creator: string;
  subject: string;
  description: string;
  publisher?: string | null;
  contributor?: string | null;
  date?: string | null;
  type: string;
  format?: string | null;
  identifier?: string | null;
  source: string;
  language: string;
  relation?: string | null;
  coverage?: string | null;
  rights: string;
}

export interface Resource {
  id: number;
  title: string;
  subtitle?: string | null;
  description: string;
  abstract?: string | null;
  creator: string;
  contributor?: string | null;
  subject: string;
  language: string;
  translated_language?: string | null;
  resource_type: string;
  knowledge_domain_id: number;
  publisher?: string | null;
  publication_date?: string | null;
  digitisation_date?: string | null;
  source_institution: string;
  institution_id?: number | null;
  source_url: string;
  access_url?: string | null;
  download_url?: string | null;
  license_id: number;
  rights_statement: string;
  access_status: string;
  file_format?: string | null;
  file_size?: string | null;
  thumbnail_url?: string | null;
  isbn_or_identifier?: string | null;
  keywords?: string | null;
  citation?: string | null;
  verification_status: 'Verified' | 'Pending' | 'Rejected';
  verified_at?: string | null;
  created_at: string;
  updated_at: string;
  primary_domain?: KnowledgeDomainSimple | null;
  license?: LicenseSimple | null;
  institution_ref?: InstitutionSimple | null;
}

export interface ResourceEducationalGuide {
  subject_introduction: string;
  historical_context: string;
  learning_objectives: string[];
  chapters_and_topics: { section: string; topics: string }[];
  sanskrit_terminology: { term: string; meaning: string }[];
  examples: string[];
  recommended_reading: string[];
}

export interface ResourceDetail extends Resource {
  dublin_core: DublinCoreMetadata;
  can_download?: boolean;
  download_allowed?: boolean;
  download_restriction_reason?: string | null;
  related_resources?: Resource[];
  citations?: Record<string, string>;
  educational_guide?: ResourceEducationalGuide | null;
  domains?: KnowledgeDomainSimple[];
}

export interface PaginatedResources {
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
  has_next: boolean;
  has_prev: boolean;
  items: Resource[];
}

export interface DomainProfile {
  sanskrit_name?: string;
  introduction?: string;
  detailed_explanation?: string;
  historical_background?: string;
  important_concepts?: { term: string; meaning: string }[];
  major_contributors?: { name: string; era: string; contribution: string }[];
  important_texts?: { title: string; author: string; period: string }[];
  practical_applications?: string[];
  references?: { label: string; url: string }[];
  linked_resource_ids?: number[];
}

export interface KnowledgeDomain {
  id: number;
  name: string;
  slug: string;
  sanskrit_name?: string | null;
  description?: string | null;
  parent_id?: number | null;
  icon?: string | null;
  resource_count?: number;
  profile?: DomainProfile | null;
  subcategories?: KnowledgeDomain[];
}

export interface DomainDetailResponse {
  domain: KnowledgeDomain;
  parent_domain?: KnowledgeDomainSimple | null;
  subcategories: KnowledgeDomain[];
  total_resources: number;
  resources: Resource[];
}

export interface License {
  id: number;
  name: string;
  identifier: string;
  license_url?: string | null;
  description: string;
  permissions?: string | null;
  commercial_use_allowed: boolean;
  redistribution_allowed: boolean;
  attribution_required: boolean;
  verification_notes?: string | null;
}

export interface Institution {
  id: number;
  institution_name: string;
  name?: string;
  slug: string;
  location?: string | null;
  website?: string | null;
  description?: string | null;
  repository_type?: string | null;
  resource_count?: number;
}

export interface SearchResultItem {
  id: number;
  title: string;
  subtitle?: string | null;
  creator: string;
  subject: string;
  language: string;
  resource_type: string;
  knowledge_domain_id: number;
  domain_name?: string | null;
  domain_slug?: string | null;
  source_institution: string;
  license_name?: string | null;
  access_status: string;
  publication_date?: string | null;
  relevance_score?: number | null;
  highlight_snippet?: string | null;
}

export interface SearchResponse {
  query?: string | null;
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
  results: SearchResultItem[];
}

export interface SearchSuggestionItem {
  text: string;
  type: 'keyword' | 'title' | 'creator';
  matched_id?: number | null;
}

export interface RepositoryStatistics {
  total_resources: number;
  total_domains: number;
  total_languages: number;
  total_institutions: number;
  total_licenses: number;
  access_status_distribution: Record<string, number>;
  resource_type_distribution: Record<string, number>;
  language_distribution: Record<string, number>;
}

export interface Citations {
  apa: string;
  mla: string;
  chicago: string;
  bibtex: string;
}

export interface AdminUser {
  id: number;
  username: string;
  email: string;
  role: string;
  is_active: boolean;
  created_at: string;
}

export interface AdminDashboardData {
  overview: {
    total_resources: number;
    published_resources: number;
    pending_verification: number;
    rejected_resources: number;
    total_domains: number;
    total_institutions: number;
    total_licenses: number;
  };
  distributions: {
    access_statuses: Record<string, number>;
    resource_types: Record<string, number>;
    verification_statuses: Record<string, number>;
  };
}

export interface SearchAnalyticsItem {
  id: number;
  query: string;
  filters_used: Record<string, any>;
  result_count: number;
  created_at: string;
}

export interface TopQueryItem {
  query: string;
  count: number;
}

export interface AdminAnalyticsData {
  recent_searches: SearchAnalyticsItem[];
  top_queries: TopQueryItem[];
}
