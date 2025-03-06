# import frappe
# from frappe.model.document import Document
# from frappe.custom.doctype.custom_field.custom_field import create_custom_field

# class FlightPassenger(Document):
#     def before_save(self):

#         self.full_name = f"{self.first_name} {self.last_name}".strip()

 
#         if not frappe.db.exists("Custom", {"dt": "Flight Passenger", "fieldname": "full_name"}):
#             create_custom_field("Flight Passenger", {
#                 "fieldname": "full_name",
#                 "label": "Full Name",
#                 "fieldtype": "Data",
#                 "read_only": 1,
#                 "insert_after": "last_name"
#             })

#             frappe.db.commit()
#             frappe.clear_cache(doctype="Flight Passenger")  # Refresh DocType cache
#             set_title_field()


# @frappe.whitelist(allow_guest=True)
# def set_title_field():
# 		doc = frappe.get_doc("DocType", "Flight Passenger")
# 		if doc.title_field != "full_name":  # Only update if not already set
# 			doc.title_field = "full_name"
# 			doc.save()
# 			frappe.db.commit()
# 			frappe.clear_cache(doctype="Flight Passenger")  # Refresh cache

# 	# Run the function

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
    pass
