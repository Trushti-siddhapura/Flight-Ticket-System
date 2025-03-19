import frappe

@frappe.whitelist()
def update_airport_shops(airport_name):
    # Fetch all shops linked to the selected airport
    airport_shops = frappe.get_all("Airport Shop",
        filters={"airport": airport_name},  
        fields=["name", "shop_name"]
    )

    shop_data = []
    
    for shop in airport_shops:
        # Fetch lease details for each shop
        lease = frappe.get_all("Lease Contract",
            filters={"shop_name": shop.shop_name},  
            fields=["tenant", "rent_amount", "start_date", "end_date"],
            limit=1
        )

        if lease:
            shop_data.append({
                "shop_name": shop.shop_name,
                "tenant_name": lease[0]["tenant"],
                "rent_amount": lease[0]["rent_amount"],
                "start_date": lease[0]["start_date"],
                "end_date": lease[0]["end_date"]
            })
    
    return shop_data  # Send this data to JavaScript
