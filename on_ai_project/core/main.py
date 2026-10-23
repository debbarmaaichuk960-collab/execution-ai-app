import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.security_vault import LocalSecurityVault
from bridges.accessibility_agent import AndroidAccessibilityBridge
from core.self_evolving import SelfEvolvingWatcher
from bridges.voice_engine import LocalVoiceEngine
from core.local_llm import OnDeviceLocalLLM
from core.apk_builder import AndroidAPKBuilder
from ui.floating_widget import FloatingCyberpunkWidget
from core.model_optimizer import LocalModelOptimizer
from core.offline_rag import OfflineRAGSearch
from bridges.vision_engine import OnDeviceVisionEngine
from core.battery_manager import SmartBatteryManager

class OnAIMasterEngine:
    def __init__(self):
        self.vault = LocalSecurityVault()
        self.bridge = AndroidAccessibilityBridge()
        self.watcher = SelfEvolvingWatcher()
        self.voice = LocalVoiceEngine()
        self.llm = OnDeviceLocalLLM()
        self.apk_builder = AndroidAPKBuilder()
        self.floating_widget = FloatingCyberpunkWidget()
        self.optimizer = LocalModelOptimizer()
        self.rag = OfflineRAGSearch()
        self.vision = OnDeviceVisionEngine()
        self.battery = SmartBatteryManager()

    def process_master_request(self, audio_or_text_input: str, is_voice: bool = True):
        print("\n========================================================")
        print("🚀 ON AI SUPER-APP - GOD-TIER ULTIMATE MASTER ENGINE ACTIVE")
        print("========================================================")

        # 1. Security & Vault Check
        auth_msg = self.vault.authenticate_user(biometric_verified=True)
        print(f"[SECURITY VAULT]: {auth_msg}")

        # 2. Daily Self-Evolving Tech Watcher
        self.watcher.run_daily_background_watcher()

        # 3. Smart Battery & Thermal Throttling Check
        bat_status = self.battery.check_and_throttle()
        print(f"[BATTERY CHECK]: {bat_status}")

        # 4. Model Weight & RAM Optimization
        opt_status = self.optimizer.optimize_weights()
        print(f"[OPTIMIZER STATUS]: {opt_status}")

        # 5. Floating System-Wide Widget Activation
        widget_status = self.floating_widget.render_floating_bubble()
        print(f"[FLOATING WIDGET]: {widget_status}")

        # 6. Real-time Vision Context Analysis
        vision_ctx = self.vision.analyze_screen_context()
        print(f"[VISION CONTEXT]: {vision_ctx}")

        # 7. Voice Processing
        if is_voice:
            user_command = self.voice.listen_and_transcribe_offline(audio_or_text_input)
        else:
            user_command = audio_or_text_input

        # 8. Offline RAG Document Search
        rag_result = self.rag.search_local_documents(user_command)
        print(f"[RAG RESULT]: {rag_result}")

        # 9. Local LLM Reasoning
        ai_brain_reply = self.llm.generate_local_response(user_command)
        print(f"[AI BRAIN OUTPUT]: {ai_brain_reply}")

        # 10. APK Build Pipeline Status
        apk_status = self.apk_builder.compile_to_apk()
        print(f"[BUILD STATUS]: {apk_status}")

        # 11. Accessibility Bridge Connection & Execution
        bridge_status = self.bridge.connect_accessibility_service()
        print(f"[ACCESSIBILITY BRIDGE]: {bridge_status}")

        cmd = user_command.lower()
        if "song" in cmd or "play" in cmd:
            step = {"type": "MEDIA_PLAY", "media": "Lofi Beats - YouTube"}
        elif "image" in cmd or "generate" in cmd:
            step = {"type": "IMAGE_GENERATION", "prompt": "Cyberpunk City HD"}
        else:
            step = {"type": "OPEN_APP", "package": "com.whatsapp"}

        result = self.bridge.execute_action_step(step)
        print(f"[EXECUTION RESULT]: {result}")
        print("========================================================\n")

if __name__ == "__main__":
    engine = OnAIMasterEngine()
    engine.process_master_request("YouTube par lofi song play karo", is_voice=True)
    time.sleep(1)
