import frappe
from frappe.utils import nowdate, add_days, get_first_day, get_last_day
from frappe.core.doctype.communication.email import make

def send_rent_due_reminders():
    """Send rent due reminder emails to tenants on the 1st of every month."""
    
    # Get all tenants with rent due
    tenants = frappe.get_all(
        "Lease Contract",
        filters={"end_date": get_first_day(nowdate())},  # Rent due on 1st of the month
        fields=["name", "email", "rent_amount"]
    )

    for tenant in tenants:
        subject = "Reminder: Rent Due for This Month"
        message = f"""
        Dear {tenant.name},<br><br>
        This is a friendly reminder that your rent of <b>{tenant.rent_amount} USD</b> 
        is due this month.<br><br>
        Please make the payment on time to avoid any late fees.<br><br>
        Best regards,<br>
        Property Management Team
        """

        # Send email
        frappe.sendmail(
            recipients=[tenant.email],
            subject=subject,
            message=message
        )
