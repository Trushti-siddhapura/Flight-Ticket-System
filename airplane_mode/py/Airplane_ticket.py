import frappe
import random

def before_save(doc, method):
    unique_add_ons = []
    seen_add_on = set()

    for add_on in doc.add_ons:
        if add_on.item not in seen_add_on:
            seen_add_on.add(add_on.item)
            unique_add_ons.append(add_on)  # Append single add_on, not the whole doc.add_ons

    # Calculate total amount correctly
    total_amount = sum(add.amount for add in unique_add_ons)

    # Ensure flight_price is a valid number
    try:
        flight_price = float(doc.flight_price) if doc.flight_price else 0
    except ValueError:
        flight_price = 0  # Default to 0 if conversion fails

    # Update total amount in the document
    doc.total_amount = flight_price + total_amount

    if doc.status not in ["Boarded", "Confirmed"]:  # Adjust as needed
        frappe.throw("You can't submit. Only Boarded or Confirmed status is allowed.")


def before_insert(doc, method):
    doc.seat = f"{random.randint(1, 99)}{random.choice('ABCDE')}"
