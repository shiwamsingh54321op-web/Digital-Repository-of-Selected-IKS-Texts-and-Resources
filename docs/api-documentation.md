# REST API Documentation

The repository exposes a RESTful API under the `/api` prefix. Interactive OpenAPI documentation is accessible at `http://127.0.0.1:8000/docs` (Swagger UI) and `http://127.0.0.1:8000/redoc`.

---

## 1. Public Endpoints

### System & Overview
- `GET /api/health`
  - Returns service status and database connectivity.
  - Response: `{"status": "online", "database": "healthy"}`
- `GET /api/statistics`
  - High-level metrics for dashboard: counts of resources, domains, institutions, licenses, and access distributions.

---

### Resources Catalogue
- `GET /api/resources`
  - **Query Parameters**:
    - `page` (int, default: 1): Page number.
    - `page_size` (int, default: 12, max: 100): Number of records per page.
    - `domain_id` (int): Filter by specific domain ID.
    - `domain_slug` (string): Filter by domain slug (e.g. `indian-mathematics`).
    - `resource_type` (string): e.g. `Manuscript`, `Book`, `Critical Edition`.
    - `language` (string): e.g. `Sanskrit`, `Tamil`, `English`.
    - `access_status` (string): e.g. `Open Access`, `Download Available`.
    - `license_id` (int): Filter by license ID.
    - `institution_id` (int): Filter by source institution ID.
    - `sort_by` (string): `newest`, `oldest`, `title_asc`, `title_desc`.
  - **Response**: Paginated object containing `items`, `total`, `page`, `page_size`, `total_pages`, `has_next`, `has_prev`.

- `GET /api/resources/{id}`
  - Returns complete metadata, full Dublin Core record (15 elements), and download eligibility.

- `GET /api/resources/{id}/related`
  - Returns related treatises based on shared domain and subject concordance.

- `GET /api/resources/{id}/citation`
  - Generates pre-formatted scholarly citations in APA 7th, MLA 9th, Chicago 17th, and BibTeX.

- `GET /api/resources/{id}/download`
  - Controlled download facility. Enforces legal licensing rights.
  - If permissions are verified and allow redistribution: Returns `{ "status": "permitted", "download_url": "..." }`.
  - If reproduction is restricted: Returns `403 Forbidden` with detailed explanation.

---

### Information Retrieval (Search)
- `GET /api/search`
  - Full-text information retrieval using SQLite FTS5 with BM25 ranking.
  - **Query Parameters**:
    - `q` (string): Free-text query (e.g., "Aryabhatiya algebra", "Sushruta surgical instruments").
    - Supports all faceted filters: `domain_slug`, `resource_type`, `language`, `access_status`, `license_id`, `institution_id`.
    - `sort_by` (string): `relevance` (default), `newest`, `oldest`, `title_asc`.
  - **Response**: `SearchResponse` with highlighted snippets and BM25 relevance scores.

- `GET /api/search/suggestions`
  - Instant autocompletion suggestions matching prefixes for titles, creators, or keywords.
  - **Query Parameters**:
    - `q` (string, min length: 2)
    - `limit` (int, default: 8)

---

### Taxonomic Directories
- `GET /api/domains` — Complete 2-tier domain tree (12 primary domains + subcategories).
- `GET /api/domains/{id_or_slug}` — Specific domain details.
- `GET /api/licenses` — 9 structured legal licenses with permission flags.
- `GET /api/institutions` — 12 partner and cultural holding archives.

---

## 2. Authentication & Admin Endpoints

### Authentication
- `POST /api/auth/login`
  - Request Body: `{"username": "admin", "password": "..."}`
  - Response: `{"access_token": "...", "token_type": "bearer"}`
- `GET /api/auth/me`
  - Headers: `Authorization: Bearer <token>`
  - Returns current admin profile.

---

### Curatorial Administration (`/api/admin/`)
*All require `Authorization: Bearer <token>`*

- `GET /api/admin/dashboard`
  - Overview counts (total, verified, pending, rejected) and distributions.
- `GET /api/admin/analytics`
  - Search query logs, top queries, and user retrieval trends.
- `GET /api/admin/resources`
  - List all resources including unverified and pending records.
- `POST /api/admin/resources`
  - Catalog new treatise record with full Dublin Core fields.
- `PUT /api/admin/resources/{id}`
  - Edit existing treatise metadata.
- `DELETE /api/admin/resources/{id}`
  - Delete resource record.
- `PUT /api/admin/resources/{id}/verify`
  - Audit workflow: Change status to `Verified`, `Pending`, or `Rejected`.
- `POST /api/admin/rebuild-index`
  - Trigger reconstruction of SQLite FTS5 virtual table.
- `GET /api/admin/export/json` — Export entire repository as JSON.
- `GET /api/admin/export/csv` — Export metadata as CSV.
- `GET /api/admin/export/bibtex` — Export records as BibTeX bibliography file.
