import frappe

def before_save(doc, method):
    doc.full_name = doc.first_name+doc.last_name 



