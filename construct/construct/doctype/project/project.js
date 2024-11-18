// Copyright (c) 2024, HT and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Project", {
//     refresh: function(frm) {
//         frm.set_query('name1', function() {
//             return {
//                 filters: {
//                     contract_type : 'Fabrications'
//                 }
//             };
//         });
//     }
// });
frappe.ui.form.on('Project', {
    customer_name: function(frm) {
        if (frm.doc.customer_name) {
            // Customer document fetch karo
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Customer",
                    name: frm.doc.customer_name
                },
                callback: function(r) {
                    if (r.message) {
                        const customer_data = r.message;
                        const contact_persons = customer_data.contact_person || [];

                        // // Pehle se koi contact person ho to clear karo
                        // frm.clear_table("contact_persons");

                        // Contact persons add karo Project ke child table me
                        contact_persons.forEach(function(row) {
                            const child = frm.add_child("contact_persons");
                            child.name1 = row.name1;
                            child.email = row.email;
                        });

                        // Refresh child table
                        // frm.refresh_field("contact_persons");
                    }
                }
            });
        }
    }
});
