# BIR PH JMIT - Git Setup and Initial Commit Script (PowerShell)
# Run this script to initialize git, commit, and push to GitHub
# Usage: .\setup-git.ps1

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "BIR PH JMIT - Git Setup Script (PowerShell)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
try {
    $gitVersion = git --version
    Write-Host "✓ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Error: Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Step 1: Initializing git repository..." -ForegroundColor Yellow
git init
Write-Host ""

Write-Host "Step 2: Configuring git..." -ForegroundColor Yellow
Write-Host "Note: Update these with your actual details!" -ForegroundColor Gray
git config user.name "Your Name"
git config user.email "your.email@example.com"
Write-Host ""

Write-Host "Step 3: Adding all files..." -ForegroundColor Yellow
git add .
Write-Host "✓ Files added" -ForegroundColor Green
Write-Host ""

Write-Host "Step 4: Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit - BIR PH JMIT v1.0.0 - Complete ERPNext v15 app with 9 BIR Philippines reports"
Write-Host ""

Write-Host "========================================" -ForegroundColor Green
Write-Host "✓ Initial commit created successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "NEXT STEPS:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Create a new repository on GitHub:" -ForegroundColor Yellow
Write-Host "   → Go to https://github.com/new" -ForegroundColor Gray
Write-Host "   → Repository name: bir-ph-jmit" -ForegroundColor Gray
Write-Host "   → Make it PUBLIC" -ForegroundColor Gray
Write-Host "   → Copy the repository URL" -ForegroundColor Gray
Write-Host ""

Write-Host "2. Add remote and push to GitHub:" -ForegroundColor Yellow
Write-Host "   Replace YOUR-USERNAME with your GitHub username:" -ForegroundColor Gray
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR-USERNAME/bir-ph-jmit.git" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""

Write-Host "3. Deploy to Frappe Cloud:" -ForegroundColor Yellow
Write-Host "   See FRAPPE_CLOUD_DEPLOYMENT.md for detailed instructions" -ForegroundColor Gray
Write-Host ""

Write-Host "Useful Git Commands:" -ForegroundColor Cyan
Write-Host "  git status                    - Check status" -ForegroundColor Gray
Write-Host "  git log                       - View commit history" -ForegroundColor Gray
Write-Host "  git add .                     - Stage all changes" -ForegroundColor Gray
Write-Host "  git commit -m 'message'       - Create new commit" -ForegroundColor Gray
Write-Host "  git push                      - Push to GitHub" -ForegroundColor Gray
Write-Host ""

Write-Host "Documentation:" -ForegroundColor Cyan
Write-Host "  - README.md" -ForegroundColor Gray
Write-Host "  - QUICK_START.md" -ForegroundColor Gray
Write-Host "  - FRAPPE_CLOUD_DEPLOYMENT.md" -ForegroundColor Gray
Write-Host "  - INSTALLATION_GUIDE.md" -ForegroundColor Gray
Write-Host ""
