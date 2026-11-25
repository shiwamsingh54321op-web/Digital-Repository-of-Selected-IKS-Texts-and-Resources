import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, User, Building, Quote, ExternalLink, Download, ShieldCheck } from 'lucide-react';
import { Resource } from '../../types';
import { Badge } from '../common/Badge';
import { CitationModal } from '../common/CitationModal';
import { api } from '../../api/client';

interface ResourceCardProps {
  resource: Resource;
  viewMode?: 'grid' | 'list';
}

export const ResourceCard: React.FC<ResourceCardProps> = ({
  resource,
  viewMode = 'grid',
}) => {
  const [citationModalOpen, setCitationModalOpen] = useState(false);
  const [citations, setCitations] = useState<any>(null);
  const [isLoadingCitation, setIsLoadingCitation] = useState(false);

  const handleOpenCitation = async (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setCitationModalOpen(true);
    if (!citations) {
      setIsLoadingCitation(true);
      try {
        const data = await api.getCitations(resource.id);
        setCitations(data);
      } catch {
        const year = resource.publication_date || 'n.d.';
        const url = resource.source_url || window.location.origin;
        setCitations({
          apa: `${resource.creator}. (${year}). ${resource.title}. ${resource.source_institution}. ${url}`,
          mla: `${resource.creator}. "${resource.title}." ${resource.source_institution}, ${year}, ${url}.`,
          chicago: `${resource.creator}. ${resource.title}. ${resource.source_institution}, ${year}. ${url}.`,
          bibtex: `@misc{iks_${resource.id},\n  author = {${resource.creator}},\n  title = {${resource.title}},\n  year = {${year}},\n  publisher = {${resource.source_institution}},\n  url = {${url}},\n  note = {Accessed via IKS Digital Repository}\n}`,
        });
      } finally {
        setIsLoadingCitation(false);
      }
    }
  };

  const isDownloadable = resource.access_status === 'Download Available' || resource.access_status === 'Open Access';

  if (viewMode === 'list') {
    return (
      <>
        <div className="bg-white border border-ivory-300 rounded-xl p-5 hover:border-gold-400 hover:shadow-parchment-lg transition-all duration-200 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="flex-1 min-w-0">
            <div className="flex flex-wrap items-center gap-2 mb-2">
              {resource.primary_domain && (
                <Badge variant="domain" label={resource.primary_domain.name} />
              )}
              <Badge variant="access" label={resource.access_status} />
              <span className="text-xs text-navy-600 font-mono">
                {resource.resource_type} • {resource.language}
              </span>
            </div>

            <Link
              to={`/resources/${resource.id}`}
              className="block group"
            >
              <h3 className="font-serif text-lg font-bold text-navy-950 group-hover:text-gold-700 transition-colors leading-snug">
                {resource.title}
              </h3>
            </Link>

            {resource.subtitle && (
              <p className="text-xs text-navy-600 italic mt-0.5">{resource.subtitle}</p>
            )}

            <div className="flex flex-wrap items-center gap-x-4 gap-y-1 mt-2 text-xs text-navy-700">
              <span className="flex items-center gap-1">
                <User className="w-3.5 h-3.5 text-gold-600" />
                <span className="font-medium">{resource.creator}</span>
              </span>
              <span className="flex items-center gap-1">
                <Building className="w-3.5 h-3.5 text-navy-400" />
                <span>{resource.source_institution}</span>
              </span>
              {resource.publication_date && (
                <span className="text-navy-500">
                  Era: {resource.publication_date}
                </span>
              )}
            </div>

            <p className="text-xs text-navy-600 line-clamp-2 mt-2 leading-relaxed">
              {resource.description}
            </p>
          </div>

          {/* Action Buttons */}
          <div className="flex flex-row md:flex-col items-center md:items-end justify-between md:justify-center gap-2 pt-3 md:pt-0 border-t md:border-t-0 border-ivory-200 flex-shrink-0">
            <Link
              to={`/resources/${resource.id}`}
              className="px-3.5 py-1.5 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 shadow-sm"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>View Record</span>
            </Link>

            <button
              onClick={handleOpenCitation}
              className="px-3 py-1.5 bg-ivory-100 hover:bg-ivory-200 text-navy-800 border border-ivory-300 rounded-lg text-xs font-medium transition-colors flex items-center gap-1"
            >
              <Quote className="w-3 h-3 text-gold-600" />
              <span>Cite</span>
            </button>
          </div>
        </div>

        <CitationModal
          isOpen={citationModalOpen}
          onClose={() => setCitationModalOpen(false)}
          title={resource.title}
          citations={citations}
          isLoading={isLoadingCitation}
        />
      </>
    );
  }

  // Grid Card View
  return (
    <>
      <div className="bg-white border border-ivory-300 rounded-xl overflow-hidden hover:border-gold-400 hover:shadow-parchment-lg transition-all duration-200 flex flex-col h-full group">
        {/* Top Header Strip */}
        <div className="bg-ivory-100/70 border-b border-ivory-200 px-4 py-2.5 flex items-center justify-between gap-2">
          {resource.primary_domain ? (
            <span className="text-xs font-medium text-gold-700 truncate max-w-[170px]" title={resource.primary_domain.name}>
              {resource.primary_domain.name}
            </span>
          ) : (
            <span className="text-xs font-medium text-navy-600">IKS Repository</span>
          )}
          <Badge variant="access" label={resource.access_status} />
        </div>

        {/* Card Body */}
        <div className="p-5 flex-1 flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 text-[11px] text-navy-600 font-mono mb-1.5 uppercase tracking-wider">
              <span>{resource.resource_type}</span>
              <span>•</span>
              <span>{resource.language}</span>
            </div>

            <Link to={`/resources/${resource.id}`} className="block">
              <h3 className="font-serif text-base font-bold text-navy-950 group-hover:text-gold-700 transition-colors line-clamp-2 leading-snug">
                {resource.title}
              </h3>
            </Link>

            {resource.subtitle && (
              <p className="text-xs text-navy-600 italic mt-1 line-clamp-1">
                {resource.subtitle}
              </p>
            )}

            <div className="mt-3 flex items-center gap-1.5 text-xs text-navy-800 font-medium">
              <User className="w-3.5 h-3.5 text-gold-600 flex-shrink-0" />
              <span className="truncate">{resource.creator}</span>
            </div>

            <div className="mt-1 flex items-center gap-1.5 text-xs text-navy-600">
              <Building className="w-3.5 h-3.5 text-navy-400 flex-shrink-0" />
              <span className="truncate">{resource.source_institution}</span>
            </div>

            <p className="text-xs text-navy-600 mt-3 line-clamp-3 leading-relaxed">
              {resource.description}
            </p>
          </div>

          {/* Footer Metadata & Actions */}
          <div className="mt-5 pt-4 border-t border-ivory-200 flex items-center justify-between gap-2">
            <span className="text-[11px] text-navy-600 truncate max-w-[120px]" title={resource.license?.name || resource.rights_statement}>
              {resource.license?.name || 'Verified Rights'}
            </span>

            <div className="flex items-center gap-1.5">
              <button
                onClick={handleOpenCitation}
                title="Generate Citation"
                className="p-1.5 text-navy-600 hover:text-navy-950 hover:bg-ivory-100 rounded-lg transition-colors border border-transparent hover:border-ivory-300"
              >
                <Quote className="w-4 h-4 text-gold-600" />
              </button>

              <Link
                to={`/resources/${resource.id}`}
                className="px-3 py-1.5 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-lg text-xs font-medium transition-colors flex items-center gap-1 shadow-sm"
              >
                <span>Details</span>
                <BookOpen className="w-3 h-3" />
              </Link>
            </div>
          </div>
        </div>
      </div>

      <CitationModal
        isOpen={citationModalOpen}
        onClose={() => setCitationModalOpen(false)}
        title={resource.title}
        citations={citations}
        isLoading={isLoadingCitation}
      />
    </>
  );
};
