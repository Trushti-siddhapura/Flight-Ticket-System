import frappe

def validate_ticket(doc, method):
    if not doc.flight:  # Ensure the correct field is used
        return

    # Fetch the Airplane Flight document
    flight_doc = frappe.get_doc("Airplane Flight", doc.flight)
    if not flight_doc.airplane:
        frappe.throw("The flight is not linked to any airplane.")

    # Fetch the Airplane document
    airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)
    capacity = airplane_doc.capacity

    # Count existing Airplane Ticket records for this flight
    ticket_count = frappe.db.count("Airplane Ticket", {
        "flight": doc.flight,
        "docstatus": ["!=", 2]  # Exclude cancelled tickets
    })

    # Check if the capacity is exceeded
    if ticket_count >= capacity:
        frappe.throw("This airplane has no available seats.")
s