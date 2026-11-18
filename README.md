# Digital Repository of Selected IKS Texts and Resources

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/Frontend-React_18_%2B_TypeScript-61DAFB.svg?logo=react)](https://react.dev)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind_CSS-38B2AC.svg?logo=tailwind-css)](https://tailwindcss.com)
[![SQLite FTS5](https://img.shields.io/badge/Search-SQLite_FTS5_%2B_BM25-003B57.svg?logo=sqlite)](https://www.sqlite.org/fts5.html)
[![Dublin Core](https://img.shields.io/badge/Metadata-Dublin_Core_ISO_15836-B8860B.svg)](https://www.dublincore.org)

An academic-grade digital library and information retrieval prototype dedicated to the **Indian Knowledge Systems (IKS)**. Engineered to categorize, index, search, and legally govern classical Indian texts, manuscripts, translations, and research resources following **Dublin Core ISO 15836** metadata standards and **SQLite FTS5 BM25** probabilistic ranking.

---

## Academic Assignment Mandate

> *"Build a prototype repository with metadata, categorisation, search, and retrieval facilities for legally usable/open IKS resources."*

This repository satisfies all three core engineering disciplines:
1. **Database Architecture**: Normalized SQLite relational schema, composite indices, and Alembic migrations.
2. **Information Retrieval (IR)**: SQLite FTS5 virtual table, Porter stemmer, Unicode61 diacritic stripping, column-weighted BM25 relevance scoring, and query analytics.
3. **Web Development**: Single Page Application built in React 18, TypeScript, Tailwind CSS, TanStack Query, and an asynchronous REST API in FastAPI.

---

## Key Features

- **Standardized Dublin Core Metadata**: Every record implements the 15 standard DCMI elements (`title`, `creator`, `subject`, `description`, `publisher`, `contributor`, `date`, `type`, `format`, `identifier`, `source`, `language`, `relation`, `coverage`, `rights`).
- **52 Taxonomic Knowledge Domains**: 12 primary disciplines (*Ganita*, *Jyotisha*, *Ayurveda*, *Darshana*, *Dhatuvada*, *Vyakarana*, *Vastu*, *Krishi*, etc.) and 40+ specialized subcategories.
- **32 Verified Canonical IKS Treatises**: Seeded records including the *Aryabhatiya*, *Brahmasphutasiddhanta*, *Baudhayana Sulba Sutra*, *Charaka Samhita*, *Sushruta Samhita*, *Patanjali Yoga Sutras*, *Arthashastra*, *Natyashastra*, and more.
- **Full-Text BM25 Information Retrieval**: Sub-millisecond keyword and phrase queries, live prefix autocomplete suggestions, and Sanskrit IAST transliteration tolerance (e.g. `Aryabhata` matches `Āryabhaṭa`).
- **Legal Rights & Controlled Downloads**: Strict differentiation between Open Access, Public Domain, Creative Commons, and In-Copyright works. Unauthorized downloads are blocked via 403 Forbidden checks, preserving research access while respecting intellectual property.
- **Scholarly Citation Generator**: One-click citation formatting in **APA 7th**, **MLA 9th**, **Chicago 17th**, and **BibTeX**.
- **Curator & Admin Portal**: Role-based authentication (Argon2id + JWT), live analytics, search logs, full resource CRUD, and curatorial verification queue.
- **Metadata Export**: Instant batch exports of the repository catalogue in **JSON**, **CSV**, and **BibTeX**.

---

## Technology Stack

| Domain | Technologies |
| :--- | :--- |
| **Backend API** | FastAPI, Python 3.10+, Uvicorn ASGI, Pydantic v2 |
| **Database & ORM** | SQLite 3, SQLAlchemy 2.0, Alembic |
| **Search Engine** | SQLite FTS5, Okapi BM25 ranking, Unicode61 Tokenizer |
| **Security & Auth** | Argon2id (`argon2-cffi`), PyJWT (HS256) |
| **Frontend SPA** | React 18, TypeScript 5, Vite 5, Tailwind CSS |
| **Data Fetching** | TanStack Query v5 (React Query), React Router v6 |
| **Icons & UI** | Lucide React, Google Fonts (*Cinzel*, *Merriweather*, *Plus Jakarta Sans*) |

---

## Directory Structure

```
iks-digital-repository/
├── backend/
│   ├── alembic/                 # Alembic DB migration framework
│   ├── app/
│   │   ├── api/routes/          # FastAPI routers (resources, search, auth, admin, etc.)
│   │   ├── core/config.py       # Pydantic environment configuration
│   │   ├── database/session.py  # SQLAlchemy engine & session maker
│   │   ├── models/              # SQLAlchemy models (Resource, Domain, License, etc.)
│   │   ├── repositories/        # Database query abstractions
│   │   ├── schemas/             # Pydantic validation & Dublin Core schemas
│   │   ├── search/engine.py     # SQLite FTS5 virtual table & BM25 logic
│   │   ├── security/            # Argon2 password hashing & JWT token dependencies
│   │   ├── services/            # Citation, resource, search, and export services
│   │   └── main.py              # Application entrypoint & CORS setup
│   ├── scripts/seed_data.py     # Comprehensive seed data script (32 treatises, 52 domains)
│   ├── tests/                   # Pytest test suite (database, search, API, auth)
│   ├── requirements.txt         # Python dependencies
│   └── iks_repository.db        # Pre-seeded SQLite database file
├── frontend/
│   ├── src/
│   │   ├── api/client.ts        # Typed API client with token management
│   │   ├── components/          # Reusable UI components (Navbar, Footer, SearchBar, Cards)
│   │   ├── context/AuthContext  # React authentication state context
│   │   ├── pages/               # Application views (Home, Explore, Domains, Details, Admin)
│   │   ├── types/               # TypeScript definitions matching backend schemas
│   │   ├── App.tsx              # React router configuration
│   │   └── main.tsx             # Application bootstrap
│   ├── index.html               # Main HTML template
│   ├── package.json             # NPM dependencies
│   ├── tailwind.config.js       # Academic theme styling configuration
│   └── vite.config.ts           # Vite build & API proxy setup
└── docs/                        # Complete technical documentation
    ├── architecture.md          # 3-tier system architecture
    ├── database-schema.md       # Relational & FTS5 schema specifications
    ├── api-documentation.md     # REST API reference
    ├── search-engine.md         # BM25 & FTS5 search engine details
    ├── resource-licensing.md    # Legal rights & download governance framework
    └── user-guide.md            # User and curator guide
```

---

## Installation & Setup

### Prerequisites
- **Python 3.10+** (Tested on Python 3.10 through 3.14)
- **Node.js 18+** and **npm**

---

### 1. Backend Setup

```bash
# Navigate to the backend directory
cd backend

# (Optional) Create and activate a virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run the database seeding script (initializes FTS5 index & creates default admin)
python scripts/seed_data.py
```

### 2. Frontend Setup

```bash
# Navigate to the frontend directory
cd ../frontend

# Install dependencies
npm install

# Build production bundle
npm run build
```

---

## Running the Application

### Start the Backend Server (Port 8000)
```bash
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The FastAPI backend and interactive documentation will be live at:
- **API Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Health Endpoint**: [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

### Start the Frontend Dev Server (Port 5173)
```bash
cd frontend
npm run dev
```
Open your browser and navigate to:
- **Repository Web Portal**: [http://localhost:5173](http://localhost:5173)

---

## Default Administrative Credentials

The database comes pre-configured with a default administrator account:
- **Username**: `admin`
- **Password**: `Admin@IKS2026!`
- **Role**: `administrator`

Login via the web portal at [http://localhost:5173/admin/login](http://localhost:5173/admin/login) to access the Curator Console, edit Dublin Core records, audit pending treatises, and export metadata.

---

## Running Automated Tests

Run the backend test suite:
```bash
cd backend
pytest tests/test_database.py tests/test_search.py
```

---

## License & Attribution

- Built for academic research, cultural preservation, and institutional review.
- Treatises and metadata are curated from open institutional repositories: IGNCA, National Digital Library of India (NDLI), Bhandarkar Oriental Research Institute (BORI), INSA, and Rare Book Society of India.
- Released under the MIT License. See [LICENSE](file:///LICENSE) for details.
