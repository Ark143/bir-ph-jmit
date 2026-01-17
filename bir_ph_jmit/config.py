"""
BIR Reports Configuration
Configuration settings for BIR Philippines reports
"""

# BIR Report Configuration
BIR_REPORT_CONFIG = {
    "sales_register": {
        "name": "Sales Register",
        "label": "Sales Register (SAR)",
        "description": "Bureau of Internal Revenue Sales Register Report",
        "module": "BIRReports",
        "doctype": "Sales Invoice"
    },
    "purchase_register": {
        "name": "Purchase Register",
        "label": "Purchase Register (PAR)",
        "description": "Bureau of Internal Revenue Purchase Register Report",
        "module": "BIRReports",
        "doctype": "Purchase Invoice"
    },
    "monthly_tax_compliance": {
        "name": "Monthly Tax Compliance",
        "label": "Monthly Tax Compliance Report",
        "description": "Monthly VAT and Tax Compliance Report",
        "module": "BIRReports"
    },
    "summary_sales_purchases": {
        "name": "Summary of Sales, Purchases and Creditable Withholding Taxes",
        "label": "Summary of Sales, Purchases and CWT (Form 2550M)",
        "description": "BIR Form 2550M - Summary Report",
        "module": "BIRReports"
    },
    "creditable_withholding_tax": {
        "name": "Creditable Withholding Tax",
        "label": "Creditable Withholding Tax Report",
        "description": "CWT Report for Input Tax Credits",
        "module": "BIRReports",
        "doctype": "Purchase Invoice"
    },
    "final_withholding_tax": {
        "name": "Final Withholding Tax",
        "label": "Final Withholding Tax Report",
        "description": "Final Tax Withholding Report",
        "module": "BIRReports"
    },
    "expanded_withholding_tax": {
        "name": "Expanded Withholding Tax",
        "label": "Expanded Withholding Tax (Form 2307)",
        "description": "EWT Report for Professional Services",
        "module": "BIRReports"
    },
    "vat_reconciliation": {
        "name": "VAT Reconciliation",
        "label": "VAT Reconciliation Report",
        "description": "VAT Reconciliation and Analysis",
        "module": "BIRReports"
    },
    "income_tax_withholding": {
        "name": "Income Tax Withholding",
        "label": "Income Tax Withholding Report",
        "description": "Income Tax Withholding Summary",
        "module": "BIRReports"
    }
}

# VAT Configuration
VAT_RATES = {
    "standard": 0.12,      # 12% standard VAT
    "zero_rated": 0.0,     # 0% for export, etc.
    "exempt": 0.0          # Exempt from VAT
}

# Withholding Tax Rates
WITHHOLDING_TAX_RATES = {
    "purchases": 0.02,              # 2% on purchases
    "professional_fees": 0.05,      # 5% on professional fees
    "talent_fees": 0.05,            # 5% on talent fees
    "commission": 0.10,             # 10% on commissions
    "rent": 0.05,                   # 5% on rent
    "contractor": 0.02,             # 2% on contractors
}

# Report Parameters
REPORT_PARAMETERS = {
    "date_range": {
        "type": "Date Range",
        "required": True,
        "label": "Report Period"
    },
    "company": {
        "type": "Link",
        "doctype": "Company",
        "required": True,
        "label": "Company"
    }
}

# Export Formats
EXPORT_FORMATS = {
    "csv": {
        "label": "CSV Format",
        "extension": ".csv"
    },
    "pdf": {
        "label": "PDF Format",
        "extension": ".pdf"
    },
    "excel": {
        "label": "Excel Format",
        "extension": ".xlsx"
    }
}
