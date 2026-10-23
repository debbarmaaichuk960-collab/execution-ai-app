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
        
        # 1. Multi-App Chaining Workflow: Uber + WhatsApp
        if "uber" in cmd and "whatsapp" in cmd:
            actions = [
                {"type": "OPEN_APP", "package": "com.ubercab"},
                {"type": "INPUT_TEXT", "field": "destination", "value": "Office"},
                {"type": "CLICK", "target": "Confirm UberGo"},
                {"type": "OPEN_APP", "package": "com.whatsapp"},
                {"type": "INPUT_TEXT", "field": "chat", "value": "Cab book ho gayi hai, main nikal raha hoon!"},
                {"type": "CLICK", "target": "Send"}
            ]
        
        # 2. Single App Workflow: Uber
        elif "uber" in cmd or "cab" in cmd:
            actions = [
                {"type": "OPEN_APP", "package": "com.ubercab"},
                {"type": "INPUT_TEXT", "field": "destination", "value": "Home"},
                {"type": "CLICK", "target": "Confirm UberGo"}
            ]
            
        # 3. Single App Workflow: Zomato
        elif "zomato" in cmd or "food" in cmd:
            actions = [
                {"type": "OPEN_APP", "package": "com.application.zomato"},
                {"type": "INPUT_TEXT", "field": "search", "value": "Biryani"},
                {"type": "CLICK", "target": "Add to Cart"}
            ]

        print("--- Executing Cross-App Workflow ---")
        for step in actions:
            # Accessibility bridge se real-time execution
            result = self.bridge.execute_action_step(step)
            print(f"[EXECUTION]: {result}")

if __name__ == "__main__":
    ai = OnAIEngine()
    # Test a complex multi-app command
    ai.parse_and_execute("Uber book karo aur WhatsApp par message bhej do")
