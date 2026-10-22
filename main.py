import json

def process_command(cmd):
    cmd = cmd.lower()
    if "whatsapp" in cmd:
        return {"app": "WhatsApp", "action": "OPEN"}
    elif "zomato" in cmd:
        return {"app": "Zomato", "action": "SEARCH"}
    else:
        return {"app": "System", "action": "CHAT"}

print(process_command("Zomato se biryani search karo"))
