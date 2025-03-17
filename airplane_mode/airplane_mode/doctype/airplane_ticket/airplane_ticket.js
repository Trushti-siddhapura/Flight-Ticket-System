frappe.ui.form.on("Airplane Ticket", {
    refresh: function (frm) {
        if (!frm.is_new() && frm.doc.docstatus === 0) { // Ensure button appears only for existing records
            frm.add_custom_button(__('Assign Seat'), function () {
                let d = new frappe.ui.Dialog({
                    title: "Enter Details",
                    fields: [
                        {
                            label: "Seat Number",
                            fieldname: "seat",
                            fieldtype: "Data", // Fixed typo
                            reqd: 1
                        }
                    ],
                    primary_action_label: "Assign Seat",
                    primary_action(values) {
                        frappe.msgprint(__("Seat Assigned: " + values.seat)); // Fixed typo
                        frm.set_value("seat", values.seat); // Set field value
                        d.hide();
                    }
                });
                d.show();   
            }, __("Actions"));
        }
    }
});
