import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Employee": [
            {
                "collapsible": 1,
                "fieldname": "statutory",
                "fieldtype": "Section Break",
                "label": "Statutory Details",
                "translatable": 1,
                "insert_after": "personal_details"
            },
            {
                "fieldname": "national_id",
                "fieldtype": "Data",
                "label": "National ID",
                "translatable": 1,
                "insert_after": "statutory"
            },
            {
                "fieldname": "nssf_no",
                "fieldtype": "Data",
                "label": "NSSF No",
                "translatable": 1,
                "insert_after": "national_id"
            },
            {
                "fieldname": "sd_column_break",
                "fieldtype": "Column Break",
                "insert_after": "nssf_no"
            },
            {
                "fieldname": "nhif_no",
                "fieldtype": "Data",
                "label": "NHIF No",
                "translatable": 1,
                "insert_after": "sd_column_break"
            },
            {
                "fieldname": "tax_id",
                "fieldtype": "Data",
                "label": "Tax ID",
                "translatable": 1,
                "insert_after": "nhif_no"
            },
            {
                "fieldname": "sd_section_break",
                "fieldtype": "Section Break",
                "insert_after": "tax_id"
            }
        ]
    }

    create_custom_fields(custom_fields)