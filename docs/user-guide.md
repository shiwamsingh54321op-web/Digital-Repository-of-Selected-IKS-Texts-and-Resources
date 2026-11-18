# User & Curator Guide

This guide describes how to operate both the public research interface and the curator administration console of the IKS Digital Repository.

---

## 1. Public Research Experience

### A. Searching the Archive
1. **Quick Search**: On the Home or Catalogue Explorer page, enter keywords, authors, treatise titles, or subjects into the search bar.
2. **Autocomplete**: As you type 2 or more characters, suggestions will automatically appear with classifications (`treatise`, `author`, or `keyword`).
3. **Sanskrit & IAST Transliteration**: You can enter queries in standard English or transliterated Sanskrit (e.g., typing `Aryabhata`, `Aryabhatiya`, or `Āryabhaṭa` returns the same treatise records).

### B. Faceted Filtering & Sorting
On the `/explore` page, use the left-hand faceted filters to narrow results:
- **Knowledge Domain**: Filter by any of the 12 primary domains (Mathematics, Astronomy, Ayurveda, etc.).
- **Resource Type**: Filter by `Manuscript`, `Book`, `Critical Edition`, `Translation`, or `Research Paper`.
- **Language**: Filter by `Sanskrit`, `Tamil`, `English`, etc.
- **Access Status**: Focus on `Open Access` or `Download Available`.
- **Source Institution**: Filter records preserved by specific archives like IGNCA, NDLI, or BORI.
- **Sorting**: Toggle between `Relevance` (BM25 score), `Newest Catalogued`, `Oldest`, and alphabetical (`A-Z`, `Z-A`).
- **View Toggle**: Switch between responsive Grid Cards and dense List View.

### C. Viewing Dublin Core Records
Clicking **View Record** or **Details** on any treatise card opens its full Dublin Core record:
- Review the 15 standard DCMI elements (`dc:title`, `dc:creator`, `dc:subject`, `dc:description`, `dc:rights`, etc.).
- Examine provenance information, historical era, and holding institution profile.
- View content-based related treatises.

### D. Generating Scholarly Citations
Click the **Cite** or **Generate Scholarly Citation** button on any card or detail page:
- Select from **APA 7th**, **MLA 9th**, **Chicago 17th**, or **BibTeX**.
- Click **Copy Citation** to copy the formatted text to your clipboard.

### E. Controlled Downloads
- For **Open Access** / **Public Domain** items: Click **Download Digital Resource** to retrieve the verified digital copy.
- For **Read Online** or restricted items: The download button is safely disabled, with a notification pointing to the holding archive's access portal.

---

## 2. Curator & Administrator Console

### A. Logging In
1. Navigate to `/admin/login`.
2. Enter the authorized administrative credentials:
   - **Username**: `admin`
   - **Password**: `Admin@IKS2026!`
3. Upon authentication, you will be redirected to the **Curator Control Console** (`/admin/dashboard`).

### B. Monitoring Analytics & KPI Metrics
On `/admin/dashboard`:
- View total cataloged, published, pending, and rejected records.
- Inspect distribution charts for legal rights and material formats.
- View live search logs and top queried keywords to understand user research trends.
- Use **Re-Index FTS** to rebuild the SQLite FTS5 search index if needed.

### C. Managing Resources (CRUD)
Navigate to `/admin/resources`:
- **Create**: Click **Add New Resource** to open the cataloging modal. Populate all required Dublin Core and licensing fields.
- **Edit**: Click the pencil icon on any row to modify metadata.
- **Delete**: Click the trash icon to remove an invalid record.
- **Batch Export**: Click **Export CSV**, **Export JSON**, or **Export BibTeX** to download the repository metadata.

### D. Quality Assurance & Verification Queue
Navigate to `/admin/verification`:
- Review items flagged as `Pending`.
- Check source URLs and license redistribution legality.
- Click **Approve & Verify** to publish to the public catalog, or **Reject** to withhold publication.
