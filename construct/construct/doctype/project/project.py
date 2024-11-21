import frappe
from frappe.model.document import Document

class Project(Document):
    def validate(self):
        self.total_quantity = self.po_qty/1000
        self.total_amount = self.po_qty * self.po_rate
        for drw in self.drawings:
            if drw.numbersquant and drw.drawing_weight:
                drw.total = drw.numbersquant * drw.drawing_weight

            if drw.rate and drw.total:
                drw.amount = drw.rate * drw.total



