frappe.web_form.after_load(function() {
    setTimeout(() => {
        frappe.call({
            method: 'frappe.client.get_value',
            args: {
                doctype: 'Airplane Ticket',
                filters: { flight: flight },
                fieldname: 'total_amount'
            },
			async:false,
            callback: function(response) {
                if (response.message && response.message.total_amount) {
                    let price = response.message.total_amount;
                    let fieldDiv = document.querySelector('[data-fieldname="flight_price"] .control-value');
                    if (fieldDiv) {
                        fieldDiv.innerHTML = `INR ${price.toFixed(2)}`; // Format as currency
                    }
                    frappe.web_form.refresh_field('flight_price'); // ✅ Refresh field

                    console.log("Flight Price Updated:", price);
                }
            }
        });
    }, 500); // Delay of 500ms
});	