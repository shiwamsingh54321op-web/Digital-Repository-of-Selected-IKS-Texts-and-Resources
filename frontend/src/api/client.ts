import {
  Resource,
  ResourceDetail,
  PaginatedResources,
  KnowledgeDomain,
  License,
  Institution,
  SearchResponse,
  SearchSuggestionItem,
  RepositoryStatistics,
  Citations,
  AdminUser,
  AdminDashboardData,
  AdminAnalyticsData
} from '../types';

const metaEnv = (import.meta as any)?.env || {};
const API_BASE = (metaEnv.VITE_API_BASE_URL || '/api').replace(/\/+$/, '');

export class ApiError extends Error {
  status: number;
  data: any;

  constructor(status: number, message: string, data?: any) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.data = data;
  }
}

// Token helper
export const getAuthToken = (): string | null => {
  return localStorage.getItem('iks_admin_token');
};

export const setAuthToken = (token: string): void => {
  localStorage.setItem('iks_admin_token', token);
};

export const removeAuthToken = (): void => {
  localStorage.removeItem('iks_admin_token');
};

// Generic fetch wrapper
async function request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const url = `${API_BASE}${endpoint}`;
  const headers = new Headers(options.headers || {});

  if (!headers.has('Content-Type') && !(options.body instanceof FormData)) {
    headers.set('Content-Type', 'application/json');
  }

  const token = getAuthToken();
  if (token && !headers.has('Authorization')) {
    headers.set('Authorization', `Bearer ${token}`);
  }

  const config: RequestInit = {
    ...options,
    headers,
  };

  const response = await fetch(url, config);

  if (!response.ok) {
    let errorDetail = response.statusText;
    try {
      const errJson = await response.json();
      errorDetail = errJson.detail || JSON.stringify(errJson);
    } catch {
      // ignore
    }
    throw new ApiError(response.status, errorDetail);
  }

  // Handle empty responses
  if (response.status === 204) {
    return {} as T;
  }

  return response.json();
}

// Public API
export const api = {
  // System
  getHealth: () => request<{ status: string; database: string }>('/health'),
  getStatistics: () => request<RepositoryStatistics>('/statistics'),

  // Resources
  getResources: (params: {
    page?: number;
    page_size?: number;
    domain_id?: number;
    domain_slug?: string;
    resource_type?: string;
    language?: string;
    access_status?: string;
    license_id?: number;
    institution_id?: number;
    sort_by?: string;
  } = {}) => {
    const searchParams = new URLSearchParams();
    if (params.page) searchParams.set('page', params.page.toString());
    if (params.page_size) searchParams.set('page_size', params.page_size.toString());
    if (params.domain_id) searchParams.set('domain_id', params.domain_id.toString());
    if (params.domain_slug) searchParams.set('domain_slug', params.domain_slug);
    if (params.resource_type) searchParams.set('resource_type', params.resource_type);
    if (params.language) searchParams.set('language', params.language);
    if (params.access_status) searchParams.set('access_status', params.access_status);
    if (params.license_id) searchParams.set('license_id', params.license_id.toString());
    if (params.institution_id) searchParams.set('institution_id', params.institution_id.toString());
    if (params.sort_by) searchParams.set('sort_by', params.sort_by);

    const query = searchParams.toString();
    return request<PaginatedResources>(`/resources${query ? `?${query}` : ''}`);
  },

  getResource: (id: number) => request<ResourceDetail>(`/resources/${id}`),

  getRelatedResources: (id: number, limit: number = 4) =>
    request<Resource[]>(`/resources/${id}/related?limit=${limit}`),

  getCitations: (id: number) => request<Citations>(`/resources/${id}/citation`),

  getDownloadUrl: (id: number) => `${API_BASE}/resources/${id}/download`,

  // Search & Autocomplete
  search: (params: {
    q?: string;
    domain_id?: number;
    domain_slug?: string;
    resource_type?: string;
    language?: string;
    access_status?: string;
    license_id?: number;
    institution_id?: number;
    sort_by?: string;
    page?: number;
    page_size?: number;
  }) => {
    const searchParams = new URLSearchParams();
    if (params.q) searchParams.set('q', params.q);
    if (params.domain_id) searchParams.set('domain_id', params.domain_id.toString());
    if (params.domain_slug) searchParams.set('domain_slug', params.domain_slug);
    if (params.resource_type) searchParams.set('resource_type', params.resource_type);
    if (params.language) searchParams.set('language', params.language);
    if (params.access_status) searchParams.set('access_status', params.access_status);
    if (params.license_id) searchParams.set('license_id', params.license_id.toString());
    if (params.institution_id) searchParams.set('institution_id', params.institution_id.toString());
    if (params.sort_by) searchParams.set('sort_by', params.sort_by);
    if (params.page) searchParams.set('page', params.page.toString());
    if (params.page_size) searchParams.set('page_size', params.page_size.toString());

    return request<SearchResponse>(`/search?${searchParams.toString()}`);
  },

  getSuggestions: (q: string, limit: number = 8) =>
    request<SearchSuggestionItem[]>(`/search/suggestions?q=${encodeURIComponent(q)}&limit=${limit}`),

  // Taxonomy & Metadata
  getDomains: () => request<KnowledgeDomain[]>('/domains'),
  getDomain: (identifier: string | number) => request<KnowledgeDomain>(`/domains/${identifier}`),

  getLicenses: () => request<License[]>('/licenses'),
  getLicense: (id: number) => request<License>(`/licenses/${id}`),

  getInstitutions: () => request<Institution[]>('/institutions'),
  getInstitution: (id: number) => request<Institution>(`/institutions/${id}`),

  // Auth
  login: async (username: string, password: string): Promise<{ access_token: string; token_type: string }> => {
    const data = await request<{ access_token: string; token_type: string }>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    });
    setAuthToken(data.access_token);
    return data;
  },

  getMe: () => request<AdminUser>('/auth/me'),

  logout: () => {
    removeAuthToken();
  },

  // Admin Portal
  getAdminDashboard: () => request<AdminDashboardData>('/admin/dashboard'),
  getAdminAnalytics: (limit: number = 50) => request<AdminAnalyticsData>(`/admin/analytics?limit=${limit}`),

  getAdminResources: (params: {
    page?: number;
    page_size?: number;
    verification_status?: string;
    resource_type?: string;
    domain_id?: number;
  } = {}) => {
    const searchParams = new URLSearchParams();
    if (params.page) searchParams.set('page', params.page.toString());
    if (params.page_size) searchParams.set('page_size', params.page_size.toString());
    if (params.verification_status) searchParams.set('verification_status', params.verification_status);
    if (params.resource_type) searchParams.set('resource_type', params.resource_type);
    if (params.domain_id) searchParams.set('domain_id', params.domain_id.toString());
    return request<PaginatedResources>(`/admin/resources?${searchParams.toString()}`);
  },

  createResource: (data: any) => request<Resource>('/admin/resources', {
    method: 'POST',
    body: JSON.stringify(data),
  }),

  updateResource: (id: number, data: any) => request<Resource>(`/admin/resources/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  }),

  deleteResource: (id: number) => request<{ message: string }>(`/admin/resources/${id}`, {
    method: 'DELETE',
  }),

  verifyResource: (id: number, verification_status: 'Verified' | 'Pending' | 'Rejected', notes?: string) =>
    request<Resource>(`/admin/resources/${id}/verify`, {
      method: 'PUT',
      body: JSON.stringify({ verification_status, notes }),
    }),

  rebuildIndex: () => request<{ message: string }>('/admin/rebuild-index', {
    method: 'POST',
  }),

  getExportUrl: (format: 'json' | 'csv' | 'bibtex') => `${API_BASE}/admin/export/${format}`,
};
