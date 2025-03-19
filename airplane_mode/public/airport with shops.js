frappe.ui.form.on("Airport with Shops", {
    airport: function(frm) {
        if (frm.doc.airport) {
            frappe.call({
                method: "airplane_mode.py.update_airport_shops",
                args: {
                    airport_name: frm.doc.airport
                },
                callback: function(r) {
                    if (r.message) {
                        frm.clear_table("shops");
                        r.message.forEach((shop) => {
                            let row = frm.add_child("shops");
                            row.shop_name = shop.shop_name;
                            row.tenant_name = shop.tenant_name;
                            row.rent_amount = shop.rent_amount;
                            row.start_date = shop.start_date;
                            row.end_date = shop.end_date;
                        });
                        frm.refresh_field("shops");
                    }
                }
            });
        }
    }
});
