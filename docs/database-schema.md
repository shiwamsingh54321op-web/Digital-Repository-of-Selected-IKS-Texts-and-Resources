# Database Schema Specification

The IKS Digital Repository utilizes SQLite with an architecture combining standard relational integrity and specialized full-text search indexing.

---

## 1. Entity-Relationship Overview

```
+--------------------+            +------------------------+
|  knowledge_domains |            |       resources        |
+--------------------+            +------------------------+
| id (PK)            |<---(1:N)---| id (PK)                |
| name               |            | title                  |
| slug               |            | subtitle               |
| sanskrit_name      |            | description            |
| parent_id (FK)     |            | creator                |
+--------------------+            | subject                |
                                  | language               |
+--------------------+            | resource_type          |
|      licenses      |            | knowledge_domain_id(FK)|
+--------------------+            | institution_id (FK)    |
| id (PK)            |<---(1:N)---| license_id (FK)        |
| name               |            | rights_statement       |
| identifier         |            | access_status          |
| redistribution_... |            | verification_status    |
+--------------------+            +------------------------+
                                       |              |
+--------------------+                 |              |
|    institutions    |                 |              |
+--------------------+                 |              |
| id (PK)            |<---(1:N)--------+              |
| institution_name   |                                |
| slug               |                                |
| location           |          +-------------------+ |
+--------------------+          |   resources_fts   | |
                                +-------------------+ |
                                | Virtual FTS5      |<-+ (Trigger Synced)
                                +-------------------+
```

---

## 2. Table Definitions

### A. `resources`
The central catalogue table implementing Dublin Core principles.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY | Unique resource surrogate key |
| `title` | VARCHAR(300) | NOT NULL, INDEX | Canonical treatise title (English/IAST) |
| `subtitle` | VARCHAR(300) | NULLABLE | Secondary title or commentary name |
| `description` | TEXT | NOT NULL | Scholarly overview / abstract |
| `abstract` | TEXT | NULLABLE | Archival colophon note / chapter summary |
| `creator` | VARCHAR(250) | NOT NULL, INDEX | Historical author, commentator, or editor |
| `contributor` | VARCHAR(250) | NULLABLE | Translator or editorial contributor |
| `subject` | VARCHAR(250) | NOT NULL, INDEX | Primary Dublin Core subject heading |
| `language` | VARCHAR(100) | NOT NULL, INDEX | Original language (e.g. Sanskrit) |
| `translated_language` | VARCHAR(100) | NULLABLE | Target language for translated editions |
| `resource_type` | VARCHAR(80) | NOT NULL, INDEX | Manuscript, Book, Critical Edition, Paper |
| `knowledge_domain_id` | INTEGER | FK -> knowledge_domains.id | Primary IKS domain association |
| `publisher` | VARCHAR(250) | NULLABLE | Original publisher or press |
| `publication_date` | VARCHAR(100) | NULLABLE | Historical era or publication year |
| `digitisation_date` | VARCHAR(100) | NULLABLE | Date when physical text was digitized |
| `source_institution` | VARCHAR(250) | NOT NULL, INDEX | Preserving archive or cultural foundation |
| `institution_id` | INTEGER | FK -> institutions.id | Structured link to holding institution |
| `source_url` | VARCHAR(1000) | NOT NULL | Verified source catalogue link |
| `access_url` | VARCHAR(1000) | NULLABLE | Web reading portal URL |
| `download_url` | VARCHAR(1000) | NULLABLE | Direct digital download link |
| `license_id` | INTEGER | FK -> licenses.id | Legal licensing classification |
| `rights_statement` | TEXT | NOT NULL | Explicit copyright and reuse statement |
| `access_status` | VARCHAR(80) | NOT NULL, INDEX | Open Access, Download Available, Read Online, etc. |
| `file_format` | VARCHAR(50) | NULLABLE | PDF, EPUB, Manuscript Images |
| `file_size` | VARCHAR(50) | NULLABLE | Human-readable file size (e.g., "14.2 MB") |
| `isbn_or_identifier` | VARCHAR(150) | NULLABLE, INDEX | DOI, ISBN, or manuscript accession number |
| `keywords` | TEXT | NULLABLE | Comma-delimited controlled vocabulary |
| `citation` | TEXT | NULLABLE | Pre-computed citation string |
| `verification_status` | VARCHAR(50) | NOT NULL, INDEX | Verified, Pending, Rejected |
| `created_at` | DATETIME | NOT NULL | Creation timestamp (UTC) |
| `updated_at` | DATETIME | NOT NULL | Last update timestamp (UTC) |

**Composite Indices:**
- `idx_resource_domain_status`: `(knowledge_domain_id, access_status, verification_status)`
- `idx_resource_type_lang`: `(resource_type, language)`

---

### B. `knowledge_domains`
A 2-tier hierarchical taxonomy representing the 12 primary disciplines and 40 sub-branches.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY | Unique domain identifier |
| `name` | VARCHAR(150) | NOT NULL, UNIQUE | English domain name |
| `slug` | VARCHAR(160) | NOT NULL, UNIQUE, INDEX | URL-safe slug |
| `sanskrit_name` | VARCHAR(150) | NULLABLE | Classical Sanskrit shastric name |
| `description` | TEXT | NULLABLE | Archival scope note |
| `parent_id` | INTEGER | FK -> knowledge_domains.id | NULL for primary domains; references parent for subcategories |

---

### C. `licenses`
Structured legal framework governing user permissions and download eligibility.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY | Unique license identifier |
| `name` | VARCHAR(150) | NOT NULL, UNIQUE | Full license title |
| `identifier` | VARCHAR(80) | NOT NULL, UNIQUE, INDEX | Machine-readable identifier (e.g. `cc-by-4.0`) |
| `license_url` | VARCHAR(500) | NULLABLE | Legal deed URL |
| `description` | TEXT | NOT NULL | Plain-language permissions summary |
| `permissions` | TEXT | NULLABLE | Detailed usage rights breakdown |
| `commercial_use_allowed` | BOOLEAN | NOT NULL | Commercial reuse permission |
| `redistribution_allowed` | BOOLEAN | NOT NULL | Redistribution / republication permission |
| `attribution_required` | BOOLEAN | NOT NULL | Creator credit requirement |
| `verification_notes` | TEXT | NULLABLE | Archival notes on copyright expiration |

---

### D. `institutions`
Authoritative cultural archives, libraries, and university repositories.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY | Unique institution ID |
| `institution_name` | VARCHAR(250) | NOT NULL, UNIQUE | Official archive title |
| `slug` | VARCHAR(260) | NOT NULL, UNIQUE, INDEX | URL-safe identifier |
| `location` | VARCHAR(200) | NULLABLE | City, State, Country |
| `website` | VARCHAR(500) | NULLABLE | Institutional homepage |
| `description` | TEXT | NULLABLE | Holdings overview |
| `repository_type` | VARCHAR(80) | NULLABLE | National, Academic, Cultural, Research |

---

### E. `admin_users`
Curator and administrator accounts with password protection.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY | Administrator ID |
| `username` | VARCHAR(80) | NOT NULL, UNIQUE, INDEX | Login username |
| `email` | VARCHAR(150) | NOT NULL, UNIQUE, INDEX | Registered contact email |
| `hashed_password` | VARCHAR(255) | NOT NULL | Argon2id password hash |
| `role` | VARCHAR(50) | NOT NULL | Role designation (`administrator`) |
| `is_active` | BOOLEAN | NOT NULL | Active status flag |

---

### F. `search_history`
Anonymized retrieval analytics table tracking user search queries and filter choices.

| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | PRIMARY KEY | Log entry ID |
| `query` | VARCHAR(300) | NULLABLE, INDEX | Raw user query string |
| `filters_used` | TEXT | NULLABLE | JSON-encoded filter dictionary |
| `result_count` | INTEGER | NOT NULL | Number of records matched |
| `created_at` | DATETIME | NOT NULL, INDEX | Search timestamp (UTC) |
