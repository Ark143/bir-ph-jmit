"""
Expanded Withholding Tax Report
Bureau of Internal Revenue - Philippine Standard (BIR Form 2307)
"""

from frappe import _

def execute(filters=None):
    """
    Generate Expanded Withholding Tax Report (BIR Form 2307)
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
            "fieldname": "document",
            "label": _("Document"),
            "fieldtype": "Data",
            "width": 100
        },
        {
            "fieldname": "payee",
            "label": _("Payee"),
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
            "fieldname": "gross_amount",
            "label": _("Gross Amount"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "ewt_rate",
            "label": _("EWT Rate (%)"),
            "fieldtype": "Float",
            "width": 100
        },
        {
            "fieldname": "ewt_amount",
            "label": _("EWT Amount"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "remarks",
            "label": _("Remarks"),
            "fieldtype": "Data",
            "width": 150
        }
    ]


def get_data(filters):
    """
    Fetch data for Expanded Withholding Tax Report
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
            name as document,
            supplier as payee,
            COALESCE(tax_id, 'N/A') as tin,
            'Professional Services' as income_type,
            total as gross_amount,
            COALESCE((total_taxes_and_charges / total * 100), 0) as ewt_rate,
            total_taxes_and_charges as ewt_amount,
            remarks
        FROM `tabPurchase Invoice`
        {conditions}
        ORDER BY posting_date DESC
    """
    
    data = frappe.db.sql(query, as_dict=True)
    return data
