import frappe

from  airplane_module.py import update_gate_number

@frappe.whitelist()
def trigger_gate_number(doc,method):
    frappe.enqueue(update_gate_number.flight=doc.name,new_gate_number=doc.gate_number)