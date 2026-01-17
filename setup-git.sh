#!/bin/bash
# BIR PH JMIT - Git Setup and Initial Commit Script
# Run this script to initialize git, commit, and push to GitHub

echo "🚀 BIR PH JMIT - Git Setup Script"
echo "=================================="
echo ""

# Initialize git repository
echo "📝 Initializing git repository..."
git init

# Configure git (optional - update these with your details)
echo ""
echo "⚙️  Configuring git..."
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
echo ""
echo "📦 Adding all files..."
git add .

# Create initial commit
echo ""
echo "💾 Creating initial commit..."
git commit -m "Initial commit - BIR PH JMIT v1.0.0 - Complete ERPNext v15 app with 9 BIR Philippines reports"

# Display status
echo ""
echo "✅ Commit created successfully!"
echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub at https://github.com/new"
echo "2. Name it: bir-ph-jmit"
echo "3. Copy the repository URL"
echo "4. Run this command (replace YOUR-REPO-URL):"
echo "   git remote add origin YOUR-REPO-URL"
echo "5. Push to GitHub:"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "Or run this to set remote and push in one go:"
echo "git remote add origin https://github.com/YOUR-USERNAME/bir-ph-jmit.git"
echo "git branch -M main"
echo "git push -u origin main"
