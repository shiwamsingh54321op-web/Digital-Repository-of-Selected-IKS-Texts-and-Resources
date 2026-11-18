# Search & Information Retrieval Engine Specification

## 1. Engine Overview

The repository's retrieval facility is powered by **SQLite FTS5** (Full-Text Search Version 5) augmented with custom tokenization, column weighting, and **Okapi BM25** probabilistic relevance ranking.

---

## 2. FTS5 Virtual Table Definition

The virtual table `resources_fts` is defined as:

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS resources_fts USING fts5(
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
```

### Tokenizer Configuration:
1. **`unicode61`**: Full Unicode handling supporting multilingual text.
2. **`remove_diacritics 2`**: Strips diacritical accents during both indexing and query parsing. This allows searchers to type either standard ASCII (e.g. *Sankhya Karika*, *Aryabhata*) or rigorous IAST transliteration (e.g. *Sāṅkhyakārikā*, *Āryabhaṭa*) and achieve identical matching.
3. **`porter`**: English Porter stemming algorithm for morphological inflection matching (e.g., *astronomical* matches *astronomy*).

---

## 3. Automated Database Trigger Synchronization

To avoid reliance on background indexing worker processes, synchronization between the physical `resources` table and the virtual `resources_fts` table is managed entirely by three native SQLite triggers:

```sql
-- On Insert
CREATE TRIGGER IF NOT EXISTS trg_resources_insert AFTER INSERT ON resources
BEGIN
    INSERT INTO resources_fts (
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

-- On Delete
CREATE TRIGGER IF NOT EXISTS trg_resources_delete AFTER DELETE ON resources
BEGIN
    DELETE FROM resources_fts WHERE rowid = old.id;
END;

-- On Update
CREATE TRIGGER IF NOT EXISTS trg_resources_update AFTER UPDATE ON resources
BEGIN
    DELETE FROM resources_fts WHERE rowid = old.id;
    INSERT INTO resources_fts (
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
```

---

## 4. Relevance Ranking & Column Weighting

Matches are evaluated using the native `bm25()` function with column weights:

$$\text{Weighting Vector} = [10.0, 5.0, 2.0, 2.0, 6.0, 4.0, 5.0, 1.0, 2.0]$$

1. `title` (weight 10.0) — Highest priority.
2. `creator` (weight 6.0) — Author/commentator matches.
3. `keywords` (weight 5.0) — Controlled indexing vocabulary.
4. `subtitle` (weight 5.0) — Commentary and recension names.
5. `subject` (weight 4.0) — Dublin Core subject classification.
6. `description` / `abstract` (weight 2.0) — Deep text descriptions.
7. `source_institution` (weight 2.0) — Archive provenance.
8. `language` (weight 1.0) — Base language.

SQLite FTS5 BM25 assigns negative scores (lower is more relevant). The engine negates the value:
$$\text{relevance\_score} = - \text{bm25}(...)$$
so higher numbers indicate greater relevance to the user.

---

## 5. Autocomplete & Query Suggestions

The `/api/search/suggestions` endpoint provides sub-millisecond prefix autocompletion queries:
- Prefixes of 2 or more characters match indexed `keywords`, `title` prefixes, and `creator` names.
- Returns suggestions grouped with semantic metadata (`type`: `keyword`, `title`, or `creator`).
