"""
BIR PH JMIT - How to Commit and Push to GitHub
"""

# 📝 How to Commit and Push This Project

I've created setup scripts for you. Choose the one that matches your system:

## Option 1: PowerShell (Recommended for Windows)

1. Open PowerShell in the project directory:
```powershell
cd "c:\Users\josem\Desktop\eprnext\birreportjmit"
```

2. Run the setup script:
```powershell
.\setup-git.ps1
```

3. Follow the on-screen instructions

## Option 2: Command Prompt (CMD)

1. Open Command Prompt (cmd.exe) in the project directory:
```cmd
cd c:\Users\josem\Desktop\eprnext\birreportjmit
```

2. Run the batch script:
```cmd
setup-git.bat
```

3. Follow the on-screen instructions

## Option 3: Manual Commands (Any Terminal with Git)

```bash
cd "c:\Users\josem\Desktop\eprnext\birreportjmit"

# Initialize git
git init

# Configure git (use your own name/email)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit - BIR PH JMIT v1.0.0"

# View commit log
git log
```

## After Commit: Push to GitHub

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `bir-ph-jmit`
3. Make it **PUBLIC** (required for Frappe)
4. Click "Create repository"
5. Copy your repository URL

### Step 2: Add Remote and Push

```bash
# Replace YOUR-USERNAME with your GitHub username
git remote add origin https://github.com/YOUR-USERNAME/bir-ph-jmit.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Verify Success

After pushing, you should see:
```
✓ Everything up-to-date
✓ Branch 'main' set up to track remote branch 'main' from 'origin'.
```

Then visit: `https://github.com/YOUR-USERNAME/bir-ph-jmit`

You should see all your files there! ✅

## Next: Deploy to Frappe Cloud

Once pushed to GitHub, follow the instructions in:
- `FRAPPE_CLOUD_DEPLOYMENT.md` - Step-by-step Frappe Cloud guide
- `INSTALLATION_GUIDE.md` - Complete installation reference

---

## Common Issues

### "git is not recognized"
- Git is not installed
- Solution: Install from https://git-scm.com/download/win
- Restart your terminal after installing

### "fatal: not a git repository"
- You're not in the project directory
- Solution: Make sure you're in `c:\Users\josem\Desktop\eprnext\birreportjmit`

### "Permission denied" when pushing
- Your GitHub account doesn't have permission
- Solution: Use SSH key or GitHub token (see GitHub docs)

### Repository already exists error
- You already pushed to GitHub
- Solution: This is fine! Just keep pushing with `git push`

---

## Files Included

The project has **36 files** ready to commit:
- 9 BIR Reports
- 6 Documentation files
- Complete Frappe app structure
- Installation hooks
- API utilities

See `FILE_STRUCTURE.md` for complete file listing.

---

## Git Workflow Going Forward

After initial commit:

```bash
# Check status
git status

# Make changes...

# Stage changes
git add .

# Create commit
git commit -m "Description of changes"

# Push to GitHub
git push
```

---

## Support

If you need help:
1. Check `FRAPPE_CLOUD_DEPLOYMENT.md`
2. Review `INSTALLATION_GUIDE.md`
3. See `README.md` for overview

---

**Choose your option above and let's get this committed!** 🚀
