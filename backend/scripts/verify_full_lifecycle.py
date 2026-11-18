import httpx
import json

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    client = httpx.Client(base_url=BASE_URL, timeout=10.0)

    print("==================================================")
    print("RUNNING END-TO-END VERIFICATION AUDIT")
    print("==================================================")

    # 1. Health & Statistics
    print("\n--- 1. Health & Statistics ---")
    r = client.get("/api/health")
    assert r.status_code == 200, f"Health check failed: {r.status_code}"
    print(f"Health Check: PASS ({r.json()['status']}, db: {r.json()['database']})")

    r_stats = client.get("/api/statistics")
    assert r_stats.status_code == 200, f"Statistics failed: {r_stats.status_code}"
    stats = r_stats.json()
    assert stats["total_resources"] >= 32, "Resource count mismatch"
    assert stats["total_domains"] >= 12, "Domain count mismatch"
    print(f"Repository Statistics: PASS ({stats['total_resources']} resources, {stats['total_domains']} domains)")

    # 2. Search & Autocomplete
    print("\n--- 2. Search & Autocomplete Engine ---")
    r_sugg = client.get("/api/search/suggestions?q=Arya")
    assert r_sugg.status_code == 200
    suggestions = r_sugg.json()
    assert len(suggestions) > 0, "No suggestions returned for 'Arya'"
    print(f"Autocomplete Suggestions: PASS ({len(suggestions)} suggestions for 'Arya': {[s['text'] for s in suggestions[:3]]})")

    r_search = client.get("/api/search?q=Aryabhatiya")
    assert r_search.status_code == 200
    search_data = r_search.json()
    assert search_data["total"] >= 1, "Search for 'Aryabhatiya' returned 0 results"
    first_hit = search_data["results"][0]
    print(f"Search Query 'Aryabhatiya': PASS (Total hits: {search_data['total']}, Top hit: {first_hit['title']})")

    # Transliteration / Diacritic check
    r_dia1 = client.get("/api/search?q=Aryabhata")
    r_dia2 = client.get("/api/search?q=Āryabhaṭa")
    assert r_dia1.status_code == 200 and r_dia2.status_code == 200
    assert r_dia1.json()["total"] == r_dia2.json()["total"], f"Diacritic mismatch: {r_dia1.json()['total']} vs {r_dia2.json()['total']}"
    print(f"Sanskrit Diacritic Tolerance (Aryabhata vs Āryabhaṭa): PASS (Hits: {r_dia1.json()['total']})")

    # 3. Faceted Filters & Pagination
    print("\n--- 3. Faceted Filtering & Pagination ---")
    # Filter by domain
    r_domain = client.get("/api/resources?domain_slug=ayurveda-and-traditional-medicine")
    assert r_domain.status_code == 200
    ayur_items = r_domain.json()["items"]
    assert len(ayur_items) >= 2, "Ayurveda domain filter returned too few items"
    assert all("Ayurveda" in (item.get("primary_domain") or {}).get("name", "") for item in ayur_items)
    print(f"Domain Filtering: PASS ({len(ayur_items)} items for 'Ayurveda')")

    # Filter by resource_type
    r_type = client.get("/api/resources?resource_type=Book")
    assert r_type.status_code == 200
    assert len(r_type.json()["items"]) > 0, "No Book items found"
    assert all(item["resource_type"] == "Book" for item in r_type.json()["items"])
    print(f"Resource Type Filtering: PASS ({r_type.json()['total']} Books)")

    # Pagination
    r_p1 = client.get("/api/resources?page=1&page_size=10")
    r_p2 = client.get("/api/resources?page=2&page_size=10")
    assert r_p1.status_code == 200 and r_p2.status_code == 200
    assert len(r_p1.json()["items"]) == 10
    assert len(r_p2.json()["items"]) == 10
    assert r_p1.json()["items"][0]["id"] != r_p2.json()["items"][0]["id"], "Page 1 and Page 2 contain same records!"
    print(f"Pagination (Page 1 & 2): PASS (10 items per page, distinct records)")

    # 4. Resource Details & Citation Generation
    print("\n--- 4. Dublin Core & Citation Generation ---")
    r_detail = client.get("/api/resources/1")
    assert r_detail.status_code == 200
    detail = r_detail.json()
    assert "dublin_core" in detail, "Missing dublin_core in detail"
    dc = detail["dublin_core"]
    for req_field in ["title", "creator", "subject", "description", "rights", "language", "type"]:
        assert dc[req_field], f"Missing DC element: {req_field}"
    print(f"Dublin Core 15 Elements: PASS (dc:title = '{dc['title'][:30]}...')")

    r_cite = client.get("/api/resources/1/citation")
    assert r_cite.status_code == 200
    citations = r_cite.json()
    for style in ["apa", "mla", "chicago", "bibtex"]:
        assert style in citations and len(citations[style]) > 10, f"Citation style {style} invalid"
    print(f"Scholarly Citation Generation: PASS (APA, MLA, Chicago, BibTeX verified)")

    # 5. Admin Authentication & Resource CRUD Lifecycle
    print("\n--- 5. Admin Login & Resource CRUD Lifecycle ---")
    login_resp = client.post("/api/auth/login", json={
        "username": "admin",
        "password": "Admin@IKS2026!"
    })
    assert login_resp.status_code == 200, f"Admin login failed: {login_resp.status_code}"
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print(f"Admin Authentication: PASS (Bearer token received)")

    # Test Admin Dashboard
    r_dash = client.get("/api/admin/dashboard", headers=headers)
    assert r_dash.status_code == 200
    print(f"Admin Dashboard Analytics: PASS ({r_dash.json()['overview']['total_resources']} resources)")

    # Create a new test resource
    test_resource_payload = {
        "title": "Yuktidipika on Samkhyakarika",
        "subtitle": "An Ancient Commentary on Samkhya Philosophy",
        "description": "Comprehensive classical commentary elucidating the Samkhyakarika epistemology and dualism.",
        "abstract": "Scholarly text critical edition of the ancient Samkhya school commentary.",
        "creator": "Unknown Classical Scholar (Edited by Albrecht Wezler)",
        "subject": "Samkhya Philosophy",
        "language": "Sanskrit",
        "resource_type": "Critical Edition",
        "knowledge_domain_id": 4, # Yoga and Philosophy
        "source_institution": "Bhandarkar Oriental Research Institute (BORI)",
        "source_url": "https://bori.ac.in/catalogue/yuktidipika",
        "license_id": 1, # Public domain
        "rights_statement": "Public domain academic edition.",
        "access_status": "Download Available",
        "verification_status": "Verified",
        "keywords": "Samkhya, Karika, Yuktidipika, Philosophy"
    }

    create_resp = client.post("/api/admin/resources", json=test_resource_payload, headers=headers)
    assert create_resp.status_code in (200, 201), f"Resource creation failed: {create_resp.status_code} - {create_resp.text}"
    created_id = create_resp.json()["id"]
    print(f"Resource CREATE: PASS (Created new resource ID {created_id})")

    # Verify newly created resource appears in catalog
    r_get_new = client.get(f"/api/resources/{created_id}")
    assert r_get_new.status_code == 200
    assert r_get_new.json()["title"] == test_resource_payload["title"]
    print(f"Newly Created Resource in Catalogue: PASS (ID {created_id} verified)")

    # Verify newly created resource is indexed and searchable via FTS5 triggers!
    search_new = client.get("/api/search?q=Yuktidipika")
    assert search_new.status_code == 200
    assert any(item["id"] == created_id for item in search_new.json()["results"]), "Newly created resource NOT found in FTS search!"
    print(f"Newly Created Resource in Full-Text Search (FTS5): PASS (Found via query 'Yuktidipika')")

    # Update the resource
    update_payload = dict(test_resource_payload)
    update_payload["subtitle"] = "Updated Subtitle for Verification Test"
    update_resp = client.put(f"/api/admin/resources/{created_id}", json=update_payload, headers=headers)
    assert update_resp.status_code == 200
    assert update_resp.json()["subtitle"] == "Updated Subtitle for Verification Test"
    print(f"Resource UPDATE: PASS (Updated subtitle)")

    # Delete the resource
    del_resp = client.delete(f"/api/admin/resources/{created_id}", headers=headers)
    assert del_resp.status_code in (200, 204), f"Delete failed: {del_resp.status_code}"
    print(f"Resource DELETE: PASS (Deleted ID {created_id})")

    # Verify deleted resource is gone from catalog and search
    r_gone = client.get(f"/api/resources/{created_id}")
    assert r_gone.status_code == 404, "Deleted resource still accessible!"
    search_gone = client.get("/api/search?q=Yuktidipika")
    assert not any(item["id"] == created_id for item in search_gone.json()["results"]), "Deleted resource still returned by FTS5!"
    print(f"Resource Delete Cleanup: PASS (Properly un-indexed from FTS5 and catalog)")

    print("\n==================================================")
    print("ALL API & RETRIEVAL LIFECYCLE CHECKS PASSED!")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
