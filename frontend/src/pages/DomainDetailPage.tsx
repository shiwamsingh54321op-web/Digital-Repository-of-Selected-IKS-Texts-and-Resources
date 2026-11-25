import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import {
  Layers,
  BookOpen,
  ChevronRight,
  Compass,
  History,
  Lightbulb,
  Users,
  Bookmark,
  ExternalLink,
  ArrowLeft,
  CheckCircle2,
  Sparkles
} from 'lucide-react';
import { api } from '../api/client';
import { DomainDetailResponse, KnowledgeDomain } from '../types';
import { FALLBACK_DOMAINS, FALLBACK_RESOURCES } from '../data/fallbackData';
import { ResourceCard } from '../components/resources/ResourceCard';

function buildFallbackDomainDetail(slug: string): DomainDetailResponse | undefined {
  let foundDomain: KnowledgeDomain | undefined;
  let parentDomain: KnowledgeDomain | undefined;

  for (const d of FALLBACK_DOMAINS) {
    if (d.slug === slug) {
      foundDomain = d;
      break;
    }
    const sub = d.subcategories?.find((s) => s.slug === slug);
    if (sub) {
      foundDomain = sub;
      parentDomain = d;
      break;
    }
  }

  if (!foundDomain) return undefined;

  const linkedIds = new Set(foundDomain.profile?.linked_resource_ids || []);
  const subSlugs = new Set((foundDomain.subcategories || []).map((s) => s.slug));
  const resources = FALLBACK_RESOURCES.filter(
    (r) =>
      linkedIds.has(r.id) ||
      r.primary_domain?.slug === slug ||
      r.domains?.some((dom) => dom.slug === slug || subSlugs.has(dom.slug))
  );

  return {
    domain: foundDomain,
    parent_domain: parentDomain
      ? { id: parentDomain.id, name: parentDomain.name, slug: parentDomain.slug, sanskrit_name: parentDomain.sanskrit_name }
      : null,
    subcategories: foundDomain.subcategories || parentDomain?.subcategories?.filter((s) => s.slug !== slug) || [],
    total_resources: resources.length,
    resources,
  };
}

export const DomainDetailPage: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const fallback = slug ? buildFallbackDomainDetail(slug) : undefined;

  const { data, isLoading, error } = useQuery({
    queryKey: ['domain-detail', slug],
    queryFn: async () => {
      if (!slug) throw new Error('Missing domain slug');
      try {
        return await api.getDomain(slug);
      } catch (err) {
        if (fallback) return fallback;
        throw err;
      }
    },
    enabled: !!slug,
    initialData: fallback,
  });

  if (isLoading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 text-center">
        <div className="w-10 h-10 border-3 border-gold-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="font-serif text-lg text-navy-800">Loading Knowledge Domain Monograph...</p>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <Layers className="w-12 h-12 text-gold-600 mx-auto mb-3" />
        <h2 className="font-serif text-2xl font-bold text-navy-900">Knowledge Domain Not Found</h2>
        <p className="text-xs text-navy-600 mt-2 mb-6">
          The requested domain ({slug}) could not be located in the repository taxonomy.
        </p>
        <Link
          to="/domains"
          className="inline-flex items-center gap-2 px-4 py-2 bg-navy-900 text-gold-300 rounded-lg text-xs font-medium"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Return to Knowledge Domains</span>
        </Link>
      </div>
    );
  }

  const { domain, parent_domain, subcategories, resources } = data;
  const profile = domain.profile || fallback?.domain.profile;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Breadcrumbs */}
      <nav className="flex items-center gap-2 text-xs text-navy-600 font-mono overflow-x-auto whitespace-nowrap pb-1">
        <Link to="/" className="hover:text-gold-700">Home</Link>
        <ChevronRight className="w-3.5 h-3.5 text-navy-400" />
        <Link to="/domains" className="hover:text-gold-700">Knowledge Domains</Link>
        {parent_domain && (
          <>
            <ChevronRight className="w-3.5 h-3.5 text-navy-400" />
            <Link to={`/domains/${parent_domain.slug}`} className="hover:text-gold-700">
              {parent_domain.name}
            </Link>
          </>
        )}
        <ChevronRight className="w-3.5 h-3.5 text-navy-400" />
        <span className="text-navy-900 font-medium">{domain.name}</span>
      </nav>

      {/* Domain Header Card */}
      <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="flex flex-wrap items-center gap-2">
            <span className="font-mono text-xs font-semibold text-gold-800 bg-gold-50 px-2.5 py-1 rounded border border-gold-200">
              {domain.sanskrit_name || profile?.sanskrit_name || 'IKS Discipline'}
            </span>
            <span className="text-xs font-mono text-navy-600 bg-ivory-100 px-2.5 py-1 rounded border border-ivory-200">
              {resources.length} Connected {resources.length === 1 ? 'Resource' : 'Resources'}
            </span>
          </div>

          <Link
            to={`/explore?domain_slug=${domain.slug}`}
            className="px-4 py-2 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-xl text-xs font-semibold inline-flex items-center gap-1.5 shadow-sm transition-colors"
          >
            <Compass className="w-3.5 h-3.5" />
            <span>Filter in Explore Catalog</span>
          </Link>
        </div>

        <h1 className="font-serif text-2xl sm:text-4xl font-bold text-navy-950">
          {domain.name}
        </h1>

        <p className="text-sm sm:text-base text-navy-800 leading-relaxed">
          {profile?.introduction || domain.description}
        </p>

        {profile?.detailed_explanation && (
          <p className="text-xs sm:text-sm text-navy-600 leading-relaxed pt-2 border-t border-ivory-200">
            {profile.detailed_explanation}
          </p>
        )}
      </div>

      {/* Scholarly Overview Grid */}
      {profile && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 space-y-8">
            {/* Historical Background */}
            {profile.historical_background && (
              <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment space-y-3">
                <h2 className="font-serif text-xl font-bold text-navy-950 flex items-center gap-2 pb-2 border-b border-ivory-200">
                  <History className="w-5 h-5 text-gold-600" />
                  <span>Historical Background &amp; Evolution</span>
                </h2>
                <p className="text-sm text-navy-700 leading-relaxed">
                  {profile.historical_background}
                </p>
              </div>
            )}

            {/* Important Concepts & Sanskrit Terminology */}
            {profile.important_concepts && profile.important_concepts.length > 0 && (
              <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment space-y-4">
                <h2 className="font-serif text-xl font-bold text-navy-950 flex items-center gap-2 pb-2 border-b border-ivory-200">
                  <Lightbulb className="w-5 h-5 text-gold-600" />
                  <span>Core Concepts &amp; Key Terminology</span>
                </h2>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {profile.important_concepts.map((c, idx) => (
                    <div key={idx} className="p-4 bg-ivory-50 border border-ivory-200 rounded-xl space-y-1">
                      <h3 className="font-serif text-sm font-bold text-navy-950">{c.term}</h3>
                      <p className="text-xs text-navy-700 leading-relaxed">{c.meaning}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Major Contributors & Scholars */}
            {profile.major_contributors && profile.major_contributors.length > 0 && (
              <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment space-y-4">
                <h2 className="font-serif text-xl font-bold text-navy-950 flex items-center gap-2 pb-2 border-b border-ivory-200">
                  <Users className="w-5 h-5 text-gold-600" />
                  <span>Major Contributors &amp; Scholars</span>
                </h2>
                <div className="divide-y divide-ivory-200">
                  {profile.major_contributors.map((person, idx) => (
                    <div key={idx} className="py-3 first:pt-0 last:pb-0">
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <span className="font-serif text-sm font-bold text-navy-950">{person.name}</span>
                        <span className="text-[11px] font-mono text-gold-700 bg-gold-50 px-2 py-0.5 rounded border border-gold-200">
                          {person.era}
                        </span>
                      </div>
                      <p className="text-xs text-navy-700 mt-1 leading-relaxed">{person.contribution}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Right Sidebar: Key Texts, Practical Applications & References */}
          <div className="space-y-6">
            {profile.important_texts && profile.important_texts.length > 0 && (
              <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment space-y-3">
                <h3 className="font-serif text-base font-bold text-navy-950 flex items-center gap-2 pb-2 border-b border-ivory-200">
                  <Bookmark className="w-4 h-4 text-gold-600" />
                  <span>Foundational Texts</span>
                </h3>
                <ul className="space-y-2.5 text-xs">
                  {profile.important_texts.map((t, idx) => (
                    <li key={idx} className="p-2.5 bg-ivory-50 border border-ivory-200 rounded-lg">
                      <div className="font-semibold text-navy-900">{t.title}</div>
                      <div className="text-navy-600 mt-0.5">{t.author} • <span className="font-mono text-[11px]">{t.period}</span></div>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {profile.practical_applications && profile.practical_applications.length > 0 && (
              <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment space-y-3">
                <h3 className="font-serif text-base font-bold text-navy-950 flex items-center gap-2 pb-2 border-b border-ivory-200">
                  <Sparkles className="w-4 h-4 text-gold-600" />
                  <span>Practical Applications</span>
                </h3>
                <ul className="space-y-2 text-xs text-navy-700">
                  {profile.practical_applications.map((app, idx) => (
                    <li key={idx} className="flex items-start gap-2">
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0 mt-0.5" />
                      <span>{app}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {profile.references && profile.references.length > 0 && (
              <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment space-y-3">
                <h3 className="font-serif text-base font-bold text-navy-950 pb-2 border-b border-ivory-200">
                  Authoritative References
                </h3>
                <ul className="space-y-2 text-xs">
                  {profile.references.map((ref, idx) => (
                    <li key={idx}>
                      <a
                        href={ref.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-gold-700 hover:text-navy-950 font-medium flex items-center gap-1.5"
                      >
                        <ExternalLink className="w-3.5 h-3.5 flex-shrink-0" />
                        <span>{ref.label}</span>
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Subcategories / Related Branches */}
      {subcategories && subcategories.length > 0 && (
        <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment space-y-4">
          <h2 className="font-serif text-lg font-bold text-navy-950">
            {parent_domain ? 'Related Subcategories in This Discipline' : 'Specialized Subcategories'}
          </h2>
          <div className="flex flex-wrap gap-2.5">
            {subcategories.map((sub) => (
              <Link
                key={sub.id}
                to={`/domains/${sub.slug}`}
                className="inline-flex items-center gap-2 px-3.5 py-2 bg-ivory-50 hover:bg-gold-50 border border-ivory-300 hover:border-gold-500 rounded-xl text-xs font-medium text-navy-900 transition-all"
              >
                <span>{sub.name}</span>
                {sub.sanskrit_name && (
                  <span className="text-[11px] text-gold-700 italic">({sub.sanskrit_name})</span>
                )}
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* Connected Educational Resources */}
      <div className="space-y-6 pt-4">
        <div className="flex items-center justify-between">
          <div>
            <span className="text-xs font-mono text-gold-700 uppercase tracking-widest flex items-center gap-1.5">
              <BookOpen className="w-4 h-4" />
              <span>Repository Holdings</span>
            </span>
            <h2 className="font-serif text-2xl font-bold text-navy-950 mt-1">
              Treatises &amp; Resources in {domain.name}
            </h2>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {resources.map((res) => (
            <ResourceCard key={res.id} resource={res} viewMode="grid" />
          ))}
        </div>
      </div>
    </div>
  );
};
