"""
Purchase Register (PAR) Report
Bureau of Internal Revenue - Philippine Standard
"""

from frappe import _

def execute(filters=None):
    """
    Generate Purchase Register Report for BIR Philippines
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
            "fieldname": "invoice_no",
            "label": _("Invoice #"),
            "fieldtype": "Link",
            "options": "Purchase Invoice",
            "width": 100
        },
        {
            "fieldname": "supplier",
            "label": _("Supplier"),
            "fieldtype": "Link",
            "options": "Supplier",
            "width": 150
        },
        {
            "fieldname": "tin",
            "label": _("TIN"),
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
            "fieldname": "vat_amount",
            "label": _("Input VAT (12%)"),
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "net_amount",
            "label": _("Net Amount"),
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
    Fetch data for Purchase Register Report
    """
    import frappe
    
    conditions = "WHERE docstatus = 1"
    
    if filters.get("company"):
        conditions += f" AND company = '{filters.get('company')}'"
    
    if filters.get("from_date"):
        conditions += f" AND posting_date >= '{filters.get('from_date')}'"
    
    if filters.get("to_date"):
        conditions += f" AND posting_date <= '{filters.get('to_date')}'"
    
    if filters.get("supplier"):
        conditions += f" AND supplier = '{filters.get('supplier')}'"
    
    query = f"""
        SELECT
            pi.posting_date as date,
            pi.name as invoice_no,
            pi.supplier,
            s.tax_id as tin,
            pi.total as gross_amount,
            (pi.total_taxes_and_charges) as vat_amount,
            pi.net_total as net_amount,
            pi.remarks
        FROM
            `tabPurchase Invoice` pi
        LEFT JOIN
            `tabSupplier` s ON pi.supplier = s.name
        {conditions}
        ORDER BY pi.posting_date, pi.name
    """
    
    data = frappe.db.sql(query, as_dict=True)
    return data
