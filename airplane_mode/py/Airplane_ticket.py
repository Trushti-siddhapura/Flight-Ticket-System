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

    # Update total amount in the document
    doc.total_amount = doc.flight_price + total_amount


    if doc.status != "Boarded":
        frappe.throw("You can't submit")


def before_insert(doc):
   doc.seat = f"{random.randint(1, 99)}{random.choice('ABCDE')}"


