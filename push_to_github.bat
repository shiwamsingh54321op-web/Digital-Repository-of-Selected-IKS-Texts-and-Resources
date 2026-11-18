@echo off
title Push IKS Repository to GitHub
echo ========================================================
echo Pushing IKS Digital Repository to:
echo https://github.com/shiwamsingh54321op-web/Digital-Repository-of-Selected-IKS-Texts-and-Resources.git
echo ========================================================
cd /d "%~dp0"
git push -u origin main
echo ========================================================
if %ERRORLEVEL% EQU 0 (
    echo SUCCESS: Repository successfully pushed to GitHub!
) else (
    echo NOTE: If authentication is required, enter your GitHub Personal Access Token or credentials above.
)
echo ========================================================
pause
