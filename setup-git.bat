@echo off
REM BIR PH JMIT - Git Setup and Initial Commit Script (Windows)
REM Run this script to initialize git, commit, and push to GitHub

echo.
echo ========================================
echo BIR PH JMIT - Git Setup Script (Windows)
echo ========================================
echo.

REM Initialize git repository
echo Initializing git repository...
git init
if errorlevel 1 (
    echo Error: Git is not installed. Please install Git from https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Configure git (update these with your details)
echo.
echo Configuring git...
git config user.name "Your Name"
git config user.email "your.email@example.com"

REM Add all files
echo.
echo Adding all files...
git add .

REM Create initial commit
echo.
echo Creating initial commit...
git commit -m "Initial commit - BIR PH JMIT v1.0.0 - Complete ERPNext v15 app with 9 BIR Philippines reports"

REM Display status
echo.
echo Commit created successfully!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub at https://github.com/new
echo 2. Name it: bir-ph-jmit
echo 3. Copy the repository URL
echo 4. Run one of these commands:
echo.
echo Option A - Set remote and push in one go:
echo   git remote add origin https://github.com/YOUR-USERNAME/bir-ph-jmit.git
echo   git branch -M main
echo   git push -u origin main
echo.
echo Option B - If repo already has commits:
echo   git remote add origin https://github.com/YOUR-USERNAME/bir-ph-jmit.git
echo   git branch -M main
echo   git push -u origin main --force
echo.
echo For more details, see: FRAPPE_CLOUD_DEPLOYMENT.md
echo.
pause
