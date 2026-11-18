import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  Shield,
  BookOpen,
  CheckCircle,
  Clock,
  XCircle,
  Layers,
  Building,
  Scale,
  RefreshCw,
  Download,
  Search,
  ArrowRight,
  TrendingUp,
  FileSpreadsheet,
  FileCode,
  FileText
} from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';

export const AdminDashboardPage: React.FC = () => {
  const { admin } = useAuth();
  const queryClient = useQueryClient();
  const [indexRebuiltMessage, setIndexRebuiltMessage] = useState<string | null>(null);

  // Fetch Dashboard Stats
  const { data: dashboard, isLoading: dashLoading } = useQuery({
    queryKey: ['admin-dashboard'],
    queryFn: () => api.getAdminDashboard(),
  });

  // Fetch Search Analytics
  const { data: analytics, isLoading: analyticsLoading } = useQuery({
    queryKey: ['admin-analytics'],
    queryFn: () => api.getAdminAnalytics(20),
  });

  // Rebuild Index Mutation
  const rebuildMutation = useMutation({
    mutationFn: () => api.rebuildIndex(),
    onSuccess: (res) => {
      setIndexRebuiltMessage(res.message || 'SQLite FTS5 full-text index successfully reconstructed.');
      queryClient.invalidateQueries({ queryKey: ['admin-dashboard'] });
      setTimeout(() => setIndexRebuiltMessage(null), 5000);
    },
  });

  if (dashLoading) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-16 text-center">
        <div className="w-8 h-8 border-2 border-gold-500 border-t-transparent rounded-full animate-spin mx-auto mb-3" />
        <p className="text-sm text-navy-800">Loading Administrator Dashboard & Analytics...</p>
      </div>
    );
  }

  const overview = dashboard?.overview;
  const distributions = dashboard?.distributions;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Top Banner */}
      <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <div className="flex items-center gap-2 text-xs font-mono text-gold-700 uppercase tracking-widest mb-1">
            <Shield className="w-4 h-4 text-gold-600" />
            <span>Curatorial Control Console</span>
          </div>
          <h1 className="font-serif text-2xl sm:text-3xl font-bold text-navy-950">
            Welcome, {admin?.username || 'Administrator'}
          </h1>
          <p className="text-xs sm:text-sm text-navy-600 mt-1">
            Overview of metadata repository health, verification statuses, and search activity.
          </p>
        </div>

        {/* Quick Actions */}
        <div className="flex flex-wrap items-center gap-2">
          <Link
            to="/admin/resources"
            className="px-4 py-2 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-sm transition-colors"
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>Manage Resources</span>
          </Link>

          <Link
            to="/admin/verification"
            className="px-4 py-2 bg-gold-50 hover:bg-gold-100 text-gold-900 border border-gold-300 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-colors"
          >
            <CheckCircle className="w-3.5 h-3.5 text-gold-700" />
            <span>Verification Queue ({overview?.pending_verification || 0})</span>
          </Link>

          <button
            onClick={() => rebuildMutation.mutate()}
            disabled={rebuildMutation.isPending}
            className="px-3 py-2 bg-ivory-100 hover:bg-ivory-200 text-navy-800 border border-ivory-300 rounded-xl text-xs font-medium flex items-center gap-1.5 transition-colors disabled:opacity-50"
            title="Rebuild SQLite FTS5 index"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${rebuildMutation.isPending ? 'animate-spin' : ''}`} />
            <span>Re-Index FTS</span>
          </button>
        </div>
      </div>

      {indexRebuiltMessage && (
        <div className="p-4 bg-emerald-50 border border-emerald-300 rounded-xl text-xs text-emerald-900 flex items-center gap-2">
          <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0" />
          <span>{indexRebuiltMessage}</span>
        </div>
      )}

      {/* KPI Overview Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-4">
        <div className="bg-white border border-ivory-300 rounded-xl p-4 text-center shadow-2xs">
          <span className="text-[11px] font-mono uppercase text-navy-500 block">Total Records</span>
          <span className="font-serif text-2xl font-bold text-navy-950 mt-1 block">
            {overview?.total_resources ?? 0}
          </span>
        </div>

        <div className="bg-white border border-emerald-200 rounded-xl p-4 text-center shadow-2xs bg-emerald-50/20">
          <span className="text-[11px] font-mono uppercase text-emerald-700 block">Published</span>
          <span className="font-serif text-2xl font-bold text-emerald-800 mt-1 block">
            {overview?.published_resources ?? 0}
          </span>
        </div>

        <div className="bg-white border border-amber-200 rounded-xl p-4 text-center shadow-2xs bg-amber-50/20">
          <span className="text-[11px] font-mono uppercase text-amber-700 block">Pending Audit</span>
          <span className="font-serif text-2xl font-bold text-amber-800 mt-1 block">
            {overview?.pending_verification ?? 0}
          </span>
        </div>

        <div className="bg-white border border-rose-200 rounded-xl p-4 text-center shadow-2xs bg-rose-50/20">
          <span className="text-[11px] font-mono uppercase text-rose-700 block">Rejected</span>
          <span className="font-serif text-2xl font-bold text-rose-800 mt-1 block">
            {overview?.rejected_resources ?? 0}
          </span>
        </div>

        <div className="bg-white border border-ivory-300 rounded-xl p-4 text-center shadow-2xs">
          <span className="text-[11px] font-mono uppercase text-navy-500 block">Domains</span>
          <span className="font-serif text-2xl font-bold text-navy-950 mt-1 block">
            {overview?.total_domains ?? 0}
          </span>
        </div>

        <div className="bg-white border border-ivory-300 rounded-xl p-4 text-center shadow-2xs">
          <span className="text-[11px] font-mono uppercase text-navy-500 block">Institutions</span>
          <span className="font-serif text-2xl font-bold text-navy-950 mt-1 block">
            {overview?.total_institutions ?? 0}
          </span>
        </div>

        <div className="bg-white border border-ivory-300 rounded-xl p-4 text-center shadow-2xs">
          <span className="text-[11px] font-mono uppercase text-navy-500 block">Licenses</span>
          <span className="font-serif text-2xl font-bold text-navy-950 mt-1 block">
            {overview?.total_licenses ?? 0}
          </span>
        </div>
      </div>

      {/* Distributions Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Access Status Distribution */}
        <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment">
          <div className="flex items-center justify-between pb-3 mb-4 border-b border-ivory-200">
            <h3 className="font-serif text-base font-bold text-navy-950">
              Access & Rights Distribution
            </h3>
            <span className="text-xs text-navy-500 font-mono">By Resource Count</span>
          </div>

          <div className="space-y-3">
            {distributions?.access_statuses &&
              Object.entries(distributions.access_statuses).map(([status, count]) => {
                const total = overview?.total_resources || 1;
                const pct = Math.round((count / total) * 100);
                return (
                  <div key={status}>
                    <div className="flex items-center justify-between text-xs font-medium text-navy-800 mb-1">
                      <span>{status}</span>
                      <span className="font-mono text-navy-500">
                        {count} ({pct}%)
                      </span>
                    </div>
                    <div className="w-full bg-ivory-200 rounded-full h-2 overflow-hidden">
                      <div
                        className="bg-gold-500 h-2 rounded-full transition-all"
                        style={{ width: `${pct}%` }}
                      />
                    </div>
                  </div>
                );
              })}
          </div>
        </div>

        {/* Resource Type Distribution */}
        <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment">
          <div className="flex items-center justify-between pb-3 mb-4 border-b border-ivory-200">
            <h3 className="font-serif text-base font-bold text-navy-950">
              Material Classification Types
            </h3>
            <span className="text-xs text-navy-500 font-mono">Bibliographic Formats</span>
          </div>

          <div className="space-y-3">
            {distributions?.resource_types &&
              Object.entries(distributions.resource_types).map(([type, count]) => {
                const total = overview?.total_resources || 1;
                const pct = Math.round((count / total) * 100);
                return (
                  <div key={type}>
                    <div className="flex items-center justify-between text-xs font-medium text-navy-800 mb-1">
                      <span>{type}</span>
                      <span className="font-mono text-navy-500">
                        {count} ({pct}%)
                      </span>
                    </div>
                    <div className="w-full bg-ivory-200 rounded-full h-2 overflow-hidden">
                      <div
                        className="bg-navy-800 h-2 rounded-full transition-all"
                        style={{ width: `${pct}%` }}
                      />
                    </div>
                  </div>
                );
              })}
          </div>
        </div>
      </div>

      {/* Export Metadata Section */}
      <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h3 className="font-serif text-base font-bold text-navy-950">
            Scholarly Batch Export Facilities
          </h3>
          <p className="text-xs text-navy-600 mt-0.5">
            Download verified Dublin Core metadata in standardized academic interchange formats.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <a
            href={api.getExportUrl('json')}
            target="_blank"
            rel="noopener noreferrer"
            className="px-3.5 py-2 bg-ivory-100 hover:bg-ivory-200 text-navy-900 border border-ivory-300 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-colors"
          >
            <FileCode className="w-4 h-4 text-gold-600" />
            <span>Export JSON</span>
          </a>

          <a
            href={api.getExportUrl('csv')}
            target="_blank"
            rel="noopener noreferrer"
            className="px-3.5 py-2 bg-ivory-100 hover:bg-ivory-200 text-navy-900 border border-ivory-300 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-colors"
          >
            <FileSpreadsheet className="w-4 h-4 text-emerald-600" />
            <span>Export CSV</span>
          </a>

          <a
            href={api.getExportUrl('bibtex')}
            target="_blank"
            rel="noopener noreferrer"
            className="px-3.5 py-2 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-colors shadow-sm"
          >
            <FileText className="w-4 h-4 text-gold-400" />
            <span>Export BibTeX</span>
          </a>
        </div>
      </div>

      {/* Search Engine Analytics & Retrieval Logs */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Top Searched Queries */}
        <div className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment">
          <div className="flex items-center gap-2 pb-3 mb-4 border-b border-ivory-200">
            <TrendingUp className="w-4 h-4 text-gold-600" />
            <h3 className="font-serif text-base font-bold text-navy-950">
              Top Search Queries
            </h3>
          </div>

          {analyticsLoading ? (
            <p className="text-xs text-navy-400">Loading queries...</p>
          ) : analytics?.top_queries && analytics.top_queries.length > 0 ? (
            <ul className="divide-y divide-ivory-100 text-xs">
              {analytics.top_queries.map((item, idx) => (
                <li key={idx} className="py-2.5 flex items-center justify-between">
                  <span className="font-medium text-navy-900">"{item.query}"</span>
                  <span className="font-mono bg-ivory-100 px-2 py-0.5 rounded text-navy-600 text-[11px]">
                    {item.count} searches
                  </span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-xs text-navy-400 italic">No search queries recorded yet.</p>
          )}
        </div>

        {/* Live Search Log Stream */}
        <div className="lg:col-span-2 bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment">
          <div className="flex items-center justify-between pb-3 mb-4 border-b border-ivory-200">
            <div className="flex items-center gap-2">
              <Search className="w-4 h-4 text-gold-600" />
              <h3 className="font-serif text-base font-bold text-navy-950">
                Recent Retrieval Log Stream
              </h3>
            </div>
            <span className="text-[11px] font-mono text-navy-500">Live BM25 Queries</span>
          </div>

          {analyticsLoading ? (
            <p className="text-xs text-navy-400">Loading log stream...</p>
          ) : analytics?.recent_searches && analytics.recent_searches.length > 0 ? (
            <div className="divide-y divide-ivory-100 max-h-72 overflow-y-auto text-xs">
              {analytics.recent_searches.map((s) => (
                <div key={s.id} className="py-2.5 flex items-center justify-between gap-4">
                  <div className="min-w-0">
                    <span className="font-medium text-navy-900 font-mono">
                      {s.query ? `"${s.query}"` : '(Catalog Facet Filter)'}
                    </span>
                    {s.filters_used && Object.keys(s.filters_used).length > 0 && (
                      <span className="text-[10px] text-navy-500 block truncate">
                        Filters: {JSON.stringify(s.filters_used)}
                      </span>
                    )}
                  </div>
                  <div className="text-right flex-shrink-0">
                    <span className="font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded text-[11px]">
                      {s.result_count} hits
                    </span>
                    <span className="text-[10px] text-navy-400 block mt-0.5">
                      {new Date(s.created_at).toLocaleTimeString()}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-navy-400 italic">No queries logged in current session.</p>
          )}
        </div>
      </div>
    </div>
  );
};
