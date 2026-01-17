"""
Scheduled Tasks for BIR Reports
"""

import frappe
from datetime import datetime
from frappe.utils import get_first_day, get_last_day


def generate_monthly_reports():
    """
    Generate monthly BIR reports automatically
    """
    today = datetime.now()
    month_start = get_first_day(today)
    month_end = get_last_day(today)
    
    companies = frappe.get_all("Company", fields=["name"])
    
    for company in companies:
        try:
            # Generate Sales Register
            generate_sales_register(company['name'], month_start, month_end)
            
            # Generate Purchase Register
            generate_purchase_register(company['name'], month_start, month_end)
            
            # Generate Monthly Tax Compliance
            generate_monthly_tax_compliance(company['name'], today.year)
            
            frappe.db.commit()
        except Exception as e:
            frappe.log_error(f"Error generating reports for {company['name']}: {str(e)}")


def generate_sales_register(company, from_date, to_date):
    """
    Generate Sales Register report
    """
    from bir_ph_jmit.modules.BIRReports.report.sales_register import execute
    
    filters = {
        "company": company,
        "from_date": from_date,
        "to_date": to_date
    }
    
    columns, data = execute(filters)
    frappe.log_error(f"Sales Register generated for {company} with {len(data)} records", "BIR Report Generation")


def generate_purchase_register(company, from_date, to_date):
    """
    Generate Purchase Register report
    """
    from bir_ph_jmit.modules.BIRReports.report.purchase_register import execute
    
    filters = {
        "company": company,
        "from_date": from_date,
        "to_date": to_date
    }
    
    columns, data = execute(filters)
    frappe.log_error(f"Purchase Register generated for {company} with {len(data)} records", "BIR Report Generation")


def generate_monthly_tax_compliance(company, year):
    """
    Generate Monthly Tax Compliance report
    """
    from bir_ph_jmit.modules.BIRReports.report.monthly_tax_compliance import execute
    
    filters = {
        "company": company,
        "year": year
    }
    
    columns, data = execute(filters)
    frappe.log_error(f"Monthly Tax Compliance generated for {company}", "BIR Report Generation")
