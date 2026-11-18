import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import {
  Layers,
  Search,
  BookOpen,
  ArrowRight,
  ChevronDown,
  ChevronRight,
  Sparkles,
  Compass
} from 'lucide-react';
import { api } from '../api/client';
import { KnowledgeDomain } from '../types';

export const DomainsPage: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [expandedDomains, setExpandedDomains] = useState<Record<number, boolean>>({});

  const { data: domains, isLoading } = useQuery({
    queryKey: ['domains-hierarchy'],
    queryFn: () => api.getDomains(),
  });

  const toggleExpand = (id: number) => {
    setExpandedDomains((prev) => ({
      ...prev,
      [id]: !prev[id],
    }));
  };

  const primaryDomains = domains?.filter((d) => !d.parent_id) || [];

  const filteredDomains = primaryDomains.filter((d) => {
    if (!searchTerm.trim()) return true;
    const term = searchTerm.toLowerCase();
    const matchesName = d.name.toLowerCase().includes(term);
    const matchesSanskrit = d.sanskrit_name?.toLowerCase().includes(term);
    const matchesDesc = d.description?.toLowerCase().includes(term);
    const matchesSub = d.subcategories?.some(
      (sub) => sub.name.toLowerCase().includes(term) || sub.sanskrit_name?.toLowerCase().includes(term)
    );
    return matchesName || matchesSanskrit || matchesDesc || matchesSub;
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      {/* Header */}
      <div className="max-w-3xl mb-10">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gold-100 border border-gold-300 text-gold-800 text-xs font-mono uppercase tracking-widest mb-3">
          <Layers className="w-3.5 h-3.5" />
          <span>Taxonomic Hierarchy</span>
        </div>
        <h1 className="font-serif text-3xl sm:text-4xl font-bold text-navy-950">
          Knowledge Domains of Indian Civilization
        </h1>
        <p className="text-sm text-navy-600 mt-2 leading-relaxed">
          The repository organizes Indian intellectual heritage into 12 primary disciplines and over 40 specialized subcategories, combining traditional Sanskrit shastric taxonomy with modern metadata classification.
        </p>

        {/* Filter Input */}
        <div className="mt-6 relative max-w-md">
          <Search className="w-4 h-4 text-gold-600 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search domains or subcategories (e.g. Ganita, Vrikshayurveda)..."
            className="w-full pl-10 pr-4 py-2.5 bg-white border border-ivory-300 rounded-lg text-sm text-navy-950 placeholder-navy-400 focus:outline-none focus:ring-2 focus:ring-gold-500/40 shadow-sm"
          />
        </div>
      </div>

      {/* Grid of Domains */}
      {isLoading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div key={i} className="bg-white border border-ivory-200 rounded-xl p-6 h-64 animate-pulse" />
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {filteredDomains.map((domain) => {
            const isExpanded = expandedDomains[domain.id] ?? true; // default open
            return (
              <div
                key={domain.id}
                className="bg-white border border-ivory-300 rounded-xl overflow-hidden shadow-parchment hover:border-gold-400 transition-all"
              >
                {/* Domain Header */}
                <div className="p-6 bg-gradient-to-r from-ivory-50 to-white border-b border-ivory-200">
                  <div className="flex items-start justify-between gap-4">
                    <div>
                      <div className="flex items-center gap-2 mb-1">
                        <span className="font-mono text-xs font-semibold text-gold-700 bg-gold-50 px-2 py-0.5 rounded border border-gold-200">
                          {domain.sanskrit_name || 'Traditional Field'}
                        </span>
                        <span className="text-[11px] text-navy-500 font-mono">
                          {domain.subcategories?.length || 0} subcategories
                        </span>
                      </div>
                      <h2 className="font-serif text-xl font-bold text-navy-950">
                        {domain.name}
                      </h2>
                    </div>

                    <Link
                      to={`/explore?domain_slug=${domain.slug}`}
                      className="px-3 py-1.5 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-lg text-xs font-medium transition-colors flex items-center gap-1.5 shadow-sm flex-shrink-0"
                    >
                      <Compass className="w-3.5 h-3.5" />
                      <span>Explore</span>
                    </Link>
                  </div>

                  <p className="text-xs text-navy-600 mt-3 leading-relaxed">
                    {domain.description}
                  </p>
                </div>

                {/* Subcategories Accordion / List */}
                <div className="p-5 bg-ivory-50/50">
                  <div className="flex items-center justify-between mb-3 text-xs font-mono font-semibold uppercase tracking-wider text-navy-600">
                    <span>Specialized Sub-branches</span>
                    <button
                      onClick={() => toggleExpand(domain.id)}
                      className="text-gold-700 hover:text-navy-900 flex items-center gap-1 font-sans capitalize"
                    >
                      {isExpanded ? 'Collapse' : 'Expand'}
                      {isExpanded ? <ChevronDown className="w-3.5 h-3.5" /> : <ChevronRight className="w-3.5 h-3.5" />}
                    </button>
                  </div>

                  {isExpanded && (
                    <div className="flex flex-wrap gap-2">
                      {domain.subcategories && domain.subcategories.length > 0 ? (
                        domain.subcategories.map((sub) => (
                          <Link
                            key={sub.id}
                            to={`/explore?domain_slug=${sub.slug}`}
                            className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-white border border-ivory-300 hover:border-gold-500 hover:bg-gold-50/60 rounded-lg text-xs text-navy-800 font-medium transition-all group shadow-2xs"
                          >
                            <span className="group-hover:text-gold-800 transition-colors">
                              {sub.name}
                            </span>
                            {sub.sanskrit_name && (
                              <span className="text-[10px] text-gold-600 italic">
                                ({sub.sanskrit_name})
                              </span>
                            )}
                            <ArrowRight className="w-3 h-3 text-navy-400 group-hover:text-gold-700 group-hover:translate-x-0.5 transition-all" />
                          </Link>
                        ))
                      ) : (
                        <span className="text-xs text-navy-400 italic">No subcategories catalogued.</span>
                      )}
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
