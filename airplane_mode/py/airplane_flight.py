import frappe


def on_submit(doc,method):
    frappe.db.set_value("Airplane Flight",doc.name,"status","Completed")