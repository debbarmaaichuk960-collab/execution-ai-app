import json
from accessibility_agent import AndroidAccessibilityBridge

class OnAIEngine:
    def __init__(self):
        self.bridge = AndroidAccessibilityBridge()

    def parse_and_execute(self, user_command: str):
        cmd = user_command.lower()
        print(f"--- User Command Received: '{user_command}' ---")
        
        # Accessibility status check
        conn_status = self.bridge.connect_accessibility_service()
        print(f"Status: {conn_status}\n")

        actions = []
        if "uber" in cmd or "cab" in cmd:
            actions = [
                {"type": "OPEN_APP", "package": "com.ubercab"},
                {"type": "INPUT_TEXT", "field": "destination", "value": "Home"},
                {"type": "CLICK", "target": "Confirm UberGo"}
            ]
        elif "zomato" in cmd or "food" in cmd:
            actions = [
                {"type": "OPEN_APP", "package": "com.application.zomato"},
                {"type": "INPUT_TEXT", "field": "search", "value": "Biryani"},
                {"type": "CLICK", "target": "Add to Cart"}
            ]
        elif "whatsapp" in cmd or "message" in cmd:
            actions = [
                {"type": "OPEN_APP", "package": "com.whatsapp"},
                {"type": "INPUT_TEXT", "field": "chat", "value": "On my way!"},
                {"type": "CLICK", "target": "Send"}
            ]

        print("--- Executing System Actions ---")
        for step in actions:
            # Accessibility bridge se steps run karwana
            result = f"Action executed: {step['type']} -> {step.get('package') or step.get('target') or step.get('value')}"
            print(f"[EXECUTION]: {result}")

if __name__ == "__main__":
    ai = OnAIEngine()
    ai.parse_and_execute("Uber se cab book karo")
