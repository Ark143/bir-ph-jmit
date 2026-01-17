"""
BIR PH JMIT - Quick Deployment Guide for Frappe Cloud
"""

# BIR PH JMIT - Frappe Cloud Deployment

## Quick Start (5 minutes)

### Prerequisites
- GitHub account (or other Git provider)
- Frappe Cloud site
- Git installed locally

### Step 1: Initialize Git Repository

```bash
cd c:\Users\josem\Desktop\eprnext\birreportjmit
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
git add .
git commit -m "Initial commit - BIR PH JMIT v1.0.0"
```

### Step 2: Push to GitHub

1. Go to https://github.com/new and create a new repository
   - Repository name: `bir-ph-jmit`
   - Description: "Standard Bureau of Internal Revenue (BIR) Philippines Reports for ERPNext v15"
   - Make it **Public** (required for Frappe)

2. Push your code:
```bash
git remote add origin https://github.com/yourusername/bir-ph-jmit.git
git branch -M main
git push -u origin main
```

### Step 3: Install on Frappe Cloud

1. Open terminal/command prompt

2. Connect to your Frappe Cloud bench:
```bash
# SSH into your Frappe Cloud instance
ssh frappe@your-frappe-cloud-instance
cd frappe-bench
```

3. Install the app:
```bash
# Get the app
bench get-app bir-ph-jmit https://github.com/yourusername/bir-ph-jmit.git

# Install on your site
bench install-app bir_ph_jmit --site your-site-name.frappe.cloud

# Run database migrations
bench migrate --site your-site-name.frappe.cloud

# Restart services (optional, Frappe usually auto-restarts)
bench restart
```

### Step 4: Verify Installation

1. Go to your Frappe Cloud site: `https://your-site-name.frappe.cloud`

2. Navigate to **BIR Reports** module

3. You should see reports available:
   - Sales Register
   - Purchase Register
   - Monthly Tax Compliance
   - And more...

## Troubleshooting

### App not appearing in modules

```bash
bench --site your-site-name.frappe.cloud console
# Then run:
frappe.db.sql("INSERT INTO `tabModule Def` (`module_name`, `module_label`) VALUES ('BIRReports', 'BIR Reports')")
```

### Permission denied when installing

Ensure you have proper permissions on your Frappe Cloud instance. Contact your Frappe Cloud administrator.

### Reports showing no data

1. Check if you have Sales/Purchase Invoices in your system
2. Ensure invoices are **submitted**
3. Verify the date range filters include your invoices

## File Structure on Frappe Cloud

```
apps/
└── bir-ph-jmit/
    ├── bir_ph_jmit/
    │   ├── modules/
    │   │   └── BIRReports/
    │   │       ├── report/          # All 9 BIR reports
    │   │       ├── api/             # API utilities
    │   │       └── doctype/         # DocTypes
    │   ├── config.py                # Configuration
    │   ├── install.py               # Installation hooks
    │   └── tasks.py                 # Scheduled tasks
    ├── hooks.py                     # Frappe hooks
    └── setup.py                     # Setup configuration
```

## Backup Before Installation

It's recommended to create a backup before installing:

```bash
bench --site your-site-name.frappe.cloud backup
```

## Updating the App

When you have new updates:

```bash
cd /path/to/frappe-bench
bench update
# or
bench update-app bir-ph-jmit
```

## Version Information

- **App Version**: 1.0.0
- **ERPNext Version Required**: 15.0+
- **Frappe Version Required**: 14.0+
- **Python Version**: 3.7+

## Support

For issues or questions:
- Email: support@jmit.ph
- GitHub Issues: https://github.com/yourusername/bir-ph-jmit/issues

---

**Created**: January 18, 2026
**Status**: Production Ready
