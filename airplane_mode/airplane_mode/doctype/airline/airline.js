frappe.ui.form.on("Airline", {
    refresh: function (frm) {
        frm.dashboard.clear_headline(); 
        if (frm.doc.website) { // Clear existing web links
            frm.add_web_link(frm.doc.website, __("Visit Basic link"));
        }
    }
});
