# System Architecture & Technical Specifications

## 1. Architectural Overview

The **Digital Repository of Selected IKS Texts and Resources** is designed as a modular, three-tier academic digital library system adhering to international archival standards (Dublin Core ISO 15836) and information retrieval principles (BM25 ranking with SQLite FTS5).

```
+-------------------------------------------------------------------------+
|                          CLIENT APPLICATION LAYER                       |
|   React 18 + TypeScript + Vite + Tailwind CSS + TanStack Query + Router  |
|                                                                         |
|  [Home Page]   [Catalogue Explorer]   [Domain Tree]   [Resource Details]|
|  [Citation]    [Admin Dashboard]      [CRUD Module]   [Review Queue]    |
+-------------------------------------------------------------------------+
                                    |
                            HTTP / REST APIs
                              (JSON / Bearer JWT)
                                    v
+-------------------------------------------------------------------------+
|                       APPLICATION & API SERVER LAYER                    |
|                         FastAPI (Python Async ASGI)                     |
|                                                                         |
|  * Routers: /resources, /search, /domains, /licenses, /auth, /admin     |
|  * Security: Argon2id Password Hashing, HS256 JWT, RBAC Middleware      |
|  * Services: ResourceService, SearchService, ExportService, AuthService |
|  * Pydantic v2: Dublin Core Validation, Filter Schema Enforcement       |
+-------------------------------------------------------------------------+
                                    |
                     SQLAlchemy 2.0 ORM & Raw FTS5
                                    v
+-------------------------------------------------------------------------+
|                          DATA & RETRIEVAL LAYER                         |
|                             SQLite 3 Database                           |
|                                                                         |
|  [Relational Tables]                 [Information Retrieval Table]       |
|  * resources                         * resources_fts (Virtual FTS5)     |
|  * knowledge_domains                 * Tokenizer: Porter + Unicode61    |
|  * licenses                          * Diacritic stripping (Level 2)    |
|  * institutions                      * Automated Sync DB Triggers       |
|  * keywords & search_history         * Column-weighted BM25 Scoring     |
+-------------------------------------------------------------------------+
```

---

## 2. Component Breakdown

### A. Frontend Layer (Single Page Application)
- **Framework**: React 18 with TypeScript 5 for strict typing of Dublin Core metadata and API contracts.
- **Build System**: Vite 5 for fast module replacement and production bundling.
- **Styling**: Tailwind CSS with custom academic palette (Deep Navy `#0B192C`, Warm Ivory `#FDFBF7`, Antique Gold `#B8860B`).
- **State Management**: TanStack Query (React Query v5) providing optimistic cache invalidation, automated refetching, and request deduplication.
- **Routing**: React Router v6 with authenticated route guards for curatorial and administrative interfaces.
- **Icons**: Lucide React for accessible semantic iconography.

### B. Application & API Layer (FastAPI)
- **ASGI Server**: High-throughput asynchronous routing using Starlette and Uvicorn.
- **Dependency Injection**: Fast session management with scoped SQLAlchemy database sessions via `Depends(get_db)`.
- **CORS Handling**: Configured origins supporting local Vite client development and production origins.
- **Dublin Core Serialization**: Dynamic assembly of the 15 standard Dublin Core elements (`dc:title`, `dc:creator`, `dc:subject`, etc.) within `ResourceService`.
- **Bibliographic Citations**: Automated citation generator providing instant formatting for APA 7th, MLA 9th, Chicago 17th, and BibTeX.
- **Rights Verification Barrier**: Strict legal evaluation on `/api/resources/{id}/download`, ensuring files are only served if the license permits redistribution and access status is open.

### C. Data & Retrieval Layer (SQLite & FTS5)
- **Relational Schema**: Normalized 3NF tables with composite indices (`knowledge_domain_id`, `access_status`, `verification_status`).
- **Full-Text Virtual Table**: Native `resources_fts` utilizing SQLite FTS5.
- **Autonomous Synchronization**: Database triggers (`trg_resources_insert`, `trg_resources_update`, `trg_resources_delete`) keep the full-text search index in lockstep with the relational table with zero background daemon overhead.
- **IAST Transliteration Support**: Tokenizer configured with `unicode61 remove_diacritics 2`, allowing users to search classical Sanskrit terms using either standard English or diacritic notation (e.g., *Aryabhatiya* matches *Āryabhaṭīya*).

---

## 3. Security & Governance Architecture
- **Authentication**: Stateless Bearer tokens signed with HMAC-SHA256 (JWT) with configurable expiration.
- **Password Protection**: Passwords salted and hashed with Argon2id (`argon2-cffi`), the winner of the Password Hashing Competition.
- **Role Separation**: Public users have read access to verified catalog items and legal downloads. Curators/Administrators have authenticated CRUD access, rights verification tools, and search analytics logs.
