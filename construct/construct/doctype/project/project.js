// Copyright (c) 2024, HT and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Project', {
//     customer_name: function(frm) {
//         // Jab bhi customer select kiya jata hai, to child table ko clear kare
//         frm.clear_table("contact_persons");
//         frm.refresh_field("contact_persons");
//     }
// });

// frappe.ui.form.on('Project Contact Persons', {
//     contact_person: function(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];

//         if (frm.doc.customer_name && row.contact_person) {
//             // Fetch contact details based on selected contact person
//             frappe.call({
//                 method: "frappe.client.get",
//                 args: {
//                     doctype: "Customer",
//                     filters: {
//                         parent: frm.doc.customer_name,
//                         contact_name: row.name1
//                     }
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         frappe.model.set_value(cdt, cdn, 'name1', r.message.name1);
//                         frappe.model.set_value(cdt, cdn, 'email', r.message.email);
//                     }
//                 }
//             });
//         }
//     }
// });
