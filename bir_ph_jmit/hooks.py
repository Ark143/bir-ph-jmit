"""
BIR PH JMIT - Frappe App Hooks Configuration
Standard Bureau of Internal Revenue (BIR) Philippines Reports for ERPNext v15
"""

app_name = "bir_ph_jmit"
app_title = "BIR PH JMIT"
app_publisher = "JMIT"
app_description = "Standard Bureau of Internal Revenue (BIR) Philippines Reports for ERPNext v15 CAS Application"
app_icon = "octicon octicon-file-directory"
app_color = "#1e90ff"
app_email = "support@jmit.ph"
app_license = "MIT"
app_version = "1.0.0"

# Frappe Version Requirement
minimum_frappe_version = "14.0"
minimum_erpnext_version = "15.0"

# Web asset configuration - explicitly disabled
# This is a backend/report-only app with no frontend assets
has_website = False
has_web_assets = False

# Build configuration - no JavaScript or CSS bundles
# This tells esbuild that there's nothing to build for this app
build_command_configurations = {
    "bir_ph_jmit": {
        "entry": {},
        "output": {}
    }
}

# Installation Hooks
before_app_install = "bir_ph_jmit.install.before_app_install"
after_app_install = "bir_ph_jmit.install.after_app_install"
before_app_uninstall = "bir_ph_jmit.install.before_app_uninstall"
after_app_uninstall = "bir_ph_jmit.install.after_app_uninstall"

# Fixtures - to be exported and synchronized
fixtures = [
    {"doctype": "Report", "filters": [["Report", "module", "=", "BIRReports"]]},
    {"doctype": "Module Def", "filters": [["Module Def", "module_name", "=", "BIRReports"]]}
]

# Report List
report_list = [
    "Sales Register",
    "Purchase Register",
    "Monthly Tax Compliance",
    "Summary of Sales, Purchases and Creditable Withholding Taxes",
    "Creditable Withholding Tax",
    "Final Withholding Tax",
    "Expanded Withholding Tax",
    "VAT Reconciliation",
    "Income Tax Withholding"
]

# Apps that will be installed before this app
required_apps = ["frappe", "erpnext"]

# Autoload
auto_load_doctypes = True
auto_load_reports = True

# Desk Sidebar
desk_sidebar_items = "bir_ph_jmit.desk.get_sidebar_items"

# Document Events
doc_events = {}

# Scheduler Events
scheduler_events = {
    "cron": {
        "0 0 1 * *": [
            "bir_ph_jmit.tasks.generate_monthly_reports"
        ]
    }
}
