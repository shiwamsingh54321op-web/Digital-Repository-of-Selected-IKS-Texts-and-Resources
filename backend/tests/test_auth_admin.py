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


@pytest.fixture(scope="module")
def admin_token():
    login_resp = client.post("/api/auth/login", json={
        "username": "admin",
        "password": "Admin@IKS2026!"
    })
    assert login_resp.status_code == 200
    token = login_resp.json()["access_token"]
    return token


def test_login_invalid_credentials():
    resp = client.post("/api/auth/login", json={
        "username": "admin",
        "password": "WrongPassword123"
    })
    assert resp.status_code == 401


def test_auth_me_endpoint(admin_token):
    resp = client.get("/api/auth/me", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["username"] == "admin"
    assert data["role"] == "administrator"


def test_protected_routes_without_token():
    resp = client.get("/api/admin/dashboard")
    assert resp.status_code == 401


def test_admin_dashboard(admin_token):
    resp = client.get("/api/admin/dashboard", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    data = resp.json()
    assert "overview" in data
    assert data["overview"]["total_resources"] >= 30
    assert "distributions" in data


def test_admin_resource_crud_lifecycle(admin_token):
    # 1. Fetch domain and license IDs
    dom_resp = client.get("/api/domains")
    domain_id = dom_resp.json()[0]["id"]
    lic_resp = client.get("/api/licenses")
    license_id = lic_resp.json()[0]["id"]

    # 2. Create resource
    new_res_data = {
        "title": "Yuktidipika: Commentary on the Samkhyakarika",
        "subtitle": "Critical Edition of a Rare Philosophy Treatise",
        "creator": "Unknown Classical Scholar (Edited by Albrecht Wezler)",
        "subject": "Classical Samkhya Philosophy",
        "description": "An essential ancient commentary on Ishvarakrishna's Samkhyakarika presenting exhaustive epistemological refutations.",
        "abstract": "The Yuktidipika is an encyclopedic commentary that establishes the classical Samkhya dualist ontology.",
        "language": "Sanskrit",
        "resource_type": "Book",
        "knowledge_domain_id": domain_id,
        "source_institution": "Bhandarkar Oriental Research Institute (BORI)",
        "source_url": "https://bori.ac.in/yuktidipika",
        "license_id": license_id,
        "rights_statement": "Open educational access for research.",
        "access_status": "Open Access",
        "verification_status": "Pending",
        "keywords": "Yuktidipika, Samkhya, Philosophy, Epistemology"
    }

    create_resp = client.post(
        "/api/admin/resources",
        json=new_res_data,
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert create_resp.status_code == 201
    created = create_resp.json()
    res_id = created["id"]
    assert created["title"] == new_res_data["title"]
    assert created["verification_status"] == "Pending"

    # 3. Update Verification Status to 'Verified'
    patch_resp = client.patch(
        f"/api/admin/resources/{res_id}/verification",
        json={"verification_status": "Verified", "rights_statement": "Verified CC BY-NC-SA 4.0 by admin."},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert patch_resp.status_code == 200
    assert patch_resp.json()["verification_status"] == "Verified"

    # 4. Search as public user and verify newly created resource appears
    search_resp = client.get("/api/search?q=Yuktidipika")
    assert search_resp.status_code == 200
    search_results = search_resp.json()["results"]
    assert any(r["id"] == res_id for r in search_results)

    # 5. Delete resource
    del_resp = client.delete(
        f"/api/admin/resources/{res_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert del_resp.status_code == 204

    # 6. Verify resource is gone
    get_resp = client.get(f"/api/resources/{res_id}")
    assert get_resp.status_code == 404


def test_admin_metadata_exports(admin_token):
    # CSV export
    csv_resp = client.get(
        "/api/admin/export/resources.csv",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert csv_resp.status_code == 200
    assert "text/csv" in csv_resp.headers["content-type"]
    assert "dc_title" in csv_resp.text
    assert "dc_creator" in csv_resp.text
    assert "Aryabhatiya" in csv_resp.text

    # JSON export
    json_resp = client.get(
        "/api/admin/export/resources.json",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert json_resp.status_code == 200
    assert "application/json" in json_resp.headers["content-type"]
    json_data = json_resp.json()
    assert isinstance(json_data, list)
    assert len(json_data) >= 30
    assert "dublin_core" in json_data[0]
