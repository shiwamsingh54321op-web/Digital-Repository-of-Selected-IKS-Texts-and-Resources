@echo off
title Push IKS Repository with Personal Access Token
color 0A
echo ===============================================================================
echo          INDIAN KNOWLEDGE SYSTEMS (IKS) DIGITAL REPOSITORY
echo                 Push to GitHub with Access Token
echo ===============================================================================
echo Target: https://github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources.git
echo.
echo If you don't have a token yet:
echo 1. Open: https://github.com/settings/tokens
echo 2. Click "Generate new token" -> "Generate new token (classic)"
echo 3. Check the "repo" box and click "Generate token"
echo 4. Copy the generated token (starts with ghp_...)
echo ===============================================================================
echo.
set /p TOKEN="Paste your GitHub Personal Access Token here: "

if "%TOKEN%"=="" (
    echo [ERROR] No token entered.
    pause
    exit /b 1
)

echo.
echo Pushing repository to GitHub...
cd /d "%~dp0"
git push https://%TOKEN%@github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources.git main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===============================================================================
    echo SUCCESS: Repository successfully pushed to GitHub!
    echo Check your repository: https://github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources
    echo ===============================================================================
) else (
    echo.
    echo [ERROR] Push failed. Please make sure the token is valid and has "repo" scope.
)

echo.
pause
