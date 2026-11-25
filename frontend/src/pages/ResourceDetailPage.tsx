import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import {
  BookOpen,
  User,
  Building,
  Calendar,
  Globe,
  Download,
  Quote,
  ShieldAlert,
  ShieldCheck,
  ExternalLink,
  ChevronRight,
  FileText,
  Share2,
  Lock,
  ArrowLeft,
  CheckCircle,
  XCircle,
  Info
} from 'lucide-react';
import { api } from '../api/client';
import { Badge } from '../components/common/Badge';
import { CitationModal } from '../components/common/CitationModal';
import { ResourceCard } from '../components/resources/ResourceCard';
import { FALLBACK_RESOURCES } from '../data/fallbackData';

export const ResourceDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const resourceId = Number(id);
  const fallback = FALLBACK_RESOURCES.find((r) => r.id === resourceId);

  const [citationModalOpen, setCitationModalOpen] = useState(false);
  const [downloadError, setDownloadError] = useState<string | null>(null);
  const [isDownloading, setIsDownloading] = useState(false);

  // Fetch full details
  const { data: resource = fallback, isLoading, error } = useQuery({
    queryKey: ['resource-detail', resourceId],
    queryFn: async () => {
      try {
        return await api.getResource(resourceId);
      } catch (err) {
        if (fallback) return fallback;
        throw err;
      }
    },
    enabled: !isNaN(resourceId),
    initialData: fallback,
  });

  const handleDownload = async () => {
    setDownloadError(null);
    setIsDownloading(true);
    try {
      const res = await fetch(api.getDownloadUrl(resourceId));
      const contentType = res.headers.get('content-type') || '';
      if (!res.ok) {
        let errMessage = 'Download not permitted under current rights policy.';
        if (contentType.includes('application/json')) {
          try {
            const err = await res.json();
            if (err.detail) errMessage = err.detail;
          } catch {}
        }
        setDownloadError(errMessage);
        return;
      }
      if (contentType.includes('application/json')) {
        const data = await res.json();
        if (data.download_url) {
          window.open(data.download_url, '_blank');
          return;
        }
      }
      const fallbackUrl = resource?.download_url || resource?.access_url || resource?.source_url;
      if (fallbackUrl && (resource?.can_download ?? resource?.download_allowed)) {
        window.open(fallbackUrl, '_blank');
      } else {
        setDownloadError('Direct download is not available for this resource.');
      }
    } catch {
      const fallbackUrl = resource?.download_url || resource?.access_url || resource?.source_url;
      if (fallbackUrl && (resource?.can_download ?? resource?.download_allowed)) {
        window.open(fallbackUrl, '_blank');
      } else {
        setDownloadError('Unable to connect to download verification server.');
      }
    } finally {
      setIsDownloading(false);
    }
  };

  // Fetch citations
  const { data: citations, isLoading: citationsLoading } = useQuery({
    queryKey: ['resource-citations', resourceId],
    queryFn: async () => {
      try {
        return await api.getCitations(resourceId);
      } catch {
        if (fallback?.citations) {
          return fallback.citations as any;
        }
        throw new Error('Citations unavailable');
      }
    },
    enabled: !isNaN(resourceId),
    initialData: fallback?.citations as any,
  });

  // Fetch related resources
  const localRelated = FALLBACK_RESOURCES.filter(
    (r) => r.id !== resourceId && (!fallback || r.knowledge_domain_id === fallback.knowledge_domain_id)
  ).slice(0, 3);

  const { data: related } = useQuery({
    queryKey: ['related-resources', resourceId],
    queryFn: async () => {
      try {
        return await api.getRelatedResources(resourceId, 3);
      } catch {
        return localRelated;
      }
    },
    enabled: !isNaN(resourceId),
    initialData: localRelated,
  });

  if (isLoading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 text-center">
        <div className="w-10 h-10 border-3 border-gold-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
        <p className="font-serif text-lg text-navy-800">Loading Treatise Metadata & Dublin Core Record...</p>
      </div>
    );
  }

  if (error || !resource) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <ShieldAlert className="w-12 h-12 text-rose-500 mx-auto mb-3" />
        <h2 className="font-serif text-2xl font-bold text-navy-900">Resource Record Not Found</h2>
        <p className="text-xs text-navy-600 mt-2 mb-6">
          The requested treatise identifier ({id}) does not exist or has not yet been verified.
        </p>
        <Link
          to="/explore"
          className="inline-flex items-center gap-2 px-4 py-2 bg-navy-900 text-gold-300 rounded-lg text-xs font-medium"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Return to Catalogue</span>
        </Link>
      </div>
    );
  }

  const dc = resource.dublin_core;
  const isDownloadPermitted = Boolean(resource.can_download ?? resource.download_allowed);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Breadcrumbs */}
      <nav className="flex items-center gap-2 text-xs text-navy-600 font-mono mb-6 overflow-x-auto whitespace-nowrap pb-2">
        <Link to="/" className="hover:text-gold-700">Home</Link>
        <ChevronRight className="w-3.5 h-3.5 text-navy-400" />
        <Link to="/explore" className="hover:text-gold-700">Catalogue</Link>
        {resource.primary_domain && (
          <>
            <ChevronRight className="w-3.5 h-3.5 text-navy-400" />
            <Link to={`/explore?domain_slug=${resource.primary_domain.slug}`} className="hover:text-gold-700">
              {resource.primary_domain.name}
            </Link>
          </>
        )}
        <ChevronRight className="w-3.5 h-3.5 text-navy-400" />
        <span className="text-navy-900 font-medium truncate max-w-xs">{resource.title}</span>
      </nav>

      {/* Main Header Card */}
      <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment mb-10">
        <div className="flex flex-wrap items-center gap-2 mb-3">
          {resource.primary_domain && (
            <Badge variant="domain" label={resource.primary_domain.name} />
          )}
          <Badge variant="access" label={resource.access_status} />
          <Badge variant="type" label={resource.resource_type} />
          <Badge variant="language" label={resource.language} />
        </div>

        <h1 className="font-serif text-2xl sm:text-4xl font-bold text-navy-950 leading-tight">
          {resource.title}
        </h1>

        {resource.subtitle && (
          <p className="text-sm sm:text-base text-navy-600 italic mt-1 font-serif">
            {resource.subtitle}
          </p>
        )}

        {/* Creator & Institution Strip */}
        <div className="mt-4 pt-4 border-t border-ivory-200 flex flex-wrap items-center gap-x-6 gap-y-2 text-xs sm:text-sm text-navy-800">
          <div className="flex items-center gap-1.5">
            <User className="w-4 h-4 text-gold-600 flex-shrink-0" />
            <span className="font-semibold">{resource.creator}</span>
          </div>

          <div className="flex items-center gap-1.5">
            <Building className="w-4 h-4 text-navy-400 flex-shrink-0" />
            <span>{resource.source_institution}</span>
          </div>

          {resource.publication_date && (
            <div className="flex items-center gap-1.5 text-navy-500 font-mono text-xs">
              <Calendar className="w-3.5 h-3.5" />
              <span>Historical Era: {resource.publication_date}</span>
            </div>
          )}
        </div>

        {/* Action Buttons Toolbar */}
        <div className="mt-6 pt-6 border-t border-ivory-200 flex flex-wrap items-center gap-3">
          {/* Download / Access Button */}
          {isDownloadPermitted ? (
            <button
              onClick={handleDownload}
              disabled={isDownloading}
              className="px-4 py-2.5 bg-emerald-700 hover:bg-emerald-800 text-white rounded-xl text-xs font-semibold flex items-center gap-2 shadow-sm transition-colors disabled:opacity-50"
            >
              {isDownloading ? (
                <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
              ) : (
                <Download className="w-4 h-4" />
              )}
              <span>Download Digital Resource ({resource.file_format || 'PDF'})</span>
            </button>
          ) : (
            <button
              disabled
              title={resource.download_restriction_reason || 'Downloads restricted under current licensing terms'}
              className="px-4 py-2.5 bg-ivory-200 border border-ivory-300 text-navy-500 rounded-xl text-xs font-medium flex items-center gap-2 cursor-not-allowed"
            >
              <Lock className="w-4 h-4 text-navy-400" />
              <span>Download Restricted ({resource.access_status})</span>
            </button>
          )}

          {/* External Source / Read Online Link */}
          {resource.access_url && (
            <a
              href={resource.access_url}
              target="_blank"
              rel="noopener noreferrer"
              className="px-4 py-2.5 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-xl text-xs font-medium flex items-center gap-2 shadow-sm transition-colors"
            >
              <ExternalLink className="w-4 h-4" />
              <span>{resource.access_status === 'Read Online' ? 'Read Online at Archive' : 'View at Holding Archive'}</span>
            </a>
          )}

          {/* Citation Button */}
          <button
            onClick={() => setCitationModalOpen(true)}
            className="px-4 py-2.5 bg-white border border-ivory-300 hover:border-gold-500 text-navy-900 rounded-xl text-xs font-medium flex items-center gap-2 transition-colors shadow-2xs"
          >
            <Quote className="w-4 h-4 text-gold-600" />
            <span>Generate Scholarly Citation</span>
          </button>
        </div>

        {downloadError && (
          <div className="mt-4 p-3 bg-rose-50 border border-rose-200 rounded-xl flex items-start gap-2.5 text-xs text-rose-900">
            <Info className="w-4 h-4 text-rose-600 flex-shrink-0 mt-0.5" />
            <p>
              <span className="font-semibold">Download Access Restricted: </span>
              {downloadError}
            </p>
          </div>
        )}

        {!isDownloadPermitted && (
          <div className="mt-4 p-3 bg-amber-50/70 border border-amber-200 rounded-xl flex items-start gap-2.5 text-xs text-amber-900">
            <Info className="w-4 h-4 text-amber-600 flex-shrink-0 mt-0.5" />
            <p>
              <span className="font-semibold">Legal Redistribution Notice: </span>
              {resource.download_restriction_reason || 'File redistribution is restricted under the current license terms. Access text online via the holding institution portal.'}
            </p>
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column: Description & Dublin Core Table */}
        <div className="lg:col-span-2 space-y-8">
          {/* Abstract / Scope Description */}
          <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment">
            <h2 className="font-serif text-xl font-bold text-navy-950 mb-4 pb-2 border-b border-ivory-200">
              Description & Scholarly Scope
            </h2>
            <div className="prose text-sm text-navy-800 leading-relaxed space-y-4">
              <p>{resource.description}</p>
              {resource.abstract && (
                <div className="bg-ivory-50 border-l-4 border-gold-500 p-4 rounded-r-lg mt-4">
                  <h4 className="font-mono text-xs uppercase tracking-wider font-bold text-navy-800 mb-1">
                    Archival Abstract / Colophon Note
                  </h4>
                  <p className="text-xs text-navy-700 italic leading-relaxed">
                    {resource.abstract}
                  </p>
                </div>
              )}
            </div>

            {/* Keywords */}
            {resource.keywords && (
              <div className="mt-6 pt-4 border-t border-ivory-200">
                <span className="text-xs font-mono font-semibold text-navy-600 uppercase tracking-wider block mb-2">
                  Controlled Subject Keywords
                </span>
                <div className="flex flex-wrap gap-1.5">
                  {resource.keywords.split(',').map((kw, idx) => (
                    <Link
                      key={idx}
                      to={`/explore?q=${encodeURIComponent(kw.trim())}`}
                      className="px-2.5 py-1 bg-ivory-100 hover:bg-gold-50 text-navy-800 hover:text-gold-800 border border-ivory-300 rounded-md text-xs font-mono transition-colors"
                    >
                      #{kw.trim()}
                    </Link>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Educational Study Guide & Textual Structure */}
          {resource.educational_guide && (
            <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment space-y-6">
              <div className="flex items-center justify-between pb-3 border-b border-ivory-200">
                <div className="flex items-center gap-2">
                  <BookOpen className="w-5 h-5 text-gold-600" />
                  <h2 className="font-serif text-xl font-bold text-navy-950">
                    Educational Study Guide &amp; Textual Overview
                  </h2>
                </div>
                <span className="text-[11px] font-mono text-gold-800 bg-gold-50 px-2.5 py-0.5 rounded-full border border-gold-200">
                  Learning Module
                </span>
              </div>

              <div className="space-y-2">
                <h3 className="text-xs font-mono uppercase tracking-wider font-bold text-navy-700">
                  Subject Introduction &amp; Historical Context
                </h3>
                <p className="text-sm text-navy-800 leading-relaxed">
                  {resource.educational_guide.subject_introduction}
                </p>
                <p className="text-xs text-navy-600 leading-relaxed">
                  {resource.educational_guide.historical_context}
                </p>
              </div>

              {resource.educational_guide.learning_objectives.length > 0 && (
                <div className="bg-ivory-50 border border-ivory-200 rounded-xl p-4 space-y-2">
                  <h3 className="text-xs font-mono uppercase tracking-wider font-bold text-navy-800">
                    Key Learning Objectives
                  </h3>
                  <ul className="space-y-1.5 text-xs text-navy-700">
                    {resource.educational_guide.learning_objectives.map((obj, idx) => (
                      <li key={idx} className="flex items-start gap-2">
                        <CheckCircle className="w-3.5 h-3.5 text-emerald-600 flex-shrink-0 mt-0.5" />
                        <span>{obj}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {resource.educational_guide.chapters_and_topics.length > 0 && (
                <div className="space-y-2.5">
                  <h3 className="text-xs font-mono uppercase tracking-wider font-bold text-navy-700">
                    Chapters, Sections &amp; Core Topics
                  </h3>
                  <div className="divide-y divide-ivory-200 border border-ivory-200 rounded-xl overflow-hidden text-xs">
                    {resource.educational_guide.chapters_and_topics.map((ch, idx) => (
                      <div key={idx} className="p-3 bg-white hover:bg-ivory-50/70 transition-colors">
                        <div className="font-semibold text-navy-950">{ch.section}</div>
                        <div className="text-navy-600 mt-0.5 leading-relaxed">{ch.topics}</div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {resource.educational_guide.sanskrit_terminology.length > 0 && (
                <div className="space-y-2.5">
                  <h3 className="text-xs font-mono uppercase tracking-wider font-bold text-navy-700">
                    Key Sanskrit Terminology &amp; Definitions
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {resource.educational_guide.sanskrit_terminology.map((t, idx) => (
                      <div key={idx} className="p-3 bg-ivory-50 border border-ivory-200 rounded-lg text-xs">
                        <span className="font-serif font-bold text-navy-950 block">{t.term}</span>
                        <span className="text-navy-600 leading-relaxed">{t.meaning}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {resource.educational_guide.examples.length > 0 && (
                <div className="bg-gold-50/50 border-l-4 border-gold-500 p-4 rounded-r-lg space-y-1">
                  <h3 className="text-xs font-mono uppercase tracking-wider font-bold text-navy-800">
                    Illustrative Example from the Text
                  </h3>
                  {resource.educational_guide.examples.map((ex, idx) => (
                    <p key={idx} className="text-xs text-navy-800 leading-relaxed">{ex}</p>
                  ))}
                </div>
              )}

              {resource.educational_guide.recommended_reading.length > 0 && (
                <div className="pt-2 border-t border-ivory-200 space-y-1.5">
                  <h3 className="text-xs font-mono uppercase tracking-wider font-bold text-navy-700">
                    Recommended Academic Reading
                  </h3>
                  <ul className="list-disc list-inside space-y-1 text-xs text-navy-600">
                    {resource.educational_guide.recommended_reading.map((rec, idx) => (
                      <li key={idx}>{rec}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          {/* Full Dublin Core 15-Element Metadata Table */}
          <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment overflow-hidden">
            <div className="flex items-center justify-between pb-3 mb-4 border-b border-ivory-200">
              <div className="flex items-center gap-2">
                <ShieldCheck className="w-5 h-5 text-gold-600" />
                <h2 className="font-serif text-xl font-bold text-navy-950">
                  Dublin Core Metadata (DCMI Standard)
                </h2>
              </div>
              <span className="text-[11px] font-mono text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">
                ISO 15836 Compliant
              </span>
            </div>

            <p className="text-xs text-navy-600 mb-4 leading-relaxed">
              Standardized metadata elements following the Dublin Core Metadata Initiative principles for digital heritage curation.
            </p>

            <div className="divide-y divide-ivory-200 border border-ivory-200 rounded-xl overflow-hidden text-xs">
              {[
                { term: 'dc:title', label: 'Title', value: dc.title },
                { term: 'dc:creator', label: 'Creator / Author', value: dc.creator },
                { term: 'dc:subject', label: 'Subject', value: dc.subject },
                { term: 'dc:description', label: 'Description', value: dc.description },
                { term: 'dc:publisher', label: 'Publisher', value: dc.publisher || 'Not recorded' },
                { term: 'dc:contributor', label: 'Contributor / Editor', value: dc.contributor || 'None stated' },
                { term: 'dc:date', label: 'Date / Period', value: dc.date || 'Historical' },
                { term: 'dc:type', label: 'Resource Type', value: dc.type },
                { term: 'dc:format', label: 'Format & Size', value: dc.format || 'Application/PDF' },
                { term: 'dc:identifier', label: 'Identifier (DOI / Accession)', value: dc.identifier || `IKS-REC-${resource.id.toString().padStart(4, '0')}` },
                { term: 'dc:source', label: 'Source Provenance', value: dc.source },
                { term: 'dc:language', label: 'Language', value: dc.language },
                { term: 'dc:relation', label: 'Relation', value: dc.relation || resource.primary_domain?.name || 'Indian Knowledge Systems Collection' },
                { term: 'dc:coverage', label: 'Spatial / Temporal Coverage', value: dc.coverage || 'Ancient and Medieval India' },
                { term: 'dc:rights', label: 'Rights & Terms of Use', value: dc.rights },
              ].map((row, idx) => (
                <div key={idx} className="grid grid-cols-1 md:grid-cols-3 p-3 hover:bg-ivory-50/60 transition-colors">
                  <div className="font-mono text-navy-500 flex items-center gap-1.5 pb-1 md:pb-0">
                    <span className="font-semibold text-navy-800">{row.label}</span>
                    <span className="text-[10px] text-gold-700">({row.term})</span>
                  </div>
                  <div className="md:col-span-2 text-navy-900 leading-relaxed font-sans">
                    {row.value}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right Column: Legal Framework & Holding Archive */}
        <div className="space-y-6">
          {/* Rights & Licensing Card */}
          <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment space-y-4">
            <div className="flex items-center gap-2 pb-3 border-b border-ivory-200">
              <ShieldCheck className="w-5 h-5 text-gold-600" />
              <h3 className="font-serif text-base font-bold text-navy-950">
                Legal Rights & Permissions
              </h3>
            </div>

            <div>
              <span className="text-xs font-mono text-navy-500 uppercase tracking-wider block mb-1">
                License Classification
              </span>
              <p className="text-sm font-semibold text-navy-900">
                {resource.license?.name || 'Archival Rights Reserved'}
              </p>
              {resource.license?.identifier && (
                <span className="text-[11px] font-mono text-gold-700 bg-gold-50 px-2 py-0.5 rounded border border-gold-200 mt-1 inline-block">
                  {resource.license.identifier}
                </span>
              )}
            </div>

            {/* Permission Flags */}
            {resource.license && (
              <div className="space-y-2 pt-2 border-t border-ivory-200 text-xs">
                <div className="flex items-center justify-between">
                  <span className="text-navy-700">Commercial Reuse:</span>
                  {resource.license.commercial_use_allowed ? (
                    <span className="flex items-center gap-1 text-emerald-700 font-medium">
                      <CheckCircle className="w-3.5 h-3.5" /> Allowed
                    </span>
                  ) : (
                    <span className="flex items-center gap-1 text-rose-700 font-medium">
                      <XCircle className="w-3.5 h-3.5" /> Restricted
                    </span>
                  )}
                </div>

                <div className="flex items-center justify-between">
                  <span className="text-navy-700">Redistribution:</span>
                  {resource.license.redistribution_allowed ? (
                    <span className="flex items-center gap-1 text-emerald-700 font-medium">
                      <CheckCircle className="w-3.5 h-3.5" /> Allowed
                    </span>
                  ) : (
                    <span className="flex items-center gap-1 text-rose-700 font-medium">
                      <XCircle className="w-3.5 h-3.5" /> Restricted
                    </span>
                  )}
                </div>

                <div className="flex items-center justify-between">
                  <span className="text-navy-700">Attribution Required:</span>
                  {resource.license.attribution_required ? (
                    <span className="flex items-center gap-1 text-amber-700 font-medium">
                      <Info className="w-3.5 h-3.5" /> Yes
                    </span>
                  ) : (
                    <span className="flex items-center gap-1 text-emerald-700 font-medium">
                      <CheckCircle className="w-3.5 h-3.5" /> Public Domain
                    </span>
                  )}
                </div>
              </div>
            )}

            <div className="pt-2 border-t border-ivory-200">
              <span className="text-xs font-mono text-navy-500 uppercase tracking-wider block mb-1">
                Rights Statement
              </span>
              <p className="text-xs text-navy-700 leading-relaxed italic bg-ivory-50 p-2.5 rounded-lg border border-ivory-200">
                "{resource.rights_statement}"
              </p>
            </div>
          </div>

          {/* Holding Institution Card */}
          <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment space-y-3">
            <div className="flex items-center gap-2 pb-3 border-b border-ivory-200">
              <Building className="w-5 h-5 text-gold-600" />
              <h3 className="font-serif text-base font-bold text-navy-950">
                Source Institution
              </h3>
            </div>

            <div>
              <h4 className="text-sm font-bold text-navy-900">
                {resource.source_institution}
              </h4>
              {resource.institution_ref?.location && (
                <p className="text-xs text-navy-600 mt-0.5">
                  Location: {resource.institution_ref.location}
                </p>
              )}
            </div>

            {resource.institution_ref?.description && (
              <p className="text-xs text-navy-600 leading-relaxed">
                {resource.institution_ref.description}
              </p>
            )}

            {resource.source_url && (
              <div className="pt-2 border-t border-ivory-200">
                <a
                  href={resource.source_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-xs text-gold-700 hover:text-navy-950 font-medium flex items-center gap-1 truncate"
                >
                  <Globe className="w-3.5 h-3.5 flex-shrink-0" />
                  <span className="truncate">Archive Source Catalog Link</span>
                </a>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Related Resources Section */}
      {related && related.length > 0 && (
        <div className="mt-16 pt-12 border-t border-ivory-300">
          <div className="mb-6">
            <span className="text-xs font-mono text-gold-700 uppercase tracking-widest">
              Subject Concordance
            </span>
            <h2 className="font-serif text-2xl font-bold text-navy-950 mt-1">
              Related Treatises & Commentaries
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {related.map((item) => (
              <ResourceCard key={item.id} resource={item} viewMode="grid" />
            ))}
          </div>
        </div>
      )}

      {/* Citation Modal */}
      <CitationModal
        isOpen={citationModalOpen}
        onClose={() => setCitationModalOpen(false)}
        title={resource.title}
        citations={citations || null}
        isLoading={citationsLoading}
      />
    </div>
  );
};
