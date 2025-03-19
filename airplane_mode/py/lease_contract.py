import frappe   
from frappe.utils import today


def check_lease_expiry(doc,method):
    if doc.lease_end_date < today():
        doc.status = "Expired"
        frappe.db.set_value("Airport Shop",doc.shop_name,"status","Vacant")
