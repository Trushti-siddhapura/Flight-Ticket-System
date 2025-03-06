# Copyright (c) 2025, Trushti-Siddhapura and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests


class Airline(Document):
	pass



@frappe.whitelist(allow_guest=True)

def get_data():
	doc = frappe.get_all("Airline",fields=["name"])
	frappe.db.commit()
	return doc

