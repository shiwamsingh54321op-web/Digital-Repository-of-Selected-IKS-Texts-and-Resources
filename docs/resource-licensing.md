# Resource Licensing & Legal Governance Framework

## 1. Compliance Mandate

A central requirement of the academic assignment is:
> "Build a prototype repository with metadata, categorisation, search, and retrieval facilities for legally usable/open IKS resources."

The repository enforces legal rights through:
1. **Never conflating free web viewing with permission to redistribute files.**
2. **Never treating academic fair use as an open license.**
3. **Marking uncertain or restricted rights as `Read Online` or `Rights Unverified`.**
4. **Disabling unauthorized file downloads on restricted materials while preserving complete Dublin Core metadata.**
5. **Preserving original institutional provenance and attribution.**

---

## 2. Supported License Classifications

| License Name | Identifier | Commercial Reuse | File Redistribution | Attribution Required | Verification & Legal Scope |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Public Domain Mark 1.0** | `public-domain` | Yes | Yes | No | Works with expired copyright worldwide published prior to 1928 (e.g. 19th-century critical editions). |
| **Creative Commons Zero 1.0** | `cc0-1.0` | Yes | Yes | No | Universal waiver of copyright dedication. Free for all reproduction. |
| **CC Attribution 4.0** | `cc-by-4.0` | Yes | Yes | Yes | Open scholarly articles and datasets; requires creator credit. |
| **CC Attribution-NonCommercial 4.0** | `cc-by-nc-4.0` | No | Yes | Yes | Academic reuse permitted; commercial exploitation barred. |
| **CC Attribution-ShareAlike 4.0** | `cc-by-sa-4.0` | Yes | Yes | Yes | Derivative works must be released under identical terms. |
| **Open Government Data (OGD) India** | `ogd-india` | Yes | Yes | Yes | Official publications by Indian government research ministries. |
| **Academic Fair Use / Research Exemption** | `academic-fair-use` | No | **No** | Yes | Section 52 of Indian Copyright Act 1957. Metadata only; no file redistribution. |
| **In-Copyright (Read Online Only)** | `in-copyright-read-only` | No | **No** | Yes | Contemporary critical editions available to read at source library; downloads disabled. |
| **Restricted Cultural Heritage** | `restricted-heritage` | No | **No** | Yes | Rare fragile manuscripts; strictly restricted to physical or authorized digital inspection. |

---

## 3. Controlled Download Enforcement

When a user requests a file via `GET /api/resources/{id}/download`, the server executes a multi-factor legal check:

```python
# 1. Verification Audit Check
if resource.verification_status != "Verified":
    raise HTTPException(status_code=403, detail="Download unavailable: This resource is pending legal verification.")

# 2. Access Status Check
if resource.access_status in ("Restricted Access", "Metadata Only", "Pending Verification"):
    raise HTTPException(status_code=403, detail=f"Direct download is prohibited under '{resource.access_status}'.")

# 3. License Redistribution Rights Check
if resource.license and not resource.license.redistribution_allowed and resource.access_status != "Download Available":
    raise HTTPException(status_code=403, detail=f"Licensing restriction: The license '{resource.license.name}' does not allow direct redistribution. You may read the text online at the source institution.")
```

If unauthorized, the endpoint denies retrieval with **HTTP 403 Forbidden**, preventing copyright infringement while keeping scholarly citation and metadata intact.

---

## 4. Audit of the 32 Seed Treatises

All 32 seeded records were audited against their respective source institutions:
- **Public Domain Editions**: 19th and early 20th century translations by Thibaut, Griffith, Müller, Woods, Monier-Williams, Shamasastry, etc., published before 1928, are correctly designated as `Public Domain` or `Download Available`.
- **Contemporary Academic Translations**: Modern translations (e.g., AAHF editions translated by Nalini Sadhale, BORI publications, INFLIBNET monographs) are designated as `Read Online` or `In-Copyright (Read Online Only)` with direct downloads disabled, respecting copyright held by those foundations.
- **Institutional Attribution**: Every record explicitly credits the preserving archive (IGNCA, NDLI, BORI, INSA, MS University Baroda, RBSI) alongside active links to the host catalog.
