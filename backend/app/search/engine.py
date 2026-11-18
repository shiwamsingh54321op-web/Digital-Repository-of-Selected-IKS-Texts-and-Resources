import re
import logging
from typing import List, Dict, Any, Optional, Tuple
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.resource import Resource

logger = logging.getLogger(__name__)

# FTS5 Virtual Table and Triggers SQL Definitions
FTS_TABLE_NAME = "resources_fts"

CREATE_FTS_TABLE_SQL = f"""
CREATE VIRTUAL TABLE IF NOT EXISTS {FTS_TABLE_NAME} USING fts5(
    title,
    subtitle,
    description,
    abstract,
    creator,
    subject,
    keywords,
    language,
    source_institution,
    tokenize = 'porter unicode61 remove_diacritics 2'
);
"""

# SQLite Triggers for automated synchronization between resources and resources_fts
CREATE_INSERT_TRIGGER_SQL = f"""
CREATE TRIGGER IF NOT EXISTS trg_resources_insert AFTER INSERT ON resources
BEGIN
    INSERT INTO {FTS_TABLE_NAME} (
        rowid, title, subtitle, description, abstract,
        creator, subject, keywords, language, source_institution
    )
    VALUES (
        new.id,
        COALESCE(new.title, ''),
        COALESCE(new.subtitle, ''),
        COALESCE(new.description, ''),
        COALESCE(new.abstract, ''),
        COALESCE(new.creator, ''),
        COALESCE(new.subject, ''),
        COALESCE(new.keywords, ''),
        COALESCE(new.language, ''),
        COALESCE(new.source_institution, '')
    );
END;
"""

CREATE_DELETE_TRIGGER_SQL = f"""
CREATE TRIGGER IF NOT EXISTS trg_resources_delete AFTER DELETE ON resources
BEGIN
    DELETE FROM {FTS_TABLE_NAME} WHERE rowid = old.id;
END;
"""

CREATE_UPDATE_TRIGGER_SQL = f"""
CREATE TRIGGER IF NOT EXISTS trg_resources_update AFTER UPDATE ON resources
BEGIN
    DELETE FROM {FTS_TABLE_NAME} WHERE rowid = old.id;
    INSERT INTO {FTS_TABLE_NAME} (
        rowid, title, subtitle, description, abstract,
        creator, subject, keywords, language, source_institution
    )
    VALUES (
        new.id,
        COALESCE(new.title, ''),
        COALESCE(new.subtitle, ''),
        COALESCE(new.description, ''),
        COALESCE(new.abstract, ''),
        COALESCE(new.creator, ''),
        COALESCE(new.subject, ''),
        COALESCE(new.keywords, ''),
        COALESCE(new.language, ''),
        COALESCE(new.source_institution, '')
    );
END;
"""

# BM25 weights: title (5.0), subtitle (3.0), description (1.0), abstract (1.5),
# creator (3.0), subject (4.0), keywords (3.5), language (2.0), source_institution (2.0)
BM25_WEIGHTS = "5.0, 3.0, 1.0, 1.5, 3.0, 4.0, 3.5, 2.0, 2.0"


def init_fts_index(db: Session) -> None:
    """Initialize the FTS5 virtual table and synchronization triggers."""
    try:
        db.execute(text(CREATE_FTS_TABLE_SQL))
        db.execute(text(CREATE_INSERT_TRIGGER_SQL))
        db.execute(text(CREATE_DELETE_TRIGGER_SQL))
        db.execute(text(CREATE_UPDATE_TRIGGER_SQL))
        db.commit()
        logger.info("SQLite FTS5 full-text search table and triggers successfully verified.")
    except Exception as e:
        db.rollback()
        logger.error(f"Error initializing FTS5 index: {e}")
        raise


def rebuild_fts_index(db: Session) -> int:
    """Rebuild the FTS5 index from the resources table."""
    try:
        db.execute(text(f"DELETE FROM {FTS_TABLE_NAME};"))
        populate_sql = f"""
        INSERT INTO {FTS_TABLE_NAME} (
            rowid, title, subtitle, description, abstract,
            creator, subject, keywords, language, source_institution
        )
        SELECT
            id,
            COALESCE(title, ''),
            COALESCE(subtitle, ''),
            COALESCE(description, ''),
            COALESCE(abstract, ''),
            COALESCE(creator, ''),
            COALESCE(subject, ''),
            COALESCE(keywords, ''),
            COALESCE(language, ''),
            COALESCE(source_institution, '')
        FROM resources;
        """
        result = db.execute(text(populate_sql))
        db.commit()
        count = db.execute(text(f"SELECT count(*) FROM {FTS_TABLE_NAME}")).scalar() or 0
        logger.info(f"Rebuilt FTS5 index. Indexed {count} records.")
        return count
    except Exception as e:
        db.rollback()
        logger.error(f"Error rebuilding FTS5 index: {e}")
        raise


def sanitize_fts_query(raw_query: str) -> str:
    """
    Safely parse user search input into valid SQLite FTS5 query syntax.
    Handles phrases in quotes, word stems with *, and filters out illegal punctuation.
    """
    if not raw_query:
        return ""

    query = raw_query.strip()
    if not query:
        return ""

    # Check for quoted exact phrases like "Ancient Indian"
    phrases = re.findall(r'"([^"]+)"', query)
    tokens: List[str] = []

    for phrase in phrases:
        cleaned_phrase = re.sub(r'[^\w\s-]', '', phrase).strip()
        if cleaned_phrase:
            tokens.append(f'"{cleaned_phrase}"')

    # Remove the quoted phrases from remaining query text
    remaining = re.sub(r'"[^"]+"', ' ', query)
    # Remove unsupported characters but keep alphanumeric, hyphens, and whitespace
    clean_words = re.findall(r'[\w-]+', remaining)

    for word in clean_words:
        w_lower = word.lower()
        # Avoid treating raw boolean operators alone as rogue syntax
        if w_lower in ("and", "or", "not"):
            continue
        # Support wildcard prefix for terms longer than 2 chars
        if len(word) >= 3:
            tokens.append(f"{word}*")
        else:
            tokens.append(word)

    if not tokens:
        return ""

    # Combine tokens with NEAR or default space (implicit AND in FTS5)
    return " ".join(tokens)


class SearchEngine:
    """
    Information Retrieval Engine backed by SQLite FTS5 with BM25 ranking.
    """

    @staticmethod
    def search(
        db: Session,
        query_str: Optional[str] = None,
        domain_id: Optional[int] = None,
        domain_slug: Optional[str] = None,
        resource_type: Optional[str] = None,
        language: Optional[str] = None,
        access_status: Optional[str] = None,
        license_id: Optional[int] = None,
        institution_id: Optional[int] = None,
        verification_status: Optional[str] = "Verified",
        sort_by: str = "relevance",
        page: int = 1,
        page_size: int = 12
    ) -> Dict[str, Any]:
        """
        Execute ranked full-text search with multi-faceted filtering, BM25 scoring,
        and result snippet highlighting.
        """
        page = max(1, page)
        page_size = max(1, min(100, page_size))
        offset = (page - 1) * page_size

        fts_query = sanitize_fts_query(query_str or "")
        has_text_query = bool(fts_query)

        # Base SELECT clause and JOINs
        select_cols = [
            "r.id",
            "r.title",
            "r.subtitle",
            "r.description",
            "r.abstract",
            "r.creator",
            "r.contributor",
            "r.subject",
            "r.language",
            "r.translated_language",
            "r.resource_type",
            "r.knowledge_domain_id",
            "r.publisher",
            "r.publication_date",
            "r.digitisation_date",
            "r.source_institution",
            "r.institution_id",
            "r.source_url",
            "r.access_url",
            "r.download_url",
            "r.license_id",
            "r.rights_statement",
            "r.access_status",
            "r.file_format",
            "r.file_size",
            "r.thumbnail_url",
            "r.isbn_or_identifier",
            "r.keywords",
            "r.citation",
            "r.verification_status",
            "r.created_at",
            "d.name AS domain_name",
            "d.slug AS domain_slug",
            "l.name AS license_name",
            "l.identifier AS license_identifier",
            "l.redistribution_allowed AS license_redistribution_allowed",
            "inst.institution_name AS institution_name_ref"
        ]

        from_clause = """
            FROM resources r
            JOIN knowledge_domains d ON r.knowledge_domain_id = d.id
            JOIN licenses l ON r.license_id = l.id
            LEFT JOIN institutions inst ON r.institution_id = inst.id
        """

        where_clauses: List[str] = []
        params: Dict[str, Any] = {
            "limit": page_size,
            "offset": offset
        }

        # If verification status is set
        if verification_status:
            where_clauses.append("r.verification_status = :verification_status")
            params["verification_status"] = verification_status

        # If FTS text query is provided, join with resources_fts and calculate BM25 score
        if has_text_query:
            from_clause += f"""
                JOIN (
                    SELECT rowid, bm25({FTS_TABLE_NAME}, {BM25_WEIGHTS}) as rank,
                           snippet({FTS_TABLE_NAME}, 2, '<mark class="bg-amber-100 font-semibold px-1 rounded">', '</mark>', '...', 22) as snippet_desc
                    FROM {FTS_TABLE_NAME}
                    WHERE {FTS_TABLE_NAME} MATCH :fts_query
                ) fts ON r.id = fts.rowid
            """
            select_cols.append("fts.rank AS bm25_rank")
            select_cols.append("fts.snippet_desc AS search_snippet")
            params["fts_query"] = fts_query
        else:
            select_cols.append("0.0 AS bm25_rank")
            select_cols.append("NULL AS search_snippet")

        # Faceted filters
        if domain_id is not None:
            where_clauses.append("r.knowledge_domain_id = :domain_id")
            params["domain_id"] = domain_id
        elif domain_slug:
            where_clauses.append("d.slug = :domain_slug")
            params["domain_slug"] = domain_slug

        if resource_type:
            where_clauses.append("r.resource_type = :resource_type")
            params["resource_type"] = resource_type

        if language:
            where_clauses.append("r.language = :language")
            params["language"] = language

        if access_status:
            where_clauses.append("r.access_status = :access_status")
            params["access_status"] = access_status

        if license_id is not None:
            where_clauses.append("r.license_id = :license_id")
            params["license_id"] = license_id

        if institution_id is not None:
            where_clauses.append("r.institution_id = :institution_id")
            params["institution_id"] = institution_id

        where_str = ""
        if where_clauses:
            where_str = "WHERE " + " AND ".join(where_clauses)

        # Count total records for pagination
        count_sql = f"SELECT COUNT(*) {from_clause} {where_str}"
        total_count = db.execute(text(count_sql), params).scalar() or 0

        # Sorting rules
        order_by = "r.id DESC"
        if has_text_query and sort_by == "relevance":
            # BM25 in SQLite FTS5 returns negative values; smaller (more negative) means higher relevance
            order_by = "fts.rank ASC, r.title ASC"
        elif sort_by == "title_asc":
            order_by = "r.title ASC"
        elif sort_by == "title_desc":
            order_by = "r.title DESC"
        elif sort_by == "newest":
            order_by = "r.created_at DESC"
        elif sort_by == "oldest":
            order_by = "r.created_at ASC"

        # Final query execution
        cols_str = ", ".join(select_cols)
        query_sql = f"""
            SELECT {cols_str}
            {from_clause}
            {where_str}
            ORDER BY {order_by}
            LIMIT :limit OFFSET :offset
        """

        rows = db.execute(text(query_sql), params).mappings().all()

        results = []
        for row in rows:
            results.append(dict(row))

        total_pages = (total_count + page_size - 1) // page_size if total_count > 0 else 1

        return {
            "query": query_str or "",
            "sanitized_query": fts_query,
            "total": total_count,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1,
            "results": results
        }

    @staticmethod
    def get_suggestions(db: Session, prefix: str, limit: int = 8) -> List[Dict[str, str]]:
        """
        Provide autocomplete suggestions for repository search queries
        based on indexed keywords, creator names, and title fragments.
        """
        if not prefix or len(prefix.strip()) < 2:
            return []

        clean = prefix.strip().lower()
        search_pattern = f"{clean}%"

        # Fetch keywords matching prefix
        kw_sql = """
            SELECT keyword AS text, 'keyword' AS type
            FROM keywords
            WHERE LOWER(keyword) LIKE :pattern
            LIMIT :limit
        """
        kw_results = db.execute(text(kw_sql), {"pattern": search_pattern, "limit": limit}).mappings().all()

        # Fetch matching resource titles
        title_sql = """
            SELECT title AS text, 'title' AS type
            FROM resources
            WHERE LOWER(title) LIKE :pattern
            LIMIT :limit
        """
        title_results = db.execute(text(title_sql), {"pattern": search_pattern, "limit": limit}).mappings().all()

        # Fetch matching creators/authors
        creator_sql = """
            SELECT DISTINCT creator AS text, 'creator' AS type
            FROM resources
            WHERE LOWER(creator) LIKE :pattern
            LIMIT :limit
        """
        creator_results = db.execute(text(creator_sql), {"pattern": search_pattern, "limit": limit}).mappings().all()

        combined = []
        seen = set()

        for item in list(kw_results) + list(title_results) + list(creator_results):
            text_val = item["text"]
            if text_val and text_val.lower() not in seen:
                seen.add(text_val.lower())
                combined.append({"text": text_val, "type": item["type"]})
                if len(combined) >= limit:
                    break

        return combined
