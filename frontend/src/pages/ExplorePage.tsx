import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import {
  Filter,
  SlidersHorizontal,
  Grid,
  List,
  RotateCcw,
  BookOpen,
  ChevronLeft,
  ChevronRight,
  Search as SearchIcon,
  X
} from 'lucide-react';
import { api } from '../api/client';
import { ResourceCard } from '../components/resources/ResourceCard';
import { SearchBar } from '../components/common/SearchBar';
import {
  FALLBACK_DOMAINS,
  FALLBACK_LICENSES,
  FALLBACK_INSTITUTIONS,
  FALLBACK_RESOURCES
} from '../data/fallbackData';

export const ExplorePage: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();

  // URL state
  const query = searchParams.get('q') || '';
  const domainSlug = searchParams.get('domain_slug') || '';
  const domainId = searchParams.get('domain_id') ? Number(searchParams.get('domain_id')) : undefined;
  const resourceType = searchParams.get('resource_type') || '';
  const language = searchParams.get('language') || '';
  const accessStatus = searchParams.get('access_status') || '';
  const licenseId = searchParams.get('license_id') ? Number(searchParams.get('license_id')) : undefined;
  const institutionId = searchParams.get('institution_id') ? Number(searchParams.get('institution_id')) : undefined;
  const sortBy = searchParams.get('sort_by') || (query ? 'relevance' : 'newest');
  const page = searchParams.get('page') ? Number(searchParams.get('page')) : 1;

  const [viewMode, setViewMode] = useState<'grid' | 'list'>('grid');
  const [mobileFilterOpen, setMobileFilterOpen] = useState(false);

  // Fetch Taxonomy for Filter Dropdowns
  const { data: domains = FALLBACK_DOMAINS } = useQuery({
    queryKey: ['filter-domains'],
    queryFn: async () => {
      try {
        return await api.getDomains();
      } catch {
        return FALLBACK_DOMAINS;
      }
    },
    initialData: FALLBACK_DOMAINS,
  });

  const { data: licenses = FALLBACK_LICENSES } = useQuery({
    queryKey: ['filter-licenses'],
    queryFn: async () => {
      try {
        return await api.getLicenses();
      } catch {
        return FALLBACK_LICENSES;
      }
    },
    initialData: FALLBACK_LICENSES,
  });

  const { data: institutions = FALLBACK_INSTITUTIONS } = useQuery({
    queryKey: ['filter-institutions'],
    queryFn: async () => {
      try {
        return await api.getInstitutions();
      } catch {
        return FALLBACK_INSTITUTIONS;
      }
    },
    initialData: FALLBACK_INSTITUTIONS,
  });

  // Query resources or full-text search
  const { data: resourcesData, isLoading, isFetching } = useQuery({
    queryKey: [
      'resources-list',
      query,
      domainSlug,
      domainId,
      resourceType,
      language,
      accessStatus,
      licenseId,
      institutionId,
      sortBy,
      page,
    ],
    queryFn: async () => {
      try {
        if (query.trim()) {
          // Use full-text search engine endpoint
          const res = await api.search({
            q: query.trim(),
            domain_slug: domainSlug || undefined,
            domain_id: domainId,
            resource_type: resourceType || undefined,
            language: language || undefined,
            access_status: accessStatus || undefined,
            license_id: licenseId,
            institution_id: institutionId,
            sort_by: sortBy,
            page,
            page_size: 12,
          });

          return {
            total: res.total,
            page: res.page,
            page_size: res.page_size,
            total_pages: res.total_pages,
            has_next: res.page < res.total_pages,
            has_prev: res.page > 1,
            items: res.results.map((r: any) => ({
              ...r,
              verification_status: 'Verified',
              rights_statement: r.license_name || 'Standard Archival Rights',
              source_url: '',
              created_at: new Date().toISOString(),
              updated_at: new Date().toISOString(),
              primary_domain: r.domain_name ? { id: r.knowledge_domain_id, name: r.domain_name, slug: r.domain_slug || '' } : undefined,
            })),
          };
        } else {
          // Use standard catalog endpoint
          return await api.getResources({
            page,
            page_size: 12,
            domain_slug: domainSlug || undefined,
            domain_id: domainId,
            resource_type: resourceType || undefined,
            language: language || undefined,
            access_status: accessStatus || undefined,
            license_id: licenseId,
            institution_id: institutionId,
            sort_by: sortBy,
          });
        }
      } catch (err) {
        // Fallback to local catalog filtering if backend is unreachable
        let items = [...FALLBACK_RESOURCES];
        if (query.trim()) {
          const q = query.toLowerCase();
          items = items.filter(
            (r) =>
              r.title.toLowerCase().includes(q) ||
              r.creator.toLowerCase().includes(q) ||
              r.description.toLowerCase().includes(q) ||
              r.subject.toLowerCase().includes(q)
          );
        }
        if (domainId) {
          items = items.filter((r) => r.knowledge_domain_id === domainId);
        }
        if (resourceType) {
          items = items.filter((r) => r.resource_type === resourceType);
        }
        if (language) {
          items = items.filter((r) => r.language === language);
        }
        if (accessStatus) {
          items = items.filter((r) => r.access_status === accessStatus);
        }
        if (licenseId) {
          items = items.filter((r) => r.license_id === licenseId);
        }
        if (institutionId) {
          items = items.filter((r) => r.institution_id === institutionId);
        }

        const pageSize = 12;
        const total = items.length;
        const totalPages = Math.ceil(total / pageSize) || 1;
        const start = (page - 1) * pageSize;
        const paginatedItems = items.slice(start, start + pageSize);

        return {
          total,
          page,
          page_size: pageSize,
          total_pages: totalPages,
          has_next: page < totalPages,
          has_prev: page > 1,
          items: paginatedItems,
        };
      }
    },
  });

  const updateParam = (key: string, value: string | null) => {
    const next = new URLSearchParams(searchParams);
    if (value === null || value === '') {
      next.delete(key);
    } else {
      next.set(key, value);
    }
    next.set('page', '1'); // reset page on filter change
    setSearchParams(next);
  };

  const clearAllFilters = () => {
    setSearchParams(new URLSearchParams());
  };

  const handlePageChange = (newPage: number) => {
    const next = new URLSearchParams(searchParams);
    next.set('page', newPage.toString());
    setSearchParams(next);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const hasActiveFilters = Boolean(
    query || domainSlug || domainId || resourceType || language || accessStatus || licenseId || institutionId
  );

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Top Breadcrumb & Title */}
      <div className="mb-8">
        <h1 className="font-serif text-3xl font-bold text-navy-950">
          Repository Catalogue Explorer
        </h1>
        <p className="text-sm text-navy-600 mt-1">
          Explore and retrieve verified Indian Knowledge System texts, manuscripts, and translations.
        </p>

        {/* Search Bar */}
        <div className="mt-5 max-w-3xl">
          <SearchBar
            initialValue={query}
            onSearchSubmit={(val) => updateParam('q', val)}
            placeholder="Search treatises, creators, subjects, or keywords..."
          />
        </div>
      </div>

      <div className="flex flex-col lg:flex-row gap-8 items-start">
        {/* Filters Sidebar */}
        <aside
          className={`lg:w-72 w-full bg-white border border-ivory-300 rounded-xl p-5 shadow-parchment flex-shrink-0 ${
            mobileFilterOpen ? 'block' : 'hidden lg:block'
          }`}
        >
          <div className="flex items-center justify-between pb-4 mb-4 border-b border-ivory-200">
            <div className="flex items-center gap-2 font-serif font-bold text-navy-900 text-sm">
              <SlidersHorizontal className="w-4 h-4 text-gold-600" />
              <span>Faceted Filters</span>
            </div>
            {hasActiveFilters && (
              <button
                onClick={clearAllFilters}
                className="text-xs text-gold-700 hover:text-navy-950 font-medium flex items-center gap-1"
              >
                <RotateCcw className="w-3 h-3" />
                <span>Reset</span>
              </button>
            )}
          </div>

          <div className="space-y-5 text-xs">
            {/* Knowledge Domain */}
            <div>
              <label className="block font-semibold uppercase tracking-wider text-navy-700 mb-1.5 font-mono">
                Knowledge Domain
              </label>
              <select
                value={domainSlug || ''}
                onChange={(e) => updateParam('domain_slug', e.target.value || null)}
                className="w-full px-3 py-2 bg-ivory-50 border border-ivory-300 rounded-lg text-navy-900 focus:outline-none focus:ring-1 focus:ring-gold-500 text-xs"
              >
                <option value="">All Domains (52 Categories)</option>
                {domains?.filter(d => !d.parent_id).map((d) => (
                  <option key={d.id} value={d.slug}>
                    {d.name} {d.sanskrit_name ? `(${d.sanskrit_name})` : ''}
                  </option>
                ))}
              </select>
            </div>

            {/* Resource Type */}
            <div>
              <label className="block font-semibold uppercase tracking-wider text-navy-700 mb-1.5 font-mono">
                Resource Type
              </label>
              <select
                value={resourceType}
                onChange={(e) => updateParam('resource_type', e.target.value || null)}
                className="w-full px-3 py-2 bg-ivory-50 border border-ivory-300 rounded-lg text-navy-900 focus:outline-none focus:ring-1 focus:ring-gold-500 text-xs"
              >
                <option value="">All Resource Types</option>
                <option value="Manuscript">Manuscript</option>
                <option value="Critical Edition">Critical Edition</option>
                <option value="Book">Book / Treatise</option>
                <option value="Monograph">Monograph</option>
                <option value="Research Paper">Research Paper</option>
                <option value="Translation">Translation & Commentary</option>
              </select>
            </div>

            {/* Language */}
            <div>
              <label className="block font-semibold uppercase tracking-wider text-navy-700 mb-1.5 font-mono">
                Original Language
              </label>
              <select
                value={language}
                onChange={(e) => updateParam('language', e.target.value || null)}
                className="w-full px-3 py-2 bg-ivory-50 border border-ivory-300 rounded-lg text-navy-900 focus:outline-none focus:ring-1 focus:ring-gold-500 text-xs"
              >
                <option value="">All Languages</option>
                <option value="Sanskrit">Sanskrit (Classical & Vedic)</option>
                <option value="Tamil">Classical Tamil</option>
                <option value="Prakrit">Prakrit / Pali</option>
                <option value="English">English Translation / Scholarly Edition</option>
              </select>
            </div>

            {/* Access Status */}
            <div>
              <label className="block font-semibold uppercase tracking-wider text-navy-700 mb-1.5 font-mono">
                Access & Rights Status
              </label>
              <select
                value={accessStatus}
                onChange={(e) => updateParam('access_status', e.target.value || null)}
                className="w-full px-3 py-2 bg-ivory-50 border border-ivory-300 rounded-lg text-navy-900 focus:outline-none focus:ring-1 focus:ring-gold-500 text-xs"
              >
                <option value="">All Rights Categories</option>
                <option value="Open Access">Open Access</option>
                <option value="Download Available">Download Available</option>
                <option value="Read Online">Read Online (Restricted DL)</option>
                <option value="Restricted Access">Restricted Access</option>
              </select>
            </div>

            {/* Source Institution */}
            <div>
              <label className="block font-semibold uppercase tracking-wider text-navy-700 mb-1.5 font-mono">
                Source Institution
              </label>
              <select
                value={institutionId || ''}
                onChange={(e) => updateParam('institution_id', e.target.value || null)}
                className="w-full px-3 py-2 bg-ivory-50 border border-ivory-300 rounded-lg text-navy-900 focus:outline-none focus:ring-1 focus:ring-gold-500 text-xs"
              >
                <option value="">All Holding Institutions</option>
                {institutions?.map((inst) => (
                  <option key={inst.id} value={inst.id}>
                    {inst.institution_name}
                  </option>
                ))}
              </select>
            </div>

            {/* License Filter */}
            <div>
              <label className="block font-semibold uppercase tracking-wider text-navy-700 mb-1.5 font-mono">
                Legal License
              </label>
              <select
                value={licenseId || ''}
                onChange={(e) => updateParam('license_id', e.target.value || null)}
                className="w-full px-3 py-2 bg-ivory-50 border border-ivory-300 rounded-lg text-navy-900 focus:outline-none focus:ring-1 focus:ring-gold-500 text-xs"
              >
                <option value="">All Licenses (9 Types)</option>
                {licenses?.map((lic) => (
                  <option key={lic.id} value={lic.id}>
                    {lic.name}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </aside>

        {/* Results Main Content */}
        <div className="flex-1 w-full">
          {/* Controls Bar */}
          <div className="bg-white border border-ivory-300 rounded-xl px-4 py-3 mb-6 shadow-sm flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-2 text-xs text-navy-700 font-mono">
              <span className="font-bold text-navy-950 font-serif text-base">
                {resourcesData?.total ?? 0}
              </span>
              <span>treatises indexed</span>
              {isFetching && <span className="text-gold-600 animate-pulse">(updating...)</span>}
            </div>

            <div className="flex items-center gap-3">
              {/* Mobile Filter Toggle */}
              <button
                onClick={() => setMobileFilterOpen(!mobileFilterOpen)}
                className="lg:hidden px-3 py-1.5 bg-ivory-100 border border-ivory-300 rounded-lg text-xs font-medium text-navy-800 flex items-center gap-1.5"
              >
                <Filter className="w-3.5 h-3.5 text-gold-600" />
                <span>Filters {hasActiveFilters && '•'}</span>
              </button>

              {/* Sort By */}
              <div className="flex items-center gap-1.5 text-xs text-navy-700">
                <span className="font-mono text-navy-500">Sort:</span>
                <select
                  value={sortBy}
                  onChange={(e) => updateParam('sort_by', e.target.value)}
                  className="bg-ivory-50 border border-ivory-300 rounded-lg px-2.5 py-1 text-xs text-navy-900 focus:outline-none focus:ring-1 focus:ring-gold-500 font-medium"
                >
                  {query && <option value="relevance">Relevance (BM25)</option>}
                  <option value="newest">Newest Catalogued</option>
                  <option value="oldest">Oldest Catalogued</option>
                  <option value="title_asc">Title (A-Z)</option>
                  <option value="title_desc">Title (Z-A)</option>
                </select>
              </div>

              {/* View Switch */}
              <div className="hidden sm:flex items-center border border-ivory-300 rounded-lg p-0.5 bg-ivory-50">
                <button
                  onClick={() => setViewMode('grid')}
                  className={`p-1.5 rounded ${viewMode === 'grid' ? 'bg-white text-gold-700 shadow-xs' : 'text-navy-400 hover:text-navy-700'}`}
                  title="Grid View"
                >
                  <Grid className="w-3.5 h-3.5" />
                </button>
                <button
                  onClick={() => setViewMode('list')}
                  className={`p-1.5 rounded ${viewMode === 'list' ? 'bg-white text-gold-700 shadow-xs' : 'text-navy-400 hover:text-navy-700'}`}
                  title="List View"
                >
                  <List className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          </div>

          {/* Active Filter Pills */}
          {hasActiveFilters && (
            <div className="flex flex-wrap items-center gap-2 mb-6">
              <span className="text-xs text-navy-500 font-mono">Active Filters:</span>
              {query && (
                <span className="inline-flex items-center gap-1 px-2.5 py-1 bg-gold-50 border border-gold-200 text-gold-800 text-xs rounded-full">
                  Query: "{query}"
                  <button onClick={() => updateParam('q', null)}><X className="w-3 h-3 hover:text-navy-900" /></button>
                </span>
              )}
              {domainSlug && (
                <span className="inline-flex items-center gap-1 px-2.5 py-1 bg-gold-50 border border-gold-200 text-gold-800 text-xs rounded-full">
                  Domain: {domainSlug}
                  <button onClick={() => updateParam('domain_slug', null)}><X className="w-3 h-3 hover:text-navy-900" /></button>
                </span>
              )}
              {resourceType && (
                <span className="inline-flex items-center gap-1 px-2.5 py-1 bg-gold-50 border border-gold-200 text-gold-800 text-xs rounded-full">
                  Type: {resourceType}
                  <button onClick={() => updateParam('resource_type', null)}><X className="w-3 h-3 hover:text-navy-900" /></button>
                </span>
              )}
              {language && (
                <span className="inline-flex items-center gap-1 px-2.5 py-1 bg-gold-50 border border-gold-200 text-gold-800 text-xs rounded-full">
                  Lang: {language}
                  <button onClick={() => updateParam('language', null)}><X className="w-3 h-3 hover:text-navy-900" /></button>
                </span>
              )}
              {accessStatus && (
                <span className="inline-flex items-center gap-1 px-2.5 py-1 bg-gold-50 border border-gold-200 text-gold-800 text-xs rounded-full">
                  Status: {accessStatus}
                  <button onClick={() => updateParam('access_status', null)}><X className="w-3 h-3 hover:text-navy-900" /></button>
                </span>
              )}
            </div>
          )}

          {/* Catalog Listing */}
          {isLoading ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {[1, 2, 3, 4, 5, 6].map((i) => (
                <div key={i} className="bg-white border border-ivory-200 rounded-xl p-5 h-64 animate-pulse" />
              ))}
            </div>
          ) : resourcesData?.items && resourcesData.items.length > 0 ? (
            <div
              className={
                viewMode === 'grid'
                  ? 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'
                  : 'space-y-4'
              }
            >
              {resourcesData.items.map((resource) => (
                <ResourceCard
                  key={resource.id}
                  resource={resource}
                  viewMode={viewMode}
                />
              ))}
            </div>
          ) : (
            <div className="bg-white border border-ivory-300 rounded-xl p-12 text-center shadow-sm">
              <BookOpen className="w-12 h-12 text-gold-500 mx-auto mb-3" />
              <h3 className="font-serif text-lg font-bold text-navy-900">
                No Treatises Found Matching Criteria
              </h3>
              <p className="text-xs text-navy-600 max-w-md mx-auto mt-1 mb-4">
                Try loosening your filters, removing search terms, or checking spelling.
              </p>
              <button
                onClick={clearAllFilters}
                className="px-4 py-2 bg-navy-900 text-gold-300 rounded-lg text-xs font-medium hover:bg-navy-800 transition-colors"
              >
                Reset All Filters
              </button>
            </div>
          )}

          {/* Pagination Controls */}
          {resourcesData && resourcesData.total_pages > 1 && (
            <div className="mt-10 flex items-center justify-between border-t border-ivory-300 pt-6">
              <button
                disabled={!resourcesData.has_prev}
                onClick={() => handlePageChange(page - 1)}
                className="px-3.5 py-2 border border-ivory-300 rounded-lg text-xs font-medium text-navy-800 hover:bg-white disabled:opacity-40 disabled:cursor-not-allowed flex items-center gap-1.5"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Previous Page</span>
              </button>

              <div className="text-xs text-navy-600 font-mono">
                Page <span className="font-bold text-navy-950">{resourcesData.page}</span> of {resourcesData.total_pages}
              </div>

              <button
                disabled={!resourcesData.has_next}
                onClick={() => handlePageChange(page + 1)}
                className="px-3.5 py-2 border border-ivory-300 rounded-lg text-xs font-medium text-navy-800 hover:bg-white disabled:opacity-40 disabled:cursor-not-allowed flex items-center gap-1.5"
              >
                <span>Next Page</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
