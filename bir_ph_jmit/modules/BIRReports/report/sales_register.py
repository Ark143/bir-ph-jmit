"""
Sales Register (SAR) Report
Bureau of Internal Revenue - Philippine Standard
"""

from frappe import _

def execute(filters=None):
    """
    Generate Sales Register Report for BIR Philippines
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
            "options": "Sales Invoice",
            "width": 100
        },
        {
            "fieldname": "customer",
            "label": _("Customer"),
            "fieldtype": "Link",
            "options": "Customer",
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
            "label": _("VAT (12%)"),
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
    Fetch data for Sales Register Report
    """
    import frappe
    
    conditions = "WHERE docstatus = 1"
    
    if filters.get("company"):
        conditions += f" AND company = '{filters.get('company')}'"
    
    if filters.get("from_date"):
        conditions += f" AND posting_date >= '{filters.get('from_date')}'"
    
    if filters.get("to_date"):
        conditions += f" AND posting_date <= '{filters.get('to_date')}'"
    
    if filters.get("customer"):
        conditions += f" AND customer = '{filters.get('customer')}'"
    
    query = f"""
        SELECT
            si.posting_date as date,
            si.name as invoice_no,
            si.customer,
            c.tax_id as tin,
            si.total as gross_amount,
            (si.total_taxes_and_charges) as vat_amount,
            si.net_total as net_amount,
            si.remarks
        FROM
            `tabSales Invoice` si
        LEFT JOIN
            `tabCustomer` c ON si.customer = c.name
        {conditions}
        ORDER BY si.posting_date, si.name
    """
    
    data = frappe.db.sql(query, as_dict=True)
    return data
