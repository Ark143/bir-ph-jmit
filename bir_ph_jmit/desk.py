"""
Desk Sidebar Configuration for BIR Reports
"""

import frappe


def get_sidebar_items():
    """
    Get sidebar items for BIR Reports module
    """
    return [
        {
            "type": "doctype",
            "doctype": "Sales Invoice",
            "label": "Sales Invoices",
            "description": "View and manage sales invoices"
        },
        {
            "type": "doctype",
            "doctype": "Purchase Invoice",
            "label": "Purchase Invoices",
            "description": "View and manage purchase invoices"
        },
        {
            "type": "report",
            "name": "Sales Register",
            "label": "Sales Register (SAR)",
            "description": "Bureau of Internal Revenue Sales Register"
        },
        {
            "type": "report",
            "name": "Purchase Register",
            "label": "Purchase Register (PAR)",
            "description": "Bureau of Internal Revenue Purchase Register"
        },
        {
            "type": "report",
            "name": "Monthly Tax Compliance",
            "label": "Monthly Tax Compliance",
            "description": "Monthly tax compliance report"
        },
        {
            "type": "report",
            "name": "Summary of Sales, Purchases and Creditable Withholding Taxes",
            "label": "Form 2550M Summary",
            "description": "BIR Form 2550M summary report"
        },
        {
            "type": "report",
            "name": "Creditable Withholding Tax",
            "label": "CWT Report",
            "description": "Creditable Withholding Tax report"
        },
        {
            "type": "report",
            "name": "Final Withholding Tax",
            "label": "Final WT Report",
            "description": "Final Withholding Tax report"
        },
        {
            "type": "report",
            "name": "Expanded Withholding Tax",
            "label": "EWT Report (2307)",
            "description": "Expanded Withholding Tax Form 2307"
        },
        {
            "type": "report",
            "name": "VAT Reconciliation",
            "label": "VAT Reconciliation",
            "description": "VAT reconciliation and analysis"
        },
        {
            "type": "report",
            "name": "Income Tax Withholding",
            "label": "Income Tax Withholding",
            "description": "Income tax withholding summary"
        }
    ]
