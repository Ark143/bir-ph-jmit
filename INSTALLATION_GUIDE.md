"""
BIR PH JMIT - Installation and Deployment Guide
"""

# BIR PH JMIT - Complete Setup Guide

## Project Overview

BIR PH JMIT is a comprehensive ERPNext v15 application that provides standard Bureau of Internal Revenue (BIR) Philippines reports for CAS (Computerized Accounting System) Applications.

## Installation Steps

### 1. Prerequisites
- ERPNext v15 or higher
- Frappe Framework v14.0 or higher
- Python 3.7 or higher
- Frappe Bench environment

### 2. Clone the App

```bash
cd /home/frappe/frappe-bench  # or your Frappe Bench directory
bench get-app bir-ph-jmit https://github.com/yourusername/bir-ph-jmit.git
```

For local development (if not in git yet):
```bash
cd apps/
git init bir-ph-jmit
cd bir-ph-jmit
# Copy all files from your local project
```

### 3. Install on Your Site

```bash
# For Frappe Cloud
bench install-app bir_ph_jmit --site your-site-name.frappe.cloud

# For Local Development
bench install-app bir_ph_jmit
```

### 4. Run Migrations

```bash
bench migrate --site your-site-name.frappe.cloud
# or
bench migrate
```

### 5. Restart Bench

```bash
bench restart
# or for specific site
bench --site your-site-name.frappe.cloud restart
```

## Application Structure

```
bir-ph-jmit/
├── bir_ph_jmit/                      # Main app directory
│   ├── __init__.py                   # App initialization
│   ├── config.py                     # App configuration
│   ├── desk.py                       # Desk sidebar configuration
│   ├── install.py                    # Installation hooks
│   ├── tasks.py                      # Scheduled tasks
│   ├── modules/
│   │   ├── __init__.py
│   │   └── BIRReports/              # Main module
│   │       ├── __init__.py
│   │       ├── module_def.json       # Module definition
│   │       ├── api/
│   │       │   ├── __init__.py
│   │       │   └── utils.py          # API utilities
│   │       ├── report/
│   │       │   ├── __init__.py
│   │       │   ├── sales_register.py
│   │       │   ├── purchase_register.py
│   │       │   ├── monthly_tax_compliance.py
│   │       │   ├── creditable_withholding_tax.py
│   │       │   ├── final_withholding_tax.py
│   │       │   ├── expanded_withholding_tax.py
│   │       │   ├── vat_reconciliation.py
│   │       │   └── income_tax_withholding.py
│   │       └── doctype/
│   │           └── __init__.py
│   └── public/
│       ├── js/
│       └── css/
├── hooks.py                         # Frappe hooks configuration
├── setup.py                         # Python setup configuration
├── pyproject.toml                   # Project configuration
├── MANIFEST.in                      # Package manifest
├── README.md                        # Documentation
├── LICENSE                          # MIT License
├── CHANGELOG.md                     # Version history
└── .gitignore                       # Git ignore rules
```

## Features Included

### Standard BIR Reports

1. **Sales Register (SAR)**
   - Document: sales_register.py
   - Shows all sales transactions with VAT breakdown
   - Filters by date range, company, customer

2. **Purchase Register (PAR)**
   - Document: purchase_register.py
   - Shows all purchase transactions with input VAT
   - Filters by date range, company, supplier

3. **Monthly Tax Compliance**
   - Document: monthly_tax_compliance.py
   - Monthly VAT and tax summary
   - Output and input VAT reconciliation

4. **Summary of Sales, Purchases and CWT (Form 2550M)**
   - Document: summary_sales_purchases_cwt.py
   - Quarterly summaries
   - Annual totals

5. **Creditable Withholding Tax (CWT)**
   - Document: creditable_withholding_tax.py
   - CWT transactions from purchases
   - Input tax credits

6. **Final Withholding Tax**
   - Document: final_withholding_tax.py
   - Final tax obligations
   - Tax rate tracking

7. **Expanded Withholding Tax (Form 2307)**
   - Document: expanded_withholding_tax.py
   - Professional services withholding
   - EWT compliance reporting

8. **VAT Reconciliation**
   - Document: vat_reconciliation.py
   - Sales VAT vs Purchase VAT
   - VAT payable/refundable analysis

9. **Income Tax Withholding**
   - Document: income_tax_withholding.py
   - Income tax withholding summary
   - Payment tracking

### API Utilities

Located in: [bir_ph_jmit/modules/BIRReports/api/utils.py](bir_ph_jmit/modules/BIRReports/api/utils.py)

- `get_company_ein()` - Get company EIN
- `get_company_address()` - Get company address
- `validate_date_range()` - Validate report date range
- `get_sales_data()` - Fetch sales data for period
- `get_purchase_data()` - Fetch purchase data for period
- `calculate_vat_summary()` - Calculate VAT summary
- `export_report_to_csv()` - Export to CSV
- `get_bir_report_summary()` - Get report summary

## Configuration

### VAT Rates (config.py)
- Standard VAT: 12%
- Zero-Rated: 0%
- Exempt: 0%

### Withholding Tax Rates
- Purchases: 2%
- Professional Fees: 5%
- Commissions: 10%
- Rent: 5%
- Contractors: 2%

## Usage

### Accessing Reports

1. Navigate to the BIR Reports module in your ERPNext instance
2. Select the desired report from the sidebar
3. Set report filters:
   - Company
   - Date range (From Date, To Date)
   - Additional filters (customer, supplier, etc.)
4. Click "Generate Report"
5. View or export the report

### Report Export Formats
- CSV - Comma-separated values
- PDF - Portable document format
- Excel - .xlsx spreadsheet format

## Permissions

### Role-Based Access
- **Administrator**: Full access to all reports
- **Accountant**: Read access to all reports
- **Finance Manager**: Read and write access

### Granting Permissions

Reports are automatically available to Accountant and Administrator roles upon installation.

## Troubleshooting

### Reports Not Showing
1. Verify app is installed: `bench list-apps`
2. Check if module is active in your site
3. Clear cache: `bench --site your-site clear-cache`

### Permission Denied Errors
1. Check user roles
2. Verify report permissions in Setup > Permissions
3. Clear user cache

### Data Not Appearing
1. Ensure invoices are submitted
2. Check date range filters
3. Verify company selection

## Support and Development

### For Issues
- GitHub Issues: https://github.com/yourusername/bir-ph-jmit/issues
- Email: support@jmit.ph

### Development Setup
1. Clone repository
2. Create virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Set up development bench

## Version History

### v1.0.0 (2026-01-18)
- Initial release
- All standard BIR reports included
- API utilities
- CAS application compatibility

## License

MIT License - See LICENSE file for details

## Author

JMIT - Enterprise Solutions
Email: support@jmit.ph
Website: https://www.jmit.ph

---

**Last Updated**: January 18, 2026
**Status**: Production Ready
