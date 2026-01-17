"""
Summary of Sales, Purchases and Creditable Withholding Taxes
Bureau of Internal Revenue Form 2550M
"""

from frappe import _
from frappe.utils import get_first_day, get_last_day
from datetime import datetime

def execute(filters=None):
    """
    Generate Summary of Sales, Purchases and Creditable Withholding Taxes Report
    """
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    """Define report columns"""
    return [
        {
            "fieldname": "category",
            "label": _("Category"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "first_quarter",
            "label": _("1st Quarter"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "second_quarter",
            "label": _("2nd Quarter"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "third_quarter",
            "label": _("3rd Quarter"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "fourth_quarter",
            "label": _("4th Quarter"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "annual_total",
            "label": _("Annual Total"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]


def get_quarterly_sales(company, year):
    """Get quarterly sales data"""
    import frappe
    quarters = {}
    
    for quarter in range(1, 5):
        start_month = (quarter - 1) * 3 + 1
        end_month = quarter * 3
        
        query = f"""
            SELECT
                COALESCE(SUM(total), 0) as sales
            FROM `tabSales Invoice`
            WHERE docstatus = 1 
                AND company = '{company}'
                AND YEAR(posting_date) = {year}
                AND MONTH(posting_date) BETWEEN {start_month} AND {end_month}
        """
        
        result = frappe.db.sql(query, as_dict=True)[0]
        quarters[f"q{quarter}"] = result['sales']
    
    return quarters


def get_quarterly_purchases(company, year):
    """Get quarterly purchase data"""
    import frappe
    quarters = {}
    
    for quarter in range(1, 5):
        start_month = (quarter - 1) * 3 + 1
        end_month = quarter * 3
        
        query = f"""
            SELECT
                COALESCE(SUM(total), 0) as purchases
            FROM `tabPurchase Invoice`
            WHERE docstatus = 1 
                AND company = '{company}'
                AND YEAR(posting_date) = {year}
                AND MONTH(posting_date) BETWEEN {start_month} AND {end_month}
        """
        
        result = frappe.db.sql(query, as_dict=True)[0]
        quarters[f"q{quarter}"] = result['purchases']
    
    return quarters


def get_quarterly_cwt(company, year):
    """Get quarterly creditable withholding tax data"""
    import frappe
    quarters = {}
    
    for quarter in range(1, 5):
        start_month = (quarter - 1) * 3 + 1
        end_month = quarter * 3
        
        query = f"""
            SELECT
                COALESCE(SUM(total_taxes_and_charges), 0) as cwt
            FROM `tabPurchase Invoice`
            WHERE docstatus = 1 
                AND company = '{company}'
                AND YEAR(posting_date) = {year}
                AND MONTH(posting_date) BETWEEN {start_month} AND {end_month}
        """
        
        result = frappe.db.sql(query, as_dict=True)[0]
        quarters[f"q{quarter}"] = result['cwt']
    
    return quarters


def get_data(filters):
    """
    Fetch data for Summary Report
    """
    import frappe
    
    company = filters.get("company")
    year = filters.get("year") or datetime.now().year
    
    sales_quarters = get_quarterly_sales(company, year)
    purchase_quarters = get_quarterly_purchases(company, year)
    cwt_quarters = get_quarterly_cwt(company, year)
    
    data = [
        {
            "category": "Total Sales",
            "first_quarter": sales_quarters['q1'],
            "second_quarter": sales_quarters['q2'],
            "third_quarter": sales_quarters['q3'],
            "fourth_quarter": sales_quarters['q4'],
            "annual_total": sum(sales_quarters.values())
        },
        {
            "category": "Total Purchases",
            "first_quarter": purchase_quarters['q1'],
            "second_quarter": purchase_quarters['q2'],
            "third_quarter": purchase_quarters['q3'],
            "fourth_quarter": purchase_quarters['q4'],
            "annual_total": sum(purchase_quarters.values())
        },
        {
            "category": "Creditable Withholding Tax",
            "first_quarter": cwt_quarters['q1'],
            "second_quarter": cwt_quarters['q2'],
            "third_quarter": cwt_quarters['q3'],
            "fourth_quarter": cwt_quarters['q4'],
            "annual_total": sum(cwt_quarters.values())
        }
    ]
    
    return data
