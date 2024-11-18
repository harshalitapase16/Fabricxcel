# Copyright (c) 2024, HT and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Customer(Document):
	def before_save(self):
		print(self.contact_person)
