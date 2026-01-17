"""
Monthly Tax Compliance Report
Bureau of Internal Revenue - Philippine Standard
"""

from frappe import _
from frappe.utils import get_first_day, get_last_day
from datetime import datetime

def execute(filters=None):
    """
    Generate Monthly Tax Compliance Report
    """
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    """Define report columns"""
    return [
        {
            "fieldname": "month",
            "label": _("Month"),
            "fieldtype": "Data",
            "width": 100
        },
        {
            "fieldname": "gross_sales",
            "label": _("Gross Sales"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "output_vat",
            "label": _("Output VAT"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "input_vat",
            "label": _("Input VAT"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "vat_payable",
            "label": _("VAT Payable/(Refundable)"),
            "fieldtype": "Currency",
            "width": 180
        },
        {
            "fieldname": "gross_purchases",
            "label": _("Gross Purchases"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "status",
            "label": _("Compliance Status"),
            "fieldtype": "Data",
            "width": 120
        }
    ]


def get_data(filters):
    """
    Fetch data for Monthly Tax Compliance Report
    """
    import frappe
    
    company = filters.get("company")
    year = filters.get("year") or datetime.now().year
    
    data = []
    
    for month in range(1, 13):
        month_start = get_first_day(datetime(year, month, 1))
        month_end = get_last_day(datetime(year, month, 1))
        
        # Get sales data
        sales_query = f"""
            SELECT
                COALESCE(SUM(total), 0) as gross_sales,
                COALESCE(SUM(total_taxes_and_charges), 0) as output_vat
            FROM `tabSales Invoice`
            WHERE docstatus = 1 
                AND company = '{company}'
                AND posting_date BETWEEN '{month_start}' AND '{month_end}'
        """
        
        sales = frappe.db.sql(sales_query, as_dict=True)[0]
        
        # Get purchase data
        purchase_query = f"""
            SELECT
                COALESCE(SUM(total), 0) as gross_purchases,
                COALESCE(SUM(total_taxes_and_charges), 0) as input_vat
            FROM `tabPurchase Invoice`
            WHERE docstatus = 1 
                AND company = '{company}'
                AND posting_date BETWEEN '{month_start}' AND '{month_end}'
        """
        
        purchases = frappe.db.sql(purchase_query, as_dict=True)[0]
        
        vat_payable = sales['output_vat'] - purchases['input_vat']
        status = "Filed" if vat_payable > 0 else "Pending Refund"
        
        data.append({
            "month": datetime(year, month, 1).strftime("%B %Y"),
            "gross_sales": sales['gross_sales'],
            "output_vat": sales['output_vat'],
            "input_vat": purchases['input_vat'],
            "vat_payable": vat_payable,
            "gross_purchases": purchases['gross_purchases'],
            "status": status
        })
    
    return data
