import React from 'react';
import { Link } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import {
  BookOpen,
  Compass,
  Layers,
  ShieldCheck,
  Search,
  Scale,
  Award,
  ArrowRight,
  Database,
  Building,
  FileText,
  Languages
} from 'lucide-react';
import { api } from '../api/client';
import { SearchBar } from '../components/common/SearchBar';
import { ResourceCard } from '../components/resources/ResourceCard';

export const HomePage: React.FC = () => {
  // Fetch dynamic statistics
  const { data: stats, isLoading: statsLoading } = useQuery({
    queryKey: ['repository-statistics'],
    queryFn: () => api.getStatistics(),
  });

  // Fetch featured / recent resources
  const { data: recentData, isLoading: resourcesLoading } = useQuery({
    queryKey: ['recent-resources'],
    queryFn: () => api.getResources({ page: 1, page_size: 6, sort_by: 'newest' }),
  });

  // Fetch top-level domains
  const { data: domains } = useQuery({
    queryKey: ['knowledge-domains'],
    queryFn: () => api.getDomains(),
  });

  const topDomains = domains ? domains.filter(d => !d.parent_id).slice(0, 8) : [];

  return (
    <div className="space-y-20 pb-16">
      {/* Hero Section */}
      <section className="relative bg-navy-950 text-white overflow-hidden border-b border-gold-500/30 pt-20 pb-28 parchment-pattern">
        <div className="absolute inset-0 bg-navy-950/90 pointer-events-none" />
        
        {/* Subtle decorative gold lines */}
        <div className="absolute -top-24 -right-24 w-96 h-96 rounded-full bg-gold-500/10 blur-3xl pointer-events-none" />
        <div className="absolute -bottom-24 -left-24 w-96 h-96 rounded-full bg-gold-500/5 blur-3xl pointer-events-none" />

        <div className="relative max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-navy-900 border border-gold-400/30 text-gold-300 text-xs font-mono uppercase tracking-widest shadow-inner">
            <Award className="w-3.5 h-3.5 text-gold-400" />
            <span>Preserving Classical Indian Knowledge Systems</span>
          </div>

          <h1 className="font-serif text-3xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-ivory-50 max-w-4xl mx-auto leading-tight">
            Digital Repository of Selected <span className="text-gold-400 italic">IKS Texts</span> and Resources
          </h1>

          <p className="text-sm sm:text-lg text-ivory-300 max-w-2xl mx-auto font-light leading-relaxed">
            An open academic retrieval archive cataloging verified Sanskrit manuscripts, historical treatises, scientific translations, and Dublin Core metadata across 52 knowledge domains.
          </p>

          {/* Centered Search Engine Bar */}
          <div className="pt-4 max-w-3xl mx-auto">
            <SearchBar autoFocus={false} />
            <div className="flex flex-wrap items-center justify-center gap-2 pt-3 text-xs text-ivory-400">
              <span className="font-medium text-gold-300">Popular treatises:</span>
              <Link to="/explore?q=Aryabhatiya" className="hover:text-gold-300 underline underline-offset-2">Aryabhatiya</Link>
              <span>•</span>
              <Link to="/explore?q=Charaka+Samhita" className="hover:text-gold-300 underline underline-offset-2">Charaka Samhita</Link>
              <span>•</span>
              <Link to="/explore?q=Sulba+Sutra" className="hover:text-gold-300 underline underline-offset-2">Sulba Sutras</Link>
              <span>•</span>
              <Link to="/explore?q=Arthashastra" className="hover:text-gold-300 underline underline-offset-2">Arthashastra</Link>
              <span>•</span>
              <Link to="/explore?q=Vrikshayurveda" className="hover:text-gold-300 underline underline-offset-2">Vrikshayurveda</Link>
            </div>
          </div>
        </div>
      </section>

      {/* Dynamic Statistics Bar */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-16 relative z-10">
        <div className="bg-white rounded-2xl border border-ivory-300 shadow-parchment-lg p-6 sm:p-8">
          <div className="grid grid-cols-2 md:grid-cols-5 gap-6 text-center divide-y md:divide-y-0 md:divide-x divide-ivory-200">
            <div className="pt-2 md:pt-0">
              <div className="flex justify-center mb-2">
                <BookOpen className="w-5 h-5 text-gold-600" />
              </div>
              <p className="font-serif text-3xl font-bold text-navy-950">
                {statsLoading ? '...' : stats?.total_resources ?? 32}
              </p>
              <p className="text-xs font-mono uppercase tracking-wider text-navy-600 mt-1">
                Verified Treatises
              </p>
            </div>

            <div className="pt-4 md:pt-0">
              <div className="flex justify-center mb-2">
                <Layers className="w-5 h-5 text-gold-600" />
              </div>
              <p className="font-serif text-3xl font-bold text-navy-950">
                {statsLoading ? '...' : stats?.total_domains ?? 52}
              </p>
              <p className="text-xs font-mono uppercase tracking-wider text-navy-600 mt-1">
                Taxonomic Domains
              </p>
            </div>

            <div className="pt-4 md:pt-0">
              <div className="flex justify-center mb-2">
                <Building className="w-5 h-5 text-gold-600" />
              </div>
              <p className="font-serif text-3xl font-bold text-navy-950">
                {statsLoading ? '...' : stats?.total_institutions ?? 12}
              </p>
              <p className="text-xs font-mono uppercase tracking-wider text-navy-600 mt-1">
                Holding Archives
              </p>
            </div>

            <div className="pt-4 md:pt-0">
              <div className="flex justify-center mb-2">
                <Scale className="w-5 h-5 text-gold-600" />
              </div>
              <p className="font-serif text-3xl font-bold text-navy-950">
                {statsLoading ? '...' : stats?.total_licenses ?? 9}
              </p>
              <p className="text-xs font-mono uppercase tracking-wider text-navy-600 mt-1">
                Legal Licenses
              </p>
            </div>

            <div className="col-span-2 md:col-span-1 pt-4 md:pt-0">
              <div className="flex justify-center mb-2">
                <Languages className="w-5 h-5 text-gold-600" />
              </div>
              <p className="font-serif text-3xl font-bold text-navy-950">
                {statsLoading ? '...' : stats?.total_languages ?? 3}
              </p>
              <p className="text-xs font-mono uppercase tracking-wider text-navy-600 mt-1">
                Classical Languages
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Knowledge Domains */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between mb-8 gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono text-gold-700 uppercase tracking-widest mb-1">
              <Layers className="w-4 h-4" />
              <span>Taxonomic Classification</span>
            </div>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold text-navy-950">
              Primary Knowledge Domains
            </h2>
            <p className="text-sm text-navy-600 mt-1">
              Explore resources categorized under India's traditional intellectual disciplines.
            </p>
          </div>

          <Link
            to="/domains"
            className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-navy-900 hover:text-gold-700 transition-colors"
          >
            <span>View All 52 Domains & Subcategories</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {topDomains.map((domain) => (
            <Link
              key={domain.id}
              to={`/explore?domain_slug=${domain.slug}`}
              className="bg-white border border-ivory-300 rounded-xl p-5 hover:border-gold-500 hover:shadow-parchment-lg transition-all group flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xs font-mono text-gold-700 font-semibold">
                    {domain.sanskrit_name || 'IKS Discipline'}
                  </span>
                  <span className="text-[11px] bg-ivory-100 text-navy-600 px-2 py-0.5 rounded-full font-mono">
                    {domain.subcategories?.length || 0} sub-branches
                  </span>
                </div>
                <h3 className="font-serif text-base font-bold text-navy-900 group-hover:text-gold-700 transition-colors mb-2">
                  {domain.name}
                </h3>
                <p className="text-xs text-navy-600 line-clamp-3 leading-relaxed">
                  {domain.description || 'Classical treatise records and scholarly metadata available in this repository.'}
                </p>
              </div>

              <div className="mt-4 pt-3 border-t border-ivory-200 flex items-center justify-between text-xs text-gold-700 font-medium">
                <span>Browse Domain</span>
                <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Featured / Verified Resources */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between mb-8 gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono text-gold-700 uppercase tracking-widest mb-1">
              <BookOpen className="w-4 h-4" />
              <span>Catalog Highlights</span>
            </div>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold text-navy-950">
              Recently Verified Treatises
            </h2>
            <p className="text-sm text-navy-600 mt-1">
              Peer-reviewed and verified records complete with Dublin Core metadata and digital links.
            </p>
          </div>

          <Link
            to="/explore"
            className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-navy-900 hover:text-gold-700 transition-colors"
          >
            <span>Browse Complete Catalogue ({stats?.total_resources ?? 32})</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        {resourcesLoading ? (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6].map((n) => (
              <div key={n} className="bg-white border border-ivory-200 rounded-xl p-6 h-64 animate-pulse" />
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {recentData?.items.map((res) => (
              <ResourceCard key={res.id} resource={res} viewMode="grid" />
            ))}
          </div>
        )}
      </section>

      {/* Architectural Pillars / College Assignment Scope */}
      <section className="bg-navy-900 text-ivory-50 border-y border-gold-500/30 py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <span className="text-xs font-mono text-gold-400 uppercase tracking-widest">
              Standardized Archival Methodology
            </span>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold mt-2">
              The Three Pillars of the IKS Digital Repository
            </h2>
            <p className="text-sm text-ivory-300 mt-2 font-light">
              Fulfilling the institutional mandate for metadata precision, full-text retrieval, and legal rights governance.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-navy-950/80 border border-gold-500/30 rounded-xl p-6 space-y-3">
              <div className="w-10 h-10 rounded-lg bg-navy-900 border border-gold-400/30 flex items-center justify-center text-gold-400">
                <Database className="w-5 h-5" />
              </div>
              <h3 className="font-serif text-lg font-bold text-white">
                1. Dublin Core Metadata Standard
              </h3>
              <p className="text-xs text-ivory-300 leading-relaxed">
                All 32 canonical treatises follow the 15 core Dublin Core metadata elements (Title, Creator, Subject, Description, Publisher, Contributor, Date, Type, Format, Identifier, Source, Language, Relation, Coverage, Rights) to ensure interoperability across international archives.
              </p>
            </div>

            <div className="bg-navy-950/80 border border-gold-500/30 rounded-xl p-6 space-y-3">
              <div className="w-10 h-10 rounded-lg bg-navy-900 border border-gold-400/30 flex items-center justify-center text-gold-400">
                <Search className="w-5 h-5" />
              </div>
              <h3 className="font-serif text-lg font-bold text-white">
                2. SQLite FTS5 & BM25 Retrieval
              </h3>
              <p className="text-xs text-ivory-300 leading-relaxed">
                High-performance full-text search with BM25 relevance ranking. Tokenized with Unicode61 and diacritic stripping to allow seamless matching of Sanskrit words, Romanized IAST transliterations, authors, and subjects.
              </p>
            </div>

            <div className="bg-navy-950/80 border border-gold-500/30 rounded-xl p-6 space-y-3">
              <div className="w-10 h-10 rounded-lg bg-navy-900 border border-gold-400/30 flex items-center justify-center text-gold-400">
                <Scale className="w-5 h-5" />
              </div>
              <h3 className="font-serif text-lg font-bold text-white">
                3. Legal Rights & Controlled Downloads
              </h3>
              <p className="text-xs text-ivory-300 leading-relaxed">
                Clear distinction between Open Access, Public Domain, Creative Commons, and In-Copyright works. Direct downloads are verified against license permissions, preventing unauthorized file redistribution while encouraging legitimate research.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
