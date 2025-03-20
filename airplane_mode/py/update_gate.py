import frappe
from frappe.utils.background_jobs import enqueue

def update_gate_number_in_tickets(flight, new_gate_number):
    """
    Updates the gate number in all Airplane Tickets linked to a given flight.
    """
    tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight}, fields=["name"])

    for ticket in tickets:
        frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", new_gate_number)
    
    frappe.db.commit()  # Ensure changes are saved

def trigger_update_gate_number(doc, event):
    """
    Enqueue the background job when the gate number in the flight is changed.
    """
    old_gate_number = frappe.db.get_value("Airplane Flight", doc.name, "gate_number")

    if old_gate_number != doc.gate_number:  # Check if gate number changed
        enqueue(update_gate_number_in_tickets, flight=doc.name, new_gate_number=doc.gate_number, queue="long")
