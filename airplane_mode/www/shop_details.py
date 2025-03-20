import frappe

def get_context(context):
    frappe.msgprint(f"Received Parameters: {frappe.form_dict}")  # Debug URL params
    
    shop_name = frappe.form_dict.get("shop")  # Get shop name from URL
    if not shop_name:
        frappe.throw("Shop parameter is missing in URL")

    shop = frappe.get_all("Airport Shop", filters={"shop_name": shop_name}, fields=["*"])

    if not shop:
        frappe.throw(f"Shop '{shop_name}' does not exist in the database")

    context.shop = shop[0]  # Pass shop details to Jinja template
    return context
