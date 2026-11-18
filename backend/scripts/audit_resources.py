import sqlite3
import httpx

def audit():
    con = sqlite3.connect('backend/iks_repository.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute('''
        SELECT r.id, r.title, r.creator, r.access_status, r.verification_status,
               r.source_institution, r.source_url,
               l.name as license_name, l.identifier as license_id,
               l.redistribution_allowed, l.commercial_use_allowed
        FROM resources r
        JOIN licenses l ON r.license_id = l.id
        ORDER BY r.id
    ''').fetchall()

    print(f"==================================================")
    print(f"RESOURCE LICENSING & DOWNLOAD PERMISSION AUDIT")
    print(f"Total Resources Audited: {len(rows)}")
    print(f"==================================================")

    download_allowed_count = 0
    download_restricted_count = 0

    client = httpx.Client(base_url="http://127.0.0.1:8000")

    for r in rows:
        rid = r["id"]
        title = r["title"][:40]
        acc = r["access_status"]
        lic = r["license_id"]
        redis = r["redistribution_allowed"]

        # Test download endpoint via HTTP
        resp = client.get(f"/api/resources/{rid}/download")
        http_status = resp.status_code

        if http_status == 200:
            download_allowed_count += 1
            dl_flag = "PERMITTED (200 OK)"
            # Ensure the resource is actually permitted
            assert acc in ("Download Available", "Open Access"), f"Discrepancy for ID {rid}: status {acc} allowed download"
        elif http_status == 403:
            download_restricted_count += 1
            dl_flag = "BLOCKED (403 Forbidden)"
            # Ensure the resource is actually restricted
            assert acc in ("Read Online", "Restricted Access", "Metadata Only") or not redis, f"Discrepancy for ID {rid}: status {acc} was blocked"
        else:
            dl_flag = f"UNEXPECTED ({http_status})"

        print(f"ID {rid:2d} | {acc:18s} | {lic:24s} | {dl_flag:24s} | {title}")

    print(f"==================================================")
    print(f"AUDIT SUMMARY:")
    print(f"  Direct File Downloads Permitted:  {download_allowed_count} (Public Domain / Verified Open Access)")
    print(f"  Direct File Downloads Restricted: {download_restricted_count} (In-Copyright Read Online / Fair Use / Restricted)")
    print(f"  Total Verified:                   {len(rows)}")
    print(f"==================================================")

if __name__ == "__main__":
    audit()
