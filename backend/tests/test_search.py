import pytest
from app.database.session import SessionLocal
from app.search.engine import SearchEngine, sanitize_fts_query
from app.services.search_service import SearchService


@pytest.fixture(scope="module")
def db():
    session = SessionLocal()
    yield session
    session.close()


def test_sanitize_fts_query():
    # Empty queries
    assert sanitize_fts_query("") == ""
    assert sanitize_fts_query("   ") == ""

    # Natural words
    sanitized = sanitize_fts_query("Ayurveda medicine")
    assert "Ayurveda*" in sanitized
    assert "medicine*" in sanitized

    # Quoted phrase
    sanitized_phrase = sanitize_fts_query('"Indian Mathematics"')
    assert '"Indian Mathematics"' in sanitized_phrase

    # Punctuation stripping
    sanitized_unsafe = sanitize_fts_query("Veda! @#$%^&*() +_")
    assert "Veda*" in sanitized_unsafe


def test_search_by_keyword(db):
    res = SearchEngine.search(db, query_str="mathematics")
    assert res["total"] >= 1
    titles = [r["title"].lower() for r in res["results"]]
    assert any("aryabhatiya" in t or "lilavati" in t or "science" in t for t in titles)


def test_search_by_creator(db):
    res = SearchEngine.search(db, query_str="Patanjali")
    assert res["total"] >= 1
    assert "Yoga" in res["results"][0]["title"]


def test_search_bm25_ranking(db):
    # Searching for "Aryabhata" should rank the primary treatise Aryabhatiya first
    res = SearchEngine.search(db, query_str="Aryabhata", sort_by="relevance")
    assert res["total"] >= 1
    first_hit = res["results"][0]
    assert "Aryabhatiya" in first_hit["title"]
    assert first_hit["bm25_rank"] < 0  # BM25 negative score indicates match rank


def test_search_with_domain_filter(db):
    # Search within Ayurveda domain
    res = SearchEngine.search(
        db,
        query_str="medicine",
        domain_slug="ayurveda-and-traditional-medicine"
    )
    assert res["total"] >= 1
    for r in res["results"]:
        assert r["domain_slug"] == "ayurveda-and-traditional-medicine"


def test_search_with_license_filter(db):
    # Search for public domain records
    res = SearchEngine.search(
        db,
        query_str="Veda",
        access_status="Download Available"
    )
    for r in res["results"]:
        assert r["access_status"] == "Download Available"


def test_search_pagination(db):
    res_page_1 = SearchEngine.search(db, page=1, page_size=5)
    assert len(res_page_1["results"]) == 5
    assert res_page_1["page"] == 1
    assert res_page_1["has_next"] is True

    res_page_2 = SearchEngine.search(db, page=2, page_size=5)
    assert len(res_page_2["results"]) == 5
    assert res_page_2["page"] == 2
    # Ensure items on page 1 and page 2 are different
    ids_1 = {r["id"] for r in res_page_1["results"]}
    ids_2 = {r["id"] for r in res_page_2["results"]}
    assert len(ids_1.intersection(ids_2)) == 0


def test_search_suggestions(db):
    suggestions = SearchEngine.get_suggestions(db, prefix="Ayu")
    assert len(suggestions) >= 1
    assert any("Ayurveda" in s["text"] for s in suggestions)
