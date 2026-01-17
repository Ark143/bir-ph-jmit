# BIR PH JMIT - ERPNext v15 App

## Overview

BIR PH JMIT is a comprehensive ERPNext v15 application designed to generate standard Bureau of Internal Revenue (BIR) Philippines reports. This app is tailored for CAS (Computerized Accounting System) Applications and provides all necessary BIR compliance reports.

## Quick Start

**New to BIR PH JMIT?** Start here: [QUICK_START.md](QUICK_START.md) - Get running in 5 minutes!

## Features

- Standard BIR Philippines Reports
- CAS Application Compliance
- ERPNext v15 Compatible
- Hosted on Frappe Cloud
- 9 Standard Reports
- Multiple Export Formats (CSV, PDF, Excel)
- Automated VAT Calculations

## Installation

1. Clone the repository into your Frappe bench apps directory:
```bash
cd /home/frappe/frappe-bench
bench get-app bir-ph-jmit https://github.com/yourusername/bir-ph-jmit.git
```

2. Install the app on your site:
```bash
bench install-app bir_ph_jmit --site your-site-name.frappe.cloud
```

3. Migrate your database:
```bash
bench migrate --site your-site-name.frappe.cloud
```

## BIR Reports Included

### Sales and Purchases
- Sales Register (SAR)
- Purchase Register (PAR)
- Sales and Purchases Summary

### Tax Reports
- Sales Tax Report
- Purchase Tax Report
- Tax Adjustment Report

### Compliance Reports
- Monthly Tax Compliance Report
- Quarterly VAT Report
- Annual Income Tax Report

### Deduction Reports
- Creditable Withholding Tax
- Final Withholding Tax
- Expanded Withholding Tax

### Other Reports
- Daily Sales Inventory Report
- Excise Tax Report
- Special Audit Report

## Requirements

- ERPNext v15.0 or higher
- Frappe Framework v14.0 or higher
- Python 3.7+

## Usage

1. Navigate to the BIR Reports module in your ERPNext instance
2. Select the desired report
3. Configure report parameters (date range, filters, etc.)
4. Generate and export report

## Support

For issues, questions, or feature requests, please visit:
https://github.com/yourusername/bir-ph-jmit/issues

## License

MIT License - See LICENSE file for details

## Author

JMIT - Enterprise Solutions
Email: support@jmit.ph

## Changelog

### Version 1.0.0
- Initial release
- Core BIR reports implementation
- CAS application compliance features
