@echo off
title IKS Frontend Client (Vite)
echo ========================================================
echo Starting IKS Digital Repository Frontend on port 5173...
echo Portal URL: http://localhost:5173
echo ========================================================
set "PATH=C:\Users\shiva\.gemini\antigravity\scratch\nodejs\node-v20.18.1-win-x64;%PATH%"
cd /d "%~dp0frontend"
call npm run dev
pause
