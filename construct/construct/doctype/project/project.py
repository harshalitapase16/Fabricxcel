import frappe
from frappe.model.document import Document

class Project(Document):
    def validate(self):
        print(self.project_name)
        self.total_quantity = self.po_rate/1000
        for drw in self.drawings:
            if drw.numbersquant and drw.drawing_weight:
                drw.total = drw.numbersquant * drw.drawing_weight

            if drw.rate and drw.total:
                drw.amount = drw.rate * drw.total

     
