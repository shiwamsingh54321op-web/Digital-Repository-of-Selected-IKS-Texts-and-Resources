import pytest
import httpx
from fastapi.testclient import TestClient
from app.main import app

def get_test_client():
    try:
        r = httpx.get("http://127.0.0.1:8000/api/health", timeout=0.5)
        if r.status_code == 200:
            return httpx.Client(base_url="http://127.0.0.1:8000")
    except Exception:
        pass
    return TestClient(app)

client = get_test_client()


def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["database"] == "healthy"


def test_public_statistics_endpoint():
    response = client.get("/api/statistics")
    assert response.status_code == 200
    data = response.json()
    assert data["total_resources"] >= 30
    assert data["total_domains"] >= 12
    assert data["total_languages"] >= 1
    assert data["total_institutions"] >= 5


def test_list_resources():
    response = client.get("/api/resources?page=1&page_size=10")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 30
    assert len(data["items"]) == 10
    assert data["page"] == 1


def test_get_resource_detail_and_dublin_core():
    # Fetch first resource
    list_resp = client.get("/api/resources?page=1&page_size=1")
    first_id = list_resp.json()["items"][0]["id"]

    response = client.get(f"/api/resources/{first_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == first_id
    assert "dublin_core" in data
    dc = data["dublin_core"]
    assert dc["title"] == data["title"]
    assert dc["creator"] == data["creator"]
    assert dc["subject"] == data["subject"]
    assert "rights" in dc


def test_citation_endpoint():
    list_resp = client.get("/api/resources?page=1&page_size=1")
    first_id = list_resp.json()["items"][0]["id"]

    response = client.get(f"/api/resources/{first_id}/citation")
    assert response.status_code == 200
    citations = response.json()
    assert "apa" in citations
    assert "mla" in citations
    assert "chicago" in citations
    assert "bibtex" in citations
    assert "@misc" in citations["bibtex"]


def test_download_permission_enforcement():
    # 1. Allowed download resource (Public Domain text like Aryabhatiya or Lilavati)
    res_list = client.get("/api/resources?access_status=Download Available")
    items = res_list.json()["items"]
    assert len(items) > 0
    allowed_id = items[0]["id"]

    download_resp = client.get(f"/api/resources/{allowed_id}/download")
    assert download_resp.status_code == 200
    assert download_resp.json()["status"] == "permitted"
    assert "download_url" in download_resp.json()

    # 2. Restricted download resource (Read Online or in-copyright)
    res_read_only = client.get("/api/resources?access_status=Read Online")
    read_items = res_read_only.json()["items"]
    assert len(read_items) > 0
    restricted_id = read_items[0]["id"]

    restricted_resp = client.get(f"/api/resources/{restricted_id}/download")
    assert restricted_resp.status_code == 403
    assert "restriction" in restricted_resp.json()["detail"].lower() or "prohibited" in restricted_resp.json()["detail"].lower()


def test_domains_endpoint():
    response = client.get("/api/domains")
    assert response.status_code == 200
    domains = response.json()
    assert len(domains) >= 12
    # Verify subcategories are loaded
    assert any(len(d["subcategories"]) > 0 for d in domains)


def test_licenses_endpoint():
    response = client.get("/api/licenses")
    assert response.status_code == 200
    licenses = response.json()
    assert len(licenses) >= 9


def test_institutions_endpoint():
    response = client.get("/api/institutions")
    assert response.status_code == 200
    institutions = response.json()
    assert len(institutions) >= 10
