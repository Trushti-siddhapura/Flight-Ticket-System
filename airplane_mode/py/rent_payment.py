import frappe
from frappe.utils import getdate, add_months

@frappe.whitelist()
def fetch_monthly_rent(shop_name, current_month=None):
    lease = frappe.get_all(
        "Lease Contract",
        filters={"shop_name": shop_name},
        fields=["tenant", "rent_amount", "start_date", "end_date"],
        limit=1
    )
    
    if lease:
        tenant = lease[0]["tenant"]
        monthly_rent = lease[0]["rent_amount"] / 12  # Convert annual rent to monthly
        

        start_date = getdate(lease[0]["start_date"])
        end_date = getdate(lease[0]["end_date"])

        if not current_month:
            current_month = start_date

        monthly_start = add_months(start_date, (current_month.month - start_date.month))
        monthly_end = add_months(monthly_start, 1)

        return {
            "tenant": tenant,
            "monthly_rent": monthly_rent,
            "start_date": monthly_start,
            "end_date": monthly_end
        }
    return {}
