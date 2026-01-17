"""
Creditable Withholding Tax Report
Bureau of Internal Revenue - Philippine Standard
"""

from frappe import _

def execute(filters=None):
    """
    Generate Creditable Withholding Tax Report
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
            "fieldname": "gross_payment",
            "label": _("Gross Payment"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "cwt_rate",
            "label": _("CWT Rate (%)"),
            "fieldtype": "Float",
            "width": 100
        },
        {
            "fieldname": "cwt_amount",
            "label": _("CWT Amount"),
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
    Fetch data for Creditable Withholding Tax Report
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
            pi.posting_date as date,
            pi.name as document,
            pi.supplier as payee,
            s.tax_id as tin,
            pi.total as gross_payment,
            COALESCE((pi.total_taxes_and_charges / pi.total * 100), 0) as cwt_rate,
            pi.total_taxes_and_charges as cwt_amount,
            pi.remarks
        FROM
            `tabPurchase Invoice` pi
        LEFT JOIN
            `tabSupplier` s ON pi.supplier = s.name
        {conditions}
        ORDER BY pi.posting_date
    """
    
    data = frappe.db.sql(query, as_dict=True)
    return data
