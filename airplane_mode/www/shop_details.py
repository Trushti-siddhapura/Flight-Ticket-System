import frappe

def get_context(context):
    print("shop_details.py is running")  # Debugging line

    # Check if shop_name is received from the URL
    shop_name = frappe.form_dict.get("shop")
    print("Received Shop Name:", shop_name)

    if not shop_name:
        context.shop = {"error": "No shop name provided"}
        return context

    # Fetch Shop Details
    shop = frappe.get_value(
        "Airport Shop",
        {"name": shop_name},
        ["shop_name", "shop_number", "airport_city", "tenant", "rent"],
        as_dict=True
    )

    print("Shop Data:", shop)  # Debugging Output

    if not shop:
        context.shop = {"error": "Shop not found"}
    else:
        context.shop = shop  # Ensure it's a dictionary

    return context
