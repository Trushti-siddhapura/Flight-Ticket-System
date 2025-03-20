import frappe

def create_shop_types():
    shop_types = ["Stall", "Walk-through", "Normal"]

    for shop in shop_types:
        if not frappe.db.exists("Shop Type", shop):
            doc = frappe.get_doc({
                "doctype": "Shop Type",
                "shop_type_name": shop,
                "enabled": 1
            })
            doc.insert(ignore_permissions=True)
            print(f"Inserted {shop} Shop Type")

if __name__ == "__main__":
    create_shop_types()
