"""
VAT Reconciliation Report
Bureau of Internal Revenue - Philippine Standard
"""

from frappe import _

def execute(filters=None):
    """
    Generate VAT Reconciliation Report
    """
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    """Define report columns"""
    return [
        {
            "fieldname": "period",
            "label": _("Period"),
            "fieldtype": "Data",
            "width": 100
        },
        {
            "fieldname": "total_sales",
            "label": _("Total Sales"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "vatable_sales",
            "label": _("Vatable Sales"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "exempt_sales",
            "label": _("Exempt Sales"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "zero_rated_sales",
            "label": _("Zero-Rated Sales"),
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
            "fieldname": "vat_difference",
            "label": _("Difference"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]


def get_data(filters):
    """
    Fetch data for VAT Reconciliation Report
    """
    import frappe
    
    conditions = "WHERE docstatus = 1"
    company = filters.get("company")
    
    if company:
        conditions += f" AND company = '{company}'"
    
    if filters.get("from_date"):
        conditions += f" AND posting_date >= '{filters.get('from_date')}'"
    
    if filters.get("to_date"):
        conditions += f" AND posting_date <= '{filters.get('to_date')}'"
    
    # Sales data
    sales_query = f"""
        SELECT
            'Sales' as category,
            COALESCE(SUM(total), 0) as total_sales,
            COALESCE(SUM(CASE WHEN is_vat = 1 THEN total ELSE 0 END), 0) as vatable_sales,
            COALESCE(SUM(CASE WHEN is_exempt = 1 THEN total ELSE 0 END), 0) as exempt_sales,
            COALESCE(SUM(CASE WHEN is_zero_rated = 1 THEN total ELSE 0 END), 0) as zero_rated_sales,
            COALESCE(SUM(total_taxes_and_charges), 0) as output_vat
        FROM `tabSales Invoice`
        {conditions}
    """
    
    # Purchase data
    purchase_query = f"""
        SELECT
            COALESCE(SUM(total_taxes_and_charges), 0) as input_vat
        FROM `tabPurchase Invoice`
        {conditions}
    """
    
    sales_data = frappe.db.sql(sales_query, as_dict=True)[0]
    purchase_data = frappe.db.sql(purchase_query, as_dict=True)[0]
    
    vat_difference = sales_data['output_vat'] - purchase_data['input_vat']
    
    data = [{
        "period": filters.get("period") or "Current Period",
        "total_sales": sales_data['total_sales'],
        "vatable_sales": sales_data['vatable_sales'],
        "exempt_sales": sales_data['exempt_sales'],
        "zero_rated_sales": sales_data['zero_rated_sales'],
        "output_vat": sales_data['output_vat'],
        "input_vat": purchase_data['input_vat'],
        "vat_difference": vat_difference
    }]
    
    return data
