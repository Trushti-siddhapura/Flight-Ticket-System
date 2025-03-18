import frappe

def validate_ticket(doc, method):
    if not doc.flight:  
        return


    flight_doc = frappe.get_doc("Airplane Flight", doc.flight)
    if not flight_doc.airplane:
        frappe.throw("The flight is not linked to any airplane.")


    airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)
    capacity = airplane_doc.capacity


    ticket_count = frappe.db.count("Airplane Ticket", {
        "flight": doc.flight,
        "docstatus": ["!=", 2]  
    })


    if ticket_count >= capacity:
        frappe.throw("This airplane has no available seats.")