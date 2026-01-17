"""
Final Withholding Tax Report
Bureau of Internal Revenue - Philippine Standard
"""

from frappe import _

def execute(filters=None):
    """
    Generate Final Withholding Tax Report
    """
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    """Define report columns"""
    return [
        {
            "fieldname": "date",
            "label": _("Date"),
            "fieldtype": "Date",
            "width": 100
        },
        {
            "fieldname": "payee_name",
            "label": _("Payee Name"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "tin",
            "label": _("TIN"),
            "fieldtype": "Data",
            "width": 120
        },
        {
            "fieldname": "income_type",
            "label": _("Income Type"),
            "fieldtype": "Data",
            "width": 120
        },
        {
            "fieldname": "gross_income",
            "label": _("Gross Income"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "fwt_rate",
            "label": _("FWT Rate (%)"),
            "fieldtype": "Float",
            "width": 100
        },
        {
            "fieldname": "fwt_amount",
            "label": _("FWT Amount"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]


def get_data(filters):
    """
    Fetch data for Final Withholding Tax Report
    """
    import frappe
    
    conditions = "WHERE docstatus = 1"
    
    if filters.get("company"):
        conditions += f" AND company = '{filters.get('company')}'"
    
    if filters.get("from_date"):
        conditions += f" AND posting_date >= '{filters.get('from_date')}'"
    
    if filters.get("to_date"):
        conditions += f" AND posting_date <= '{filters.get('to_date')}'"
    
    query = f"""
        SELECT
            posting_date as date,
            supplier as payee_name,
            COALESCE(tax_id, 'N/A') as tin,
            'Purchase' as income_type,
            total as gross_income,
            COALESCE((total_taxes_and_charges / total * 100), 0) as fwt_rate,
            total_taxes_and_charges as fwt_amount
        FROM `tabPurchase Invoice`
        {conditions}
        ORDER BY posting_date
    """
    
    data = frappe.db.sql(query, as_dict=True)
    return data
