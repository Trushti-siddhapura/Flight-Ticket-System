import frappe

def update_gate_number(flight, new_gate_number):
    tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight}, fields=["name"])
    
    for ticket in tickets:
        frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number",new_gate_number)

    frappe.db.commit()