import os
import sys
from pathlib import Path

# Add backend directory and root directory to python path
current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
backend_dir = root_dir / "backend"

sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(root_dir))

# When deployed on Vercel serverless, /tmp is writable for SQLite
if os.environ.get("VERCEL"):
    os.environ.setdefault("DATABASE_URL", "sqlite:////tmp/iks_repository.db")

from app.main import app, init_db
from app.database.session import SessionLocal, engine, Base
from app.models import Resource
import logging

logger = logging.getLogger("vercel_app")

# Ensure DB initialized & seeded if empty on cold start
try:
    init_db()
    db = SessionLocal()
    try:
        count = db.query(Resource).count()
        if count == 0:
            from scripts.seed_data import seed_database
            seed_database()
    finally:
        db.close()
except Exception as e:
    logger.warning(f"Serverless initialization note: {e}")

# Vercel serverless expects 'app'
