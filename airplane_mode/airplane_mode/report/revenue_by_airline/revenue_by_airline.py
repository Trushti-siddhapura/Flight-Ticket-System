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
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "label": "Airline",
            "width": 200
        },
        {
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "label": "Revenue",
            "width": 180
        }
    ]

def getdata():
    airlines = frappe.get_all("Airline", fields=["name"])
    data = []

    for airline in airlines:
        revenue = frappe.db.sql("""
    SELECT SUM(at.flight_price)
    FROM `tabAirplane Ticket` at
    JOIN `tabAirplane Flight` af ON at.flight = af.name
    JOIN `tabAirplane` a ON af.airplane = a.name      
    WHERE a.airline = %s
""", (airline.name,))[0][0] or 0

        # Correctly append dictionary
        data.append({"airline": airline.name, "revenue": revenue})

    return sorted(data, key=lambda x: x["revenue"], reverse=True)

def chart_data(data):
    labels = [d["airline"] for d in data]  # Use correct key
    values = [d["revenue"] for d in data]  # Use correct key
      
    return {
        "data": {
            "labels": labels,  # Fix key (should be "labels")
            "datasets": [{"values": values}]
        },
        "type": "donut"
    }

def summary_data(data): 

    total_revenue = sum(d["revenue"] for d in data)  
    return [{
        "label": "Total Revenue:",
        "value": total_revenue,  
        "indicator": "Green   "
    }]

