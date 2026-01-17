#!/usr/bin/env python3
"""
BIR PH JMIT - Application Verification Script
Verify app structure and configuration
"""

import os
import json
from pathlib import Path


def verify_app_structure():
    """Verify the complete app structure"""
    
    base_path = Path(__file__).parent
    required_files = {
        "hooks.py": "Frappe hooks configuration",
        "setup.py": "Python setup configuration",
        "pyproject.toml": "Project configuration",
        "README.md": "README documentation",
        "LICENSE": "License file",
        "CHANGELOG.md": "Changelog",
        "MANIFEST.in": "Package manifest",
        "INSTALLATION_GUIDE.md": "Installation guide",
        "bir_ph_jmit/__init__.py": "App initialization",
        "bir_ph_jmit/config.py": "App configuration",
        "bir_ph_jmit/desk.py": "Desk configuration",
        "bir_ph_jmit/install.py": "Installation hooks",
        "bir_ph_jmit/tasks.py": "Scheduled tasks",
        "bir_ph_jmit/modules/__init__.py": "Modules init",
        "bir_ph_jmit/modules/BIRReports/__init__.py": "BIR Reports module init",
        "bir_ph_jmit/modules/BIRReports/module_def.json": "Module definition",
        "bir_ph_jmit/modules/BIRReports/api/__init__.py": "API init",
        "bir_ph_jmit/modules/BIRReports/api/utils.py": "API utilities",
        "bir_ph_jmit/modules/BIRReports/report/__init__.py": "Reports init",
        "bir_ph_jmit/modules/BIRReports/report/sales_register.py": "Sales Register report",
        "bir_ph_jmit/modules/BIRReports/report/purchase_register.py": "Purchase Register report",
        "bir_ph_jmit/modules/BIRReports/report/monthly_tax_compliance.py": "Monthly Tax Compliance",
        "bir_ph_jmit/modules/BIRReports/report/creditable_withholding_tax.py": "CWT report",
        "bir_ph_jmit/modules/BIRReports/report/final_withholding_tax.py": "Final WT report",
        "bir_ph_jmit/modules/BIRReports/report/expanded_withholding_tax.py": "Expanded WT report",
        "bir_ph_jmit/modules/BIRReports/report/vat_reconciliation.py": "VAT Reconciliation",
        "bir_ph_jmit/modules/BIRReports/report/income_tax_withholding.py": "Income Tax Withholding",
        "bir_ph_jmit/modules/BIRReports/report/summary_sales_purchases_cwt.py": "Form 2550M",
        "bir_ph_jmit/modules/BIRReports/doctype/__init__.py": "Doctype init",
    }
    
    print("=" * 80)
    print("BIR PH JMIT - Application Verification")
    print("=" * 80)
    
    missing_files = []
    found_files = []
    
    for file_path, description in required_files.items():
        full_path = base_path / file_path
        if full_path.exists():
            found_files.append(f"✓ {file_path} ({description})")
        else:
            missing_files.append(f"✗ {file_path} ({description})")
    
    print("\nFile Verification:")
    print("-" * 80)
    
    for found in found_files:
        print(found)
    
    if missing_files:
        print("\nMissing Files:")
        print("-" * 80)
        for missing in missing_files:
            print(missing)
    
    print("\n" + "=" * 80)
    print(f"Total Files: {len(required_files)}")
    print(f"Found: {len(found_files)}")
    print(f"Missing: {len(missing_files)}")
    print("=" * 80)
    
    if len(missing_files) == 0:
        print("\n✓ All required files are present!")
        print("✓ Application structure is complete and ready for deployment!")
        return True
    else:
        print(f"\n✗ Missing {len(missing_files)} file(s)")
        print("✗ Please ensure all files are present before deployment!")
        return False


def verify_configuration():
    """Verify configuration files"""
    print("\n" + "=" * 80)
    print("Configuration Verification")
    print("=" * 80)
    
    base_path = Path(__file__).parent
    
    # Check hooks.py
    hooks_path = base_path / "hooks.py"
    if hooks_path.exists():
        with open(hooks_path, 'r') as f:
            content = f.read()
            checks = [
                ("app_name = \"bir_ph_jmit\"", "App name"),
                ("app_title = \"BIR PH JMIT\"", "App title"),
                ("minimum_erpnext_version = \"15.0\"", "ERPNext version"),
                ("after_app_install", "Installation hooks"),
            ]
            
            print("\nHooks.py Configuration:")
            print("-" * 80)
            for check_str, description in checks:
                if check_str in content:
                    print(f"✓ {description}")
                else:
                    print(f"✗ {description}")
    
    # Check pyproject.toml
    pyproject_path = base_path / "pyproject.toml"
    if pyproject_path.exists():
        print("\nProject Configuration:")
        print("-" * 80)
        print("✓ pyproject.toml is present")
    
    print("\n" + "=" * 80)


def summary():
    """Print summary"""
    print("\n" + "=" * 80)
    print("INSTALLATION SUMMARY")
    print("=" * 80)
    print("""
BIR PH JMIT Application has been successfully created!

Directory: c:\\Users\\josem\\Desktop\\eprnext\\birreportjmit

NEXT STEPS FOR FRAPPE CLOUD DEPLOYMENT:

1. Initialize Git Repository:
   cd c:\\Users\\josem\\Desktop\\eprnext\\birreportjmit
   git init
   git add .
   git commit -m "Initial commit - BIR PH JMIT v1.0.0"

2. Push to GitHub (or your Git provider):
   git remote add origin https://github.com/yourusername/bir-ph-jmit.git
   git push -u origin master

3. Install on Frappe Cloud:
   bench get-app bir-ph-jmit https://github.com/yourusername/bir-ph-jmit.git
   bench install-app bir_ph_jmit --site your-site-name.frappe.cloud
   bench migrate --site your-site-name.frappe.cloud

4. Access the Application:
   Navigate to your-site-name.frappe.cloud
   Go to BIR Reports module
   Start generating reports!

INCLUDED REPORTS:
- Sales Register (SAR)
- Purchase Register (PAR)
- Monthly Tax Compliance
- Form 2550M Summary
- Creditable Withholding Tax (CWT)
- Final Withholding Tax
- Expanded Withholding Tax (Form 2307)
- VAT Reconciliation
- Income Tax Withholding

DOCUMENTATION:
- README.md - Overview and features
- INSTALLATION_GUIDE.md - Detailed setup instructions
- CHANGELOG.md - Version history

SUPPORT:
- Email: support@jmit.ph
- GitHub: https://github.com/yourusername/bir-ph-jmit

Thank you for using BIR PH JMIT!
""")
    print("=" * 80)


if __name__ == "__main__":
    result = verify_app_structure()
    verify_configuration()
    summary()
    
    exit(0 if result else 1)
