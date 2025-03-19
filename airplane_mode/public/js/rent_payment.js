frappe.ui.form.on("Rent Payment", {
    shop_name: function(frm) {
        if (frm.doc.shop_name) {
            frappe.call({
                method: "airplane_mode.py.rent_payment.fetch_monthly_rent",
                args: {
                    shop_name: frm.doc.shop_name
                },
                callback: function(response) {
                    if (response.message) {
                        frm.set_value("tenant", response.message.tenant);
                        frm.set_value("monthly_rent_amount", response.message.monthly_rent);
                        frm.set_value("start_date", response.message.start_date);
                        frm.set_value("end_date", response.message.end_date);
                    }
                }
            });
        }
    }
});
