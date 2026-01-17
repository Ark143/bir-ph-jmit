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

# Installation Hooks
# --------
before_app_install = "bir_ph_jmit.install.before_app_install"
after_app_install = "bir_ph_jmit.install.after_app_install"
before_app_uninstall = "bir_ph_jmit.install.before_app_uninstall"
after_app_uninstall = "bir_ph_jmit.install.after_app_uninstall"

# Include app js, css files in header of desk.html
# app_include_css = "/assets/bir_ph_jmit/css/bir_ph_jmit.css"
# app_include_js = "/assets/bir_ph_jmit/js/bir_ph_jmit.js"

# include app js, css files in header of web template
# web_include_css = "/assets/bir_ph_jmit/css/bir_ph_jmit.css"
# web_include_js = "/assets/bir_ph_jmit/js/bir_ph_jmit.js"

# include custom scss in every page
# app_include_scss = "bir_ph_jmit/public/scss/index.scss"

# Add python path of this app to default app python path
# sys.path.insert(0, '/path/to/this/app')

# Includes in <head>
# ------------------

# header js includes
# app_include_js = "/assets/bir_ph_jmit/js/bir_ph_jmit.js"

# include js file in page
# page_js = {"page" : "public/js/file.js"}

# include css file in page
# page_css = {"page" : "public/css/file.css"}

# include css in every page
# website_include_css = "/assets/bir_ph_jmit/css/website.css"

# include js in every page
# website_include_js = "/assets/bir_ph_jmit/js/website.js"

# Fixtures
# --------
# Fixtures are used to export doctypes, roles, desk setups, etc. in a version-controlled manner
fixtures = [
    {"doctype": "Report", "filters": [["Report", "module", "=", "BIRReports"]]},
    {"doctype": "Module Def", "filters": [["Module Def", "module_name", "=", "BIRReports"]]}
]

# Report List
# --------
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
# --------
auto_load_doctypes = True
auto_load_reports = True

# Desk Sidebar
# -----------
desk_sidebar_items = "bir_ph_jmit.desk.get_sidebar_items"
