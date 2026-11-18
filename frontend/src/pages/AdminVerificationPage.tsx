import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  ShieldCheck,
  CheckCircle,
  XCircle,
  Clock,
  ExternalLink,
  AlertTriangle,
  FileText,
  Search,
  Filter,
  Info
} from 'lucide-react';
import { api } from '../api/client';
import { Resource } from '../types';
import { Badge } from '../components/common/Badge';

export const AdminVerificationPage: React.FC = () => {
  const queryClient = useQueryClient();
  const [filterStatus, setFilterStatus] = useState<string>('Pending');
  const [searchTerm, setSearchTerm] = useState<string>('');

  // Fetch admin resources for verification
  const { data: resourcesData, isLoading } = useQuery({
    queryKey: ['admin-verification-list', filterStatus],
    queryFn: () =>
      api.getAdminResources({
        page: 1,
        page_size: 50,
        verification_status: filterStatus || undefined,
      }),
  });

  // Verify mutation
  const verifyMutation = useMutation({
    mutationFn: ({ id, status, notes }: { id: number; status: 'Verified' | 'Pending' | 'Rejected'; notes?: string }) =>
      api.verifyResource(id, status, notes),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin-verification-list'] });
      queryClient.invalidateQueries({ queryKey: ['admin-dashboard'] });
      queryClient.invalidateQueries({ queryKey: ['admin-resources-list'] });
    },
  });

  const items = resourcesData?.items || [];
  const filtered = items.filter((item) => {
    if (!searchTerm.trim()) return true;
    const term = searchTerm.toLowerCase();
    return item.title.toLowerCase().includes(term) || item.creator.toLowerCase().includes(term);
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Header */}
      <div>
        <div className="flex items-center gap-2 text-xs font-mono text-gold-700 uppercase tracking-widest mb-1">
          <ShieldCheck className="w-4 h-4 text-gold-600" />
          <span>Curatorial Quality Assurance</span>
        </div>
        <h1 className="font-serif text-2xl sm:text-3xl font-bold text-navy-950">
          Metadata & Resource Verification
        </h1>
        <p className="text-xs sm:text-sm text-navy-600 mt-1">
          Scholarly review queue to verify source provenance, Dublin Core completeness, and copyright/licensing legality.
        </p>
      </div>

      {/* Filter Tabs */}
      <div className="flex flex-wrap items-center justify-between gap-4 bg-white border border-ivory-300 rounded-2xl p-4 shadow-sm">
        <div className="flex items-center gap-2">
          {(['Pending', 'Verified', 'Rejected', ''] as const).map((status) => (
            <button
              key={status}
              onClick={() => setFilterStatus(status)}
              className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                filterStatus === status
                  ? 'bg-navy-950 text-gold-300'
                  : 'bg-ivory-100 text-navy-700 hover:bg-ivory-200'
              }`}
            >
              {status ? status : 'All Records'}
            </button>
          ))}
        </div>

        <div className="relative w-64">
          <Search className="w-3.5 h-3.5 text-navy-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search treatises..."
            className="w-full pl-8 pr-3 py-1.5 bg-ivory-50 border border-ivory-300 rounded-lg text-xs text-navy-950 focus:outline-none"
          />
        </div>
      </div>

      {/* Review Queue Cards */}
      {isLoading ? (
        <div className="p-12 text-center text-xs text-navy-600">
          <div className="w-6 h-6 border-2 border-gold-500 border-t-transparent rounded-full animate-spin mx-auto mb-2" />
          Loading verification audit queue...
        </div>
      ) : filtered.length > 0 ? (
        <div className="space-y-4">
          {filtered.map((res) => (
            <div
              key={res.id}
              className="bg-white border border-ivory-300 rounded-2xl p-6 shadow-parchment hover:border-gold-400 transition-all"
            >
              <div className="flex flex-col md:flex-row md:items-start justify-between gap-4">
                <div className="space-y-2 flex-1">
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="font-mono text-xs font-bold text-navy-500">
                      #{res.id.toString().padStart(3, '0')}
                    </span>
                    <Badge variant="verification" label={res.verification_status} />
                    <Badge variant="access" label={res.access_status} />
                    <span className="text-xs text-navy-600 font-mono">
                      {res.resource_type} • {res.language}
                    </span>
                  </div>

                  <h3 className="font-serif text-lg font-bold text-navy-950">
                    {res.title}
                  </h3>

                  <div className="text-xs text-navy-700 space-x-4">
                    <span className="font-medium">Author: {res.creator}</span>
                    <span>Institution: {res.source_institution}</span>
                    {res.publication_date && <span>Period: {res.publication_date}</span>}
                  </div>

                  <p className="text-xs text-navy-600 line-clamp-2 leading-relaxed">
                    {res.description}
                  </p>

                  <div className="pt-2 flex flex-wrap items-center gap-4 text-xs text-navy-500 font-mono">
                    <span>License: <strong className="text-navy-800">{res.license?.name || 'Standard License'}</strong></span>
                    {res.source_url && (
                      <a
                        href={res.source_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-gold-700 hover:text-navy-950 underline flex items-center gap-1"
                      >
                        <span>Verify Source Link</span>
                        <ExternalLink className="w-3 h-3" />
                      </a>
                    )}
                  </div>
                </div>

                {/* Audit Verification Actions */}
                <div className="flex flex-col sm:flex-row md:flex-col gap-2 flex-shrink-0 pt-4 md:pt-0 border-t md:border-t-0 border-ivory-200">
                  <button
                    onClick={() => verifyMutation.mutate({ id: res.id, status: 'Verified', notes: 'Approved by academic curator.' })}
                    disabled={res.verification_status === 'Verified' || verifyMutation.isPending}
                    className="px-4 py-2 bg-emerald-700 hover:bg-emerald-800 text-white rounded-lg text-xs font-medium flex items-center gap-1.5 transition-colors disabled:opacity-40 disabled:cursor-not-allowed shadow-sm"
                  >
                    <CheckCircle className="w-3.5 h-3.5" />
                    <span>Approve & Verify</span>
                  </button>

                  <button
                    onClick={() => verifyMutation.mutate({ id: res.id, status: 'Rejected', notes: 'Rights unverified or metadata insufficient.' })}
                    disabled={res.verification_status === 'Rejected' || verifyMutation.isPending}
                    className="px-4 py-2 bg-rose-50 hover:bg-rose-100 text-rose-700 border border-rose-200 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
                  >
                    <XCircle className="w-3.5 h-3.5" />
                    <span>Reject Record</span>
                  </button>

                  <button
                    onClick={() => verifyMutation.mutate({ id: res.id, status: 'Pending', notes: 'Awaiting further bibliographic check.' })}
                    disabled={res.verification_status === 'Pending' || verifyMutation.isPending}
                    className="px-4 py-2 bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 rounded-lg text-xs font-medium flex items-center gap-1.5 transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
                  >
                    <Clock className="w-3.5 h-3.5" />
                    <span>Mark as Pending</span>
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="bg-white border border-ivory-300 rounded-2xl p-12 text-center shadow-sm">
          <CheckCircle className="w-10 h-10 text-emerald-600 mx-auto mb-2" />
          <h3 className="font-serif text-base font-bold text-navy-950">
            No Records in this Verification State
          </h3>
          <p className="text-xs text-navy-500 mt-1">
            All records currently have been audited or match other filter criteria.
          </p>
        </div>
      )}
    </div>
  );
};
