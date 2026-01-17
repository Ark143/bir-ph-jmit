"""
Income Tax Withholding Report
Bureau of Internal Revenue - Philippine Standard
"""

from frappe import _

def execute(filters=None):
    """
    Generate Income Tax Withholding Report
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
            "fieldname": "payee_tin",
            "label": _("Payee TIN"),
            "fieldtype": "Data",
            "width": 120
        },
        {
            "fieldname": "payee_name",
            "label": _("Payee Name"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "nature_of_payment",
            "label": _("Nature of Payment"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "gross_amount",
            "label": _("Gross Amount"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "tax_rate",
            "label": _("Tax Rate (%)"),
            "fieldtype": "Float",
            "width": 100
        },
        {
            "fieldname": "tax_withheld",
            "label": _("Tax Withheld"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]


def get_data(filters):
    """
    Fetch data for Income Tax Withholding Report
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
            COALESCE(s.tax_id, 'N/A') as payee_tin,
            pi.supplier as payee_name,
            'Professional Fee' as nature_of_payment,
            pi.total as gross_amount,
            COALESCE((pi.total_taxes_and_charges / pi.total * 100), 0) as tax_rate,
            pi.total_taxes_and_charges as tax_withheld
        FROM `tabPurchase Invoice` pi
        LEFT JOIN `tabSupplier` s ON pi.supplier = s.name
        {conditions}
        ORDER BY pi.posting_date DESC
    """
    
    data = frappe.db.sql(query, as_dict=True)
    return data
