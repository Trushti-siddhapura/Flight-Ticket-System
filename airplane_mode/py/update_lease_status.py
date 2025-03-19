import frappe
from frappe.utils import today


def update_lease_status():
    shops = frappe.get_all("Airport Shop",filters = {"lease_end":["<",today()],"status":"Active"},field = ["name"])



    for shop in shops:
        doc = frappe.get_doc("Airport Shop",shop.name)
        doc.status = "Expired"
        doc.save()
        frappe.db.commit()


        