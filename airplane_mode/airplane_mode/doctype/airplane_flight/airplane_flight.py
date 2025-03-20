import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):	
	pass

def get_context(context):
	doc = frappe.get_all("Airplane Flight")
	context.duration = frappe.utils.format_duartion(doc.duration)