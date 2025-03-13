import frappe
import random

def execute ():
    tickets = frappe.get_all("Airplane Ticket",filters = {"seat":["is","not set"]},fields = ["name"])

    for ticket in tickets:
        seat_number = f"{random.randint(1,99)}{random.choice('ABCDE')}"
        frappe.db.set_value("Airplane Ticket",ticket.name,"seat",seat_number)

    frappe.db.commit()