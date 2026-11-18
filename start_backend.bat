@echo off
title IKS Backend Server (FastAPI)
echo ========================================================
echo Starting IKS Digital Repository Backend on port 8000...
echo API Docs will be at: http://127.0.0.1:8000/docs
echo ========================================================
cd /d "%~dp0backend"
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
pause
