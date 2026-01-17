"""
BIR Reports API Utilities
Utility functions for generating BIR reports
"""

import frappe
from frappe import _


def get_company_ein(company):
    """
    Get company EIN (Employer Identification Number)
    """
    company_doc = frappe.get_doc("Company", company)
    return getattr(company_doc, 'tax_id', 'N/A')


def get_company_address(company):
    """
    Get company address
    """
    company_doc = frappe.get_doc("Company", company)
    return {
        "street": getattr(company_doc, 'street', ''),
        "city": getattr(company_doc, 'city', ''),
        "state": getattr(company_doc, 'state', ''),
        "postal_code": getattr(company_doc, 'postal_code', '')
    }


def validate_date_range(from_date, to_date):
    """
    Validate date range for reports
    """
    if from_date and to_date:
        if from_date > to_date:
            frappe.throw(_("From Date must be less than or equal to To Date"))
    return True


def get_sales_data(company, from_date, to_date, customer=None):
    """
    Get sales data for specified period
    """
    conditions = "WHERE docstatus = 1"
    conditions += f" AND company = '{company}'"
    
    if from_date:
        conditions += f" AND posting_date >= '{from_date}'"
    if to_date:
        conditions += f" AND posting_date <= '{to_date}'"
    if customer:
        conditions += f" AND customer = '{customer}'"
    
    query = f"""
        SELECT
            name,
            posting_date,
            customer,
            total,
            total_taxes_and_charges,
            net_total
        FROM `tabSales Invoice`
        {conditions}
        ORDER BY posting_date
    """
    
    return frappe.db.sql(query, as_dict=True)


def get_purchase_data(company, from_date, to_date, supplier=None):
    """
    Get purchase data for specified period
    """
    conditions = "WHERE docstatus = 1"
    conditions += f" AND company = '{company}'"
    
    if from_date:
        conditions += f" AND posting_date >= '{from_date}'"
    if to_date:
        conditions += f" AND posting_date <= '{to_date}'"
    if supplier:
        conditions += f" AND supplier = '{supplier}'"
    
    query = f"""
        SELECT
            name,
            posting_date,
            supplier,
            total,
            total_taxes_and_charges,
            net_total
        FROM `tabPurchase Invoice`
        {conditions}
        ORDER BY posting_date
    """
    
    return frappe.db.sql(query, as_dict=True)


def calculate_vat_summary(company, from_date, to_date):
    """
    Calculate VAT summary for period
    """
    sales = get_sales_data(company, from_date, to_date)
    purchases = get_purchase_data(company, from_date, to_date)
    
    total_sales = sum(s['total'] for s in sales)
    total_sales_vat = sum(s['total_taxes_and_charges'] for s in sales)
    
    total_purchases = sum(p['total'] for p in purchases)
    total_purchase_vat = sum(p['total_taxes_and_charges'] for p in purchases)
    
    vat_payable = total_sales_vat - total_purchase_vat
    
    return {
        "total_sales": total_sales,
        "sales_vat": total_sales_vat,
        "total_purchases": total_purchases,
        "purchase_vat": total_purchase_vat,
        "vat_payable": vat_payable
    }


def export_report_to_csv(report_data, report_name):
    """
    Export report data to CSV format
    """
    import csv
    from io import StringIO
    
    output = StringIO()
    
    if not report_data:
        return None
    
    writer = csv.DictWriter(output, fieldnames=report_data[0].keys())
    writer.writeheader()
    writer.writerows(report_data)
    
    return output.getvalue()


def export_report_to_pdf(report_data, report_name, company):
    """
    Export report data to PDF format
    """
    from frappe.utils.pdf import get_pdf
    
    # This would require a template and additional setup
    pass


@frappe.whitelist()
def get_bir_report_summary(company, year):
    """
    Get BIR report summary for the year
    """
    frappe.has_permission("Sales Invoice", "read")
    
    summary = {
        "company": company,
        "year": year,
        "reports": []
    }
    
    # Add quarterly summaries
    for quarter in range(1, 5):
        summary["reports"].append({
            "quarter": quarter,
            "status": "Pending"
        })
    
    return summary
