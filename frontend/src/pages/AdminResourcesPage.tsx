import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  BookOpen,
  Plus,
  Edit,
  Trash2,
  CheckCircle,
  Clock,
  XCircle,
  Search,
  Filter,
  ExternalLink,
  ChevronLeft,
  ChevronRight,
  X,
  FileSpreadsheet,
  FileCode,
  FileText,
  AlertCircle
} from 'lucide-react';
import { api } from '../api/client';
import { Resource } from '../types';
import { Badge } from '../components/common/Badge';

export const AdminResourcesPage: React.FC = () => {
  const queryClient = useQueryClient();
  const [page, setPage] = useState(1);
  const [filterStatus, setFilterStatus] = useState<string>('');
  const [filterType, setFilterType] = useState<string>('');
  const [searchTerm, setSearchTerm] = useState<string>('');

  // Modals state
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [editingResource, setEditingResource] = useState<Resource | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);

  // Form State
  const initialFormState = {
    title: '',
    subtitle: '',
    description: '',
    abstract: '',
    creator: '',
    contributor: '',
    subject: '',
    language: 'Sanskrit',
    translated_language: 'English',
    resource_type: 'Manuscript',
    knowledge_domain_id: 1,
    publisher: '',
    publication_date: 'Circa 5th century CE',
    source_institution: 'Indira Gandhi National Centre for the Arts (IGNCA)',
    source_url: 'https://ignca.gov.in',
    access_url: '',
    download_url: '',
    license_id: 1,
    rights_statement: 'Public domain worldwide.',
    access_status: 'Download Available',
    file_format: 'PDF',
    file_size: '12.4 MB',
    isbn_or_identifier: '',
    keywords: 'IKS, Shastra, Sanskrit',
    citation: '',
    verification_status: 'Verified',
  };

  const [formData, setFormData] = useState(initialFormState);
  const [formError, setFormError] = useState<string | null>(null);

  // Fetch admin resources
  const { data: resourcesData, isLoading } = useQuery({
    queryKey: ['admin-resources-list', page, filterStatus, filterType],
    queryFn: () =>
      api.getAdminResources({
        page,
        page_size: 15,
        verification_status: filterStatus || undefined,
        resource_type: filterType || undefined,
      }),
  });

  // Fetch taxonomy for dropdowns
  const { data: domains } = useQuery({
    queryKey: ['admin-domains-options'],
    queryFn: () => api.getDomains(),
  });

  const { data: licenses } = useQuery({
    queryKey: ['admin-licenses-options'],
    queryFn: () => api.getLicenses(),
  });

  // Create Mutation
  const createMutation = useMutation({
    mutationFn: (data: any) => api.createResource(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin-resources-list'] });
      queryClient.invalidateQueries({ queryKey: ['admin-dashboard'] });
      setIsCreateModalOpen(false);
      setFormData(initialFormState);
    },
    onError: (err: any) => setFormError(err.message || 'Failed to create resource.'),
  });

  // Update Mutation
  const updateMutation = useMutation({
    mutationFn: ({ id, data }: { id: number; data: any }) => api.updateResource(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin-resources-list'] });
      queryClient.invalidateQueries({ queryKey: ['admin-dashboard'] });
      setEditingResource(null);
    },
    onError: (err: any) => setFormError(err.message || 'Failed to update resource.'),
  });

  // Delete Mutation
  const deleteMutation = useMutation({
    mutationFn: (id: number) => api.deleteResource(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin-resources-list'] });
      queryClient.invalidateQueries({ queryKey: ['admin-dashboard'] });
      setDeletingId(null);
    },
  });

  const handleOpenEdit = (res: Resource) => {
    setEditingResource(res);
    setFormData({
      title: res.title,
      subtitle: res.subtitle || '',
      description: res.description,
      abstract: res.abstract || '',
      creator: res.creator,
      contributor: res.contributor || '',
      subject: res.subject,
      language: res.language,
      translated_language: res.translated_language || '',
      resource_type: res.resource_type,
      knowledge_domain_id: res.knowledge_domain_id,
      publisher: res.publisher || '',
      publication_date: res.publication_date || '',
      source_institution: res.source_institution,
      source_url: res.source_url,
      access_url: res.access_url || '',
      download_url: res.download_url || '',
      license_id: res.license_id,
      rights_statement: res.rights_statement,
      access_status: res.access_status,
      file_format: res.file_format || 'PDF',
      file_size: res.file_size || '',
      isbn_or_identifier: res.isbn_or_identifier || '',
      keywords: res.keywords || '',
      citation: res.citation || '',
      verification_status: res.verification_status,
    });
    setFormError(null);
  };

  const handleSubmitForm = (e: React.FormEvent) => {
    e.preventDefault();
    setFormError(null);
    if (editingResource) {
      updateMutation.mutate({ id: editingResource.id, data: formData });
    } else {
      createMutation.mutate(formData);
    }
  };

  const filteredItems = resourcesData?.items.filter((item) => {
    if (!searchTerm.trim()) return true;
    const term = searchTerm.toLowerCase();
    return (
      item.title.toLowerCase().includes(term) ||
      item.creator.toLowerCase().includes(term) ||
      item.source_institution.toLowerCase().includes(term)
    );
  }) || [];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Page Title & Actions */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 text-xs font-mono text-gold-700 uppercase tracking-widest mb-1">
            <BookOpen className="w-4 h-4 text-gold-600" />
            <span>Catalogue Administration</span>
          </div>
          <h1 className="font-serif text-2xl sm:text-3xl font-bold text-navy-950">
            Resource Records Management
          </h1>
          <p className="text-xs text-navy-600 mt-1">
            Create, audit, edit, and export metadata for classical texts and digital treatises.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <button
            onClick={() => {
              setFormData(initialFormState);
              setFormError(null);
              setIsCreateModalOpen(true);
            }}
            className="px-4 py-2 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-sm transition-colors"
          >
            <Plus className="w-4 h-4" />
            <span>Add New Resource</span>
          </button>

          <a
            href={api.getExportUrl('csv')}
            target="_blank"
            rel="noopener noreferrer"
            className="px-3 py-2 bg-ivory-100 hover:bg-ivory-200 text-navy-800 border border-ivory-300 rounded-xl text-xs font-medium flex items-center gap-1.5 transition-colors"
          >
            <FileSpreadsheet className="w-3.5 h-3.5 text-emerald-600" />
            <span>Export CSV</span>
          </a>
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div className="bg-white border border-ivory-300 rounded-2xl p-4 shadow-sm flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center gap-2 flex-1 min-w-[220px] max-w-md">
          <div className="relative w-full">
            <Search className="w-4 h-4 text-navy-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Filter by title, author, or institution..."
              className="w-full pl-9 pr-3 py-1.5 bg-ivory-50 border border-ivory-300 rounded-lg text-xs text-navy-950 focus:outline-none focus:ring-1 focus:ring-gold-500"
            />
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <div className="flex items-center gap-1.5 text-xs text-navy-700">
            <span className="font-mono text-navy-500">Status:</span>
            <select
              value={filterStatus}
              onChange={(e) => {
                setFilterStatus(e.target.value);
                setPage(1);
              }}
              className="bg-ivory-50 border border-ivory-300 rounded-lg px-2.5 py-1 text-xs text-navy-900 focus:outline-none"
            >
              <option value="">All Statuses</option>
              <option value="Verified">Verified</option>
              <option value="Pending">Pending Audit</option>
              <option value="Rejected">Rejected</option>
            </select>
          </div>

          <div className="flex items-center gap-1.5 text-xs text-navy-700">
            <span className="font-mono text-navy-500">Type:</span>
            <select
              value={filterType}
              onChange={(e) => {
                setFilterType(e.target.value);
                setPage(1);
              }}
              className="bg-ivory-50 border border-ivory-300 rounded-lg px-2.5 py-1 text-xs text-navy-900 focus:outline-none"
            >
              <option value="">All Types</option>
              <option value="Manuscript">Manuscript</option>
              <option value="Book">Book</option>
              <option value="Critical Edition">Critical Edition</option>
              <option value="Research Paper">Research Paper</option>
            </select>
          </div>
        </div>
      </div>

      {/* Main Table */}
      <div className="bg-white border border-ivory-300 rounded-2xl shadow-parchment overflow-hidden">
        {isLoading ? (
          <div className="p-12 text-center text-xs text-navy-600">
            <div className="w-6 h-6 border-2 border-gold-500 border-t-transparent rounded-full animate-spin mx-auto mb-2" />
            Loading catalog records...
          </div>
        ) : filteredItems.length > 0 ? (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="bg-navy-950 text-ivory-200 uppercase font-mono tracking-wider border-b border-navy-900 text-[11px]">
                <tr>
                  <th className="px-4 py-3.5">ID</th>
                  <th className="px-4 py-3.5">Treatise Title & Creator</th>
                  <th className="px-4 py-3.5">Domain</th>
                  <th className="px-4 py-3.5">Access Status</th>
                  <th className="px-4 py-3.5">Audit Status</th>
                  <th className="px-4 py-3.5">Institution</th>
                  <th className="px-4 py-3.5 text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-ivory-200">
                {filteredItems.map((res) => (
                  <tr key={res.id} className="hover:bg-ivory-50/70 transition-colors">
                    <td className="px-4 py-3 font-mono text-navy-500">
                      #{res.id.toString().padStart(3, '0')}
                    </td>
                    <td className="px-4 py-3 max-w-xs">
                      <Link
                        to={`/resources/${res.id}`}
                        className="font-serif font-bold text-navy-950 hover:text-gold-700 block truncate"
                      >
                        {res.title}
                      </Link>
                      <span className="text-[11px] text-navy-600 truncate block">
                        {res.creator} • {res.language}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <span className="text-navy-700 font-medium">
                        {res.primary_domain?.name || 'IKS Discipline'}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <Badge variant="access" label={res.access_status} />
                    </td>
                    <td className="px-4 py-3">
                      <Badge variant="verification" label={res.verification_status} />
                    </td>
                    <td className="px-4 py-3 text-navy-600 truncate max-w-[140px]">
                      {res.source_institution}
                    </td>
                    <td className="px-4 py-3 text-right">
                      <div className="flex items-center justify-end gap-1.5">
                        <button
                          onClick={() => handleOpenEdit(res)}
                          title="Edit Metadata"
                          className="p-1.5 text-navy-700 hover:text-gold-700 hover:bg-ivory-100 rounded-lg transition-colors"
                        >
                          <Edit className="w-3.5 h-3.5" />
                        </button>
                        <button
                          onClick={() => setDeletingId(res.id)}
                          title="Delete Record"
                          className="p-1.5 text-rose-600 hover:text-rose-800 hover:bg-rose-50 rounded-lg transition-colors"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="p-12 text-center text-xs text-navy-500 italic">
            No resources match the selected filters.
          </div>
        )}

        {/* Pagination Bar */}
        {resourcesData && resourcesData.total_pages > 1 && (
          <div className="px-4 py-3 border-t border-ivory-200 flex items-center justify-between text-xs">
            <span className="text-navy-600 font-mono">
              Showing page {resourcesData.page} of {resourcesData.total_pages} ({resourcesData.total} records)
            </span>
            <div className="flex items-center gap-1">
              <button
                disabled={!resourcesData.has_prev}
                onClick={() => setPage((p) => Math.max(1, p - 1))}
                className="px-2.5 py-1 border border-ivory-300 rounded text-navy-800 disabled:opacity-40"
              >
                <ChevronLeft className="w-3.5 h-3.5" />
              </button>
              <button
                disabled={!resourcesData.has_next}
                onClick={() => setPage((p) => p + 1)}
                className="px-2.5 py-1 border border-ivory-300 rounded text-navy-800 disabled:opacity-40"
              >
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Create / Edit Resource Modal */}
      {(isCreateModalOpen || editingResource) && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-navy-950/70 backdrop-blur-sm overflow-y-auto">
          <div className="bg-white border border-gold-400/40 rounded-2xl max-w-3xl w-full shadow-2xl overflow-hidden my-8 max-h-[90vh] flex flex-col">
            {/* Modal Header */}
            <div className="bg-navy-900 text-ivory-50 px-6 py-4 flex items-center justify-between border-b border-gold-500/30 flex-shrink-0">
              <h3 className="font-serif text-lg font-bold">
                {editingResource ? `Edit Treatise: ${editingResource.title}` : 'Catalog New IKS Treatise'}
              </h3>
              <button
                onClick={() => {
                  setIsCreateModalOpen(false);
                  setEditingResource(null);
                }}
                className="p-1 hover:bg-navy-800 rounded-md text-ivory-300 hover:text-white"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Form */}
            <form onSubmit={handleSubmitForm} className="p-6 overflow-y-auto space-y-4 text-xs">
              {formError && (
                <div className="p-3 bg-rose-50 border border-rose-200 text-rose-800 rounded-lg flex items-center gap-2">
                  <AlertCircle className="w-4 h-4 flex-shrink-0" />
                  <span>{formError}</span>
                </div>
              )}

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="md:col-span-2">
                  <label className="block font-semibold text-navy-800 mb-1">Treatise Title *</label>
                  <input
                    type="text"
                    required
                    value={formData.title}
                    onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div className="md:col-span-2">
                  <label className="block font-semibold text-navy-800 mb-1">Subtitle</label>
                  <input
                    type="text"
                    value={formData.subtitle}
                    onChange={(e) => setFormData({ ...formData, subtitle: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Creator / Author *</label>
                  <input
                    type="text"
                    required
                    value={formData.creator}
                    onChange={(e) => setFormData({ ...formData, creator: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Contributor / Translator</label>
                  <input
                    type="text"
                    value={formData.contributor}
                    onChange={(e) => setFormData({ ...formData, contributor: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Knowledge Domain *</label>
                  <select
                    value={formData.knowledge_domain_id}
                    onChange={(e) => setFormData({ ...formData, knowledge_domain_id: Number(e.target.value) })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  >
                    {domains?.map((d) => (
                      <option key={d.id} value={d.id}>
                        {d.name} {d.sanskrit_name ? `(${d.sanskrit_name})` : ''}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Resource Type *</label>
                  <select
                    value={formData.resource_type}
                    onChange={(e) => setFormData({ ...formData, resource_type: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  >
                    <option value="Manuscript">Manuscript</option>
                    <option value="Book">Book</option>
                    <option value="Critical Edition">Critical Edition</option>
                    <option value="Research Paper">Research Paper</option>
                    <option value="Translation">Translation & Commentary</option>
                  </select>
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Original Language *</label>
                  <input
                    type="text"
                    required
                    value={formData.language}
                    onChange={(e) => setFormData({ ...formData, language: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Subject Heading *</label>
                  <input
                    type="text"
                    required
                    value={formData.subject}
                    onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div className="md:col-span-2">
                  <label className="block font-semibold text-navy-800 mb-1">Description (Dublin Core) *</label>
                  <textarea
                    rows={3}
                    required
                    value={formData.description}
                    onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Source Institution *</label>
                  <input
                    type="text"
                    required
                    value={formData.source_institution}
                    onChange={(e) => setFormData({ ...formData, source_institution: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Historical Period / Date</label>
                  <input
                    type="text"
                    value={formData.publication_date}
                    onChange={(e) => setFormData({ ...formData, publication_date: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Source URL *</label>
                  <input
                    type="url"
                    required
                    value={formData.source_url}
                    onChange={(e) => setFormData({ ...formData, source_url: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Access URL</label>
                  <input
                    type="url"
                    value={formData.access_url}
                    onChange={(e) => setFormData({ ...formData, access_url: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Legal License *</label>
                  <select
                    value={formData.license_id}
                    onChange={(e) => setFormData({ ...formData, license_id: Number(e.target.value) })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  >
                    {licenses?.map((l) => (
                      <option key={l.id} value={l.id}>
                        {l.name} ({l.identifier})
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Access & Rights Status *</label>
                  <select
                    value={formData.access_status}
                    onChange={(e) => setFormData({ ...formData, access_status: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  >
                    <option value="Open Access">Open Access</option>
                    <option value="Download Available">Download Available</option>
                    <option value="Read Online">Read Online</option>
                    <option value="Restricted Access">Restricted Access</option>
                    <option value="Metadata Only">Metadata Only</option>
                  </select>
                </div>

                <div className="md:col-span-2">
                  <label className="block font-semibold text-navy-800 mb-1">Rights Statement *</label>
                  <input
                    type="text"
                    required
                    value={formData.rights_statement}
                    onChange={(e) => setFormData({ ...formData, rights_statement: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Verification Status</label>
                  <select
                    value={formData.verification_status}
                    onChange={(e) => setFormData({ ...formData, verification_status: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50 font-semibold"
                  >
                    <option value="Verified">Verified (Publicly Visible)</option>
                    <option value="Pending">Pending Audit</option>
                    <option value="Rejected">Rejected</option>
                  </select>
                </div>

                <div>
                  <label className="block font-semibold text-navy-800 mb-1">Keywords (Comma separated)</label>
                  <input
                    type="text"
                    value={formData.keywords}
                    onChange={(e) => setFormData({ ...formData, keywords: e.target.value })}
                    className="w-full px-3 py-2 border border-ivory-300 rounded-lg bg-ivory-50"
                  />
                </div>
              </div>

              {/* Modal Footer */}
              <div className="pt-4 border-t border-ivory-200 flex items-center justify-end gap-3 flex-shrink-0">
                <button
                  type="button"
                  onClick={() => {
                    setIsCreateModalOpen(false);
                    setEditingResource(null);
                  }}
                  className="px-4 py-2 border border-ivory-300 rounded-lg text-navy-700 hover:bg-ivory-100"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={createMutation.isPending || updateMutation.isPending}
                  className="px-4 py-2 bg-navy-950 text-gold-300 font-semibold rounded-lg hover:bg-navy-900 disabled:opacity-50"
                >
                  {editingResource ? 'Update Treatise Record' : 'Save & Publish Record'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Delete Confirmation Modal */}
      {deletingId && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-navy-950/70 backdrop-blur-sm">
          <div className="bg-white border border-rose-300 rounded-2xl max-w-sm w-full p-6 shadow-2xl text-center space-y-4">
            <Trash2 className="w-10 h-10 text-rose-600 mx-auto" />
            <h3 className="font-serif text-lg font-bold text-navy-950">Confirm Deletion</h3>
            <p className="text-xs text-navy-600">
              Are you sure you want to permanently delete record #{deletingId}? This will also remove associated keyword indices.
            </p>
            <div className="flex items-center justify-center gap-3 pt-2">
              <button
                onClick={() => setDeletingId(null)}
                className="px-4 py-2 border border-ivory-300 text-navy-700 rounded-lg text-xs"
              >
                Cancel
              </button>
              <button
                onClick={() => deleteMutation.mutate(deletingId)}
                className="px-4 py-2 bg-rose-600 hover:bg-rose-700 text-white rounded-lg text-xs font-semibold"
              >
                Delete Record
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
