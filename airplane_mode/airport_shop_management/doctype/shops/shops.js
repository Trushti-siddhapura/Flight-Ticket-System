        // Copyright (c) 2025, Trushti-Siddhapura and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shops", {
	onload:function(frm) {
        frm.set_query("shop_type",function(){
            return{
                filters :{
                    "enabled":1
                }
            }
        })

	},
});
                