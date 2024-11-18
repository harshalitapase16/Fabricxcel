from frappe import _

def get_data():
    return [
        {
            "module_name": "Construct",  # Replace with your app’s name
            "category": "Modules",
            "label": _("Construct"),  # Display name in the sidebar
            "color": "#1abc9c",         # Choose a color for the icon
            "icon": "octicon octicon-device-desktop",  # Choose an icon
            "type": "module",
            "onboard_present": 1
        }
    ]
