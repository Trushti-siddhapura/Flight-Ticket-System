import frappe
import random

def before_save(doc, method):
    unique_add_ons = []
    seen_add_on = set()

    for add_on in doc.add_ons:
        if add_on.item not in seen_add_on:
            seen_add_on.add(add_on.item)
            unique_add_ons.append(add_on)  

    total_amount = sum(add.amount for add in unique_add_ons)

    try:
        # Ensure flight_price is set correctly
        doc.flight_price = float(doc.flight_price) if doc.flight_price else get_default_flight_price(doc.flight)
    except ValueError:
        doc.flight_price = get_default_flight_price(doc.flight)

    doc.total_amount = doc.flight_price + total_amount

def before_insert(doc, method):
    doc.seat = f"{random.randint(1, 99)}{random.choice('ABCDE')}"
    
    # Ensure flight_price is set before saving
    if not doc.flight_price:
        doc.flight_price = get_default_flight_price(doc.flight)

# Function to fetch default flight price
def get_default_flight_price(flight):
    flight_price = frappe.db.get_value("Flight", flight, "price")
    return float(flight_price) if flight_price else 0
