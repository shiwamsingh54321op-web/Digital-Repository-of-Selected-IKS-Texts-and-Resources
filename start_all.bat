@echo off
title IKS Digital Repository Launcher
echo ========================================================
echo Launching Digital Repository of Selected IKS Texts...
echo ========================================================
echo [1/3] Launching FastAPI Backend on Port 8000...
start "IKS Backend Server" cmd /c "%~dp0start_backend.bat"

timeout /t 3 /nobreak >nul

echo [2/3] Launching React+Vite Frontend on Port 5173...
start "IKS Frontend Client" cmd /c "%~dp0start_frontend.bat"

timeout /t 3 /nobreak >nul

echo [3/3] Opening Repository in Default Browser...
start http://localhost:5173

echo ========================================================
echo IKS Digital Repository is active!
echo Frontend: http://localhost:5173
echo Backend API Docs: http://127.0.0.1:8000/docs
echo Admin Login: http://localhost:5173/admin/login (admin / Admin@IKS2026!)
echo ========================================================
pause
