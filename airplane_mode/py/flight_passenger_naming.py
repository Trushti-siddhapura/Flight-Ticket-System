import frappe


def after_insert(doc,method):
    new_name = f"{doc.first_name}"

    frappe.db.set_value(doc.doctype,doc.name,"name",new_name)

    doc.reload()




  