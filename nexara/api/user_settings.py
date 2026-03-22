import frappe

@frappe.whitelist()
def get_user_info():
    user = frappe.get_value("User", frappe.session.user, ["name", "first_name", "full_name", "user_image"], as_dict=1)
    return {
        "first_name": user.first_name,
        "full_name": user.full_name,
        "user_image": user.user_image
    }
    
@frappe.whitelist()
def save_user_settings(field, value):
    doc = get_or_create_user_settings()
    doc.set(field, value)
    doc.save()
    
@frappe.whitelist()
def get_or_create_user_settings():
    user = frappe.session.user

    if not frappe.db.exists("Nexara User Settings", {"user": user}):
        doc = frappe.get_doc({
            "doctype": "Nexara User Settings",
            "user": user,
        })
        doc.insert()
        frappe.db.commit()
        
        return doc

    return frappe.get_doc("Nexara User Settings", {"user": user})