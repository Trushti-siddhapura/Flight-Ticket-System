# Copyright (c) 2025, Trushti-Siddhapura and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = getcolumn()
    data = getdata()
    chart_data_result = chart_data(data)
    summary = summary_data(data)
    
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
    airports = frappe.get_all("Airport Shop", fields=["name", "status", "airport"])
    data = []

    for airport in airports:
        status = airport.status or "Unknown"
        data.append({
            "airport": airport.airport or "Unknown",
            "status": status
        })

    return data 

def chart_data(data):
    available_shops = sum(1 for d in data if d["status"] == "Vacant")
    occupied_shops = sum(1 for d in data if d["status"] == "Active")

    return {
        "data": {
            "labels": ["Active", "Vacant"],
            "datasets": [{
                "values": [occupied_shops, available_shops]
            }]
        },
        "type": "donut"
    }

def summary_data(data):
    total_shops = len(data)
    available_shops = sum(1 for d in data if d["status"] == "Vacant")
    occupied_shops = total_shops - available_shops

    return [
        {
            "label": "Total Shops",
            "value": total_shops,
            "indicator": "Blue"
        },
        {
            "label": "Available Shops",
            "value": available_shops,
            "indicator": "Green"
        },
        {
            "label": "Occupied Shops",
            "value": occupied_shops,
            "indicator": "Red"
        }
    ]
