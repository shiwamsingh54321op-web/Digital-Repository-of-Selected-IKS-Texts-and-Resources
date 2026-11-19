@echo off
title Push IKS Digital Repository to GitHub
color 0B
echo ===============================================================================
echo          INDIAN KNOWLEDGE SYSTEMS (IKS) DIGITAL REPOSITORY
echo                     GitHub Repository Push Tool
echo ===============================================================================
echo Target Remote: https://github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources.git
echo Branch:        main
echo ===============================================================================
echo.

cd /d "%~dp0"

echo [1/2] Attempting push via Git Credential Manager (Browser Login)...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===============================================================================
    echo SUCCESS: Repository successfully pushed to GitHub!
    echo View online: https://github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources
    echo ===============================================================================
    pause
    exit /b 0
)

echo.
echo [!] Browser login was cancelled or not authenticated.
echo.
echo ===============================================================================
echo OPTION B: Authenticate with a GitHub Personal Access Token (PAT)
echo ===============================================================================
echo If you have a Personal Access Token:
echo 1. Go to https://github.com/settings/tokens
echo 2. Generate a token (classic) with 'repo' scope
echo 3. Paste it below
echo ===============================================================================
echo.
set /p GITHUB_TOKEN="Enter your GitHub Personal Access Token (or press Enter to cancel): "

if "%GITHUB_TOKEN%"=="" (
    echo Push cancelled.
    pause
    exit /b 1
)

echo.
echo Pushing with provided Personal Access Token...
git push https://%GITHUB_TOKEN%@github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources.git main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===============================================================================
    echo SUCCESS: Repository successfully pushed to GitHub!
    echo ===============================================================================
) else (
    echo.
    echo [ERROR] Push failed. Please verify that your token has 'repo' write permissions.
)

echo.
pause
