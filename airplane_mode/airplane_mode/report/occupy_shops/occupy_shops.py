# Copyright (c) 2025, Trushti-Siddhapura and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = getcolumn()
    data = getdata()
    chart_data_result = chart_data(data)
    summary = summary_data(data)
    
    # Ensure correct order of return values
    return columns, data, None, chart_data_result, summary

def getcolumn():
    return [
        {
            "fieldname": "airport",
            "fieldtype": "Link",
            "options": "Airport",
            "label": "Airport",
            "width": 200
        },
        {
            "fieldname": "status",
            "fieldtype": "Select",
            "label": "Status",
            "width": 180
        }
    ]

def getdata():
   airports = 	frappe.get_all("Airport Shop",fields = ["name","status","airport"])
   data = []

   for airport in airports:
       status = airport.status
       data.append({
           "airport":airport.airport,
           "status":status
	   })
       return data
   
def chart_data(data):
     available_shops = sum(1 for d in data if d["status"] == "Vacant")
     occupied_shops = sum(1 for d in data if d["status"] == "Active")
     return{
         
	 }