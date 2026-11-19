@echo off
title Deploy IKS Digital Repository to Vercel
color 0B
echo ===============================================================================
echo          INDIAN KNOWLEDGE SYSTEMS (IKS) DIGITAL REPOSITORY
echo                    Vercel Cloud Deployment Tool
echo ===============================================================================
echo.

set "PATH=C:\Users\shiva\.gemini\antigravity\scratch\nodejs\node-v20.18.1-win-x64;%PATH%"
cd /d "%~dp0"

echo [1/3] Building latest production assets...
cd frontend
call npm run build
cd ..

echo.
echo [2/3] Checking Vercel Authentication...
cd frontend\dist
copy /Y "..\vercel.json" "vercel.json" >nul

call vercel whoami >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Please log in to Vercel (your default browser will open):
    call vercel login
)

echo.
echo [3/3] Deploying production build to Vercel...
call vercel deploy --prod

echo.
echo ===============================================================================
echo Deployment finished! Your site is live on Vercel.
echo ===============================================================================
pause
