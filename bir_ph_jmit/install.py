"""
Installation and Setup for BIR PH JMIT App
"""

import frappe
from frappe import _


def before_app_install():
    """
    Run before app installation
    """
    pass


def after_app_install():
    """
    Run after app installation
    Create module definition and set up necessary permissions
    """
    create_bir_reports_module()
    setup_permissions()


def create_bir_reports_module():
    """
    Create BIRReports Module Definition if not exists
    """
    if not frappe.db.exists("Module Def", "BIRReports"):
        module_doc = frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "BIRReports",
            "module_label": "BIR Reports",
            "disabled": 0
        })
        module_doc.insert(ignore_permissions=True)
        frappe.db.commit()


def setup_permissions():
    """
    Set up permissions for BIR reports
    """
    # Grant read permission to Accountant role
    roles_to_grant = ["Accountant", "Administrator", "Finance Manager"]
    
    for report_name in [
        "Sales Register",
        "Purchase Register",
        "Monthly Tax Compliance",
        "Summary of Sales, Purchases and Creditable Withholding Taxes",
        "Creditable Withholding Tax",
        "Final Withholding Tax",
        "Expanded Withholding Tax",
        "VAT Reconciliation",
        "Income Tax Withholding"
    ]:
        if frappe.db.exists("Report", report_name):
            for role in roles_to_grant:
                frappe.db.sql("""
                    INSERT IGNORE INTO `tabHas Role` (parent, role)
                    SELECT %s, %s
                    WHERE NOT EXISTS (
                        SELECT 1 FROM `tabHas Role` 
                        WHERE parent = %s AND role = %s
                    )
                """, (report_name, role, report_name, role))
            frappe.db.commit()


def before_app_uninstall():
    """
    Run before app uninstallation
    """
    pass


def after_app_uninstall():
    """
    Run after app uninstallation
    Clean up created objects
    """
    pass
