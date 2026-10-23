import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.security_vault import LocalSecurityVault
from bridges.accessibility_agent import AndroidAccessibilityBridge
from core.self_evolving import SelfEvolvingWatcher

class OnAIAppInterface:
    def __init__(self):
        self.vault = LocalSecurityVault()
        self.bridge = AndroidAccessibilityBridge()
        self.watcher = SelfEvolvingWatcher()

    def render_mobile_hud(self):
        print("\n==================================================")
        print("📱 [ON AI MOBILE APP UI] - CYBERPUNK HUD v1.0")
        print("==================================================")
        print(" [🔒] Security Vault: ACTIVE (AES-256 Encrypted)")
        print(" [🤖] Self-Evolving Watcher: RUNNING (Daily Daemon)")
        print(" [🔌] Accessibility Bridge: CONNECTED")
        print("==================================================")

    def handle_ui_touch_event(self, button_name: str):
        print(f"\n[UI EVENT]: User tapped button -> '{button_name}'")
        if "song" in button_name.lower():
            step = {"type": "MEDIA_PLAY", "media": "Lofi Beats - YouTube"}
        elif "whatsapp" in button_name.lower():
            step = {"type": "OPEN_APP", "package": "com.whatsapp"}
        else:
            step = {"type": "OPEN_APP", "package": "General Super-App Task"}

        result = self.bridge.execute_action_step(step)
        print(f"[UI EXECUTION RESULT]: {result}")

if __name__ == "__main__":
    app_ui = OnAIAppInterface()
    app_ui.render_mobile_hud()
    app_ui.handle_ui_touch_event("Play Song on YouTube")
    app_ui.handle_ui_touch_event("Open WhatsApp")
