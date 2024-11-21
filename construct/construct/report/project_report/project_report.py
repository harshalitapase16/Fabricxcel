from frappe import _
import frappe

def execute(filters: dict | None = None):
    """Return columns and data for the report.

    This is the main entry point for the report. It accepts the filters as a
    dictionary and should return columns and data. It is called by the framework
    every time the report is refreshed or a filter is updated.
    """
    columns = get_columns()
    data = get_data()

    return columns, data


def get_columns() -> list[dict]:
    """Return columns for the report.

    One field definition per column, just like a DocType field definition.
    """
    return [
        {
            "label": _("Project Name"),
            "fieldname": "project_name",
            "fieldtype": "Data",
        },
        {
            "label": _("Project Number"),
            "fieldname": "project_number",
            "fieldtype": "Data",
        },
        {
            "label": _("PO No"),
            "fieldname": "po_no",
            "fieldtype": "Int",
        },
        {
            "label": _("PO Date"),
            "fieldname": "po_date",
            "fieldtype": "Date",
        },
        {
            "label": _("PO Qty"),
            "fieldname": "po_qty",
            "fieldtype": "Float",
        },
        {
            "label": _("PO Rate"),
            "fieldname": "po_rate",
            "fieldtype": "Float",
        },
        {
            "label": _("Total Quantity"),
            "fieldname": "total_quantity",
            "fieldtype": "Float",
        },
        {
            "label": _("Project Start Date"),
            "fieldname": "project_start_date",
            "fieldtype": "Date",
        },
        {
            "label": _("Description"),
            "fieldname": "description",
            "fieldtype": "Small Text",
        },
        {
            "label": _("Total Amount"),
            "fieldname": "total_amount",
            "fieldtype": "Float",
        },
        # {
        #     "label": _("Customer"),
        #     "fieldname": "customer",
        #     "fieldtype": "Link",
        # },
    ]


def get_data() -> list[list]:
    """Fetch and return data dynamically from the Project doctype."""
    # Fetch data from the `Project` doctype
    projects = frappe.get_all(
        "Project",
        fields=["project_name", "project_number", "po_no", "po_date", "po_qty", "po_rate","total_quantity","project_start_date","description","total_amount"],
    )
    # Convert the fetched records into a list of rows
    return [
        [
            project.get("project_name"),
            project.get("project_number"),
            project.get("po_no"),
            project.get("po_date"),
            project.get("po_qty"),
            project.get("po_rate"),
            project.get("total_quantity"),
            project.get("project_start_date"),
            project.get("description"),
            project.get("total_amount"),
            # project.get("customer"),
        ]
        for project in projects
    ]
