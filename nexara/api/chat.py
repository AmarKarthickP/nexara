import frappe
from datetime import datetime

@frappe.whitelist(allow_guest=False)
def send_message(conversation_id, message):
    
    # Save user message
    msg = frappe.get_doc({
        "doctype": "Nexara Message",
        "conversation": conversation_id,
        "role": "user",
        "content": message,
        "timestamp": datetime.now()
    })
    msg.insert(ignore_permissions=True)

    # Temporary bot response (no AI yet)
    bot_reply = "Got it. AI is still sleeping 😴"

    bot_msg = frappe.get_doc({
        "doctype": "Nexara Message",
        "conversation": conversation_id,
        "role": "assistant",
        "content": bot_reply,
        "timestamp": datetime.now()
    })
    bot_msg.insert(ignore_permissions=True)

    return {
        "reply": bot_reply
    }