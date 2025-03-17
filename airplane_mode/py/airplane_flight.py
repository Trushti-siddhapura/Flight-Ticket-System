import frappe

def on_submit(doc, method):
    frappe.db.set_value("Airplane Flight", doc.name, "status", "Completed")
    frappe.db.commit()  # Ensure changes are committed to the database
    doc.reload()  # Reload document to reflect changes in the UI
