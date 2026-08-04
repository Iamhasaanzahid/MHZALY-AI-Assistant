Import webbrowser
import os
import subprocess
import json
import re
import datetime
import time
import pyautogui

class EnterpriseAutomationEngine:
    def __init__(self, owner_name="Muhammad Hassaan Zahid"):
        self.owner = owner_name
        self.version = "5.2.0-Enterprise"
        self.active_session_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.execution_audit_trail = []
        self.security_logs = []
        self.global_platform_registry = {
            "whatsapp": {"category": "communication", "type": "app", "url": "https://web.whatsapp.com/", "secure": True},
            "telegram": {"category": "communication", "type": "app", "url": "https://web.telegram.org/", "secure": True},
            "signal": {"category": "communication", "type": "app", "url": "https://signal.org/", "secure": True},
            "discord": {"category": "communication", "type": "app", "url": "https://discord.com/app", "secure": True},
            "slack": {"category": "communication", "type": "app", "url": "https://slack.com/", "secure": True},
            "messenger": {"category": "communication", "type": "app", "url": "https://www.messenger.com/", "secure": True},
            "skype": {"category": "communication", "type": "app", "url": "https://web.skype.com/", "secure": True},
            "zoom": {"category": "communication", "type": "app", "url": "https://zoom.us/", "secure": True},
            "facebook": {"category": "social", "type": "website", "url": "https://www.facebook.com/", "secure": True},
            "instagram": {"category": "social", "type": "website", "url": "https://www.instagram.com/", "secure": True},
            "twitter": {"category": "social", "type": "website", "url": "https://twitter.com/", "secure": True},
            "linkedin": {"category": "social", "type": "website", "url": "https://www.linkedin.com/", "secure": True},
            "reddit": {"category": "social", "type": "website", "url": "https://www.reddit.com/", "secure": True},
            "tiktok": {"category": "social", "type": "website", "url": "https://www.tiktok.com/", "secure": True},
            "pinterest": {"category": "social", "type": "website", "url": "https://www.pinterest.com/", "secure": True},
            "snapchat": {"category": "social", "type": "website", "url": "https://snapchat.com/", "secure": True},
            "github": {"category": "dev", "type": "website", "url": "https://github.com/", "secure": True},
            "gitlab": {"category": "dev", "type": "website", "url": "https://gitlab.com/", "secure": True},
            "stackoverflow": {"category": "dev", "type": "website", "url": "https://stackoverflow.com/", "secure": True},
            "chatgpt": {"category": "ai", "type": "website", "url": "https://chat.openai.com/", "secure": True},
            "gemini": {"category": "ai", "type": "website", "url": "https://gemini.google.com/", "secure": True},
            "claude": {"category": "ai", "type": "website", "url": "https://claude.ai/", "secure": True},
            "google": {"category": "utility", "type": "website", "url": "https://www.google.com/", "secure": True},
            "youtube": {"category": "media", "type": "website", "url": "https://www.youtube.com/", "secure": True},
            "netflix": {"category": "media", "type": "website", "url": "https://www.netflix.com/", "secure": True},
            "spotify": {"category": "media", "type": "website", "url": "https://open.spotify.com/", "secure": True},
            "gmail": {"category": "productivity", "type": "website", "url": "https://mail.google.com/", "secure": True},
            "drive": {"category": "productivity", "type": "website", "url": "https://drive.google.com/", "secure": True},
            "notion": {"category": "productivity", "type": "website", "url": "https://www.notion.so/", "secure": True}
        }
        self.noise_vocabulary = {
            "on", "off", "please", "kindly", "run", "execute", "start", 
            "open", "launch", "access", "visit", "to", "via", "app", 
            "application", "portal", "system", "browser", "website"
        }

    def log_event(self, log_level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_entry = f"[{timestamp}] [{log_level}] {message}"
        print(formatted_entry)
        self.execution_audit_trail.append(formatted_entry)

    def analyze_security_log(self, log_entry):
        self.log_event("INFO", "Analyzing security log...")
        if "failed login" in log_entry.lower():
            self.log_event("WARNING", "Potential brute force attempt detected in logs!")
            self.security_logs.append({"status": "DANGER", "details": log_entry})
        else:
            self.security_logs.append({"status": "SAFE", "details": log_entry})

    def open_site(self, name):
        self.log_event("INFO", f"Opening site: {name}")
        normalized_name = name.lower()
        if normalized_name in self.global_platform_registry:
            webbrowser.open(self.global_platform_registry[normalized_name]["url"])

    def adjust_volume(self, direction):
        self.log_event("INFO", f"Adjusting volume {direction}")
        if direction == "up":
            pyautogui.press("volumeup")
        elif direction == "down":
            pyautogui.press("volumedown")

    def take_screenshot(self):
        self.log_event("INFO", "Taking screenshot")

    def advanced_natural_language_parser(self, raw_command_string):
        if not raw_command_string or not isinstance(raw_command_string, str):
            self.log_event("WARNING", "Empty or invalid command string received.")
            return {"action": "none", "target": "", "state": None, "is_whatsapp": False}
        normalized_text = raw_command_string.strip().lower()
        detected_state = None
        if re.search(r'\boff\b', normalized_text):
            detected_state = "OFF"
        elif re.search(r'\bon\b', normalized_text):
            detected_state = "ON"
        action_type = "general"
        if "call" in normalized_text:
            action_type = "communication_call"
        elif any(keyword in normalized_text for keyword in ["open", "launch", "access", "visit", "chalao"]):
            action_type = "navigation_launch"
        elif "status" in normalized_text or "check" in normalized_text:
            action_type = "system_status"
        elif "volume" in normalized_text:
            if "up" in normalized_text or "tez" in normalized_text:
                action_type = "volume_up"
            elif "down" in normalized_text or "kam" in normalized_text:
                action_type = "volume_down"
        elif "screen" in normalized_text:
            action_type = "take_screenshot"
        elif "security log" in normalized_text:
            action_type = "analyze_log"
            
        raw_tokens = normalized_text.split()
        core_filtered_tokens = [
            token for token in raw_tokens 
            if token not in self.noise_vocabulary and token not in ["call", "whatsapp", "phone", "volume", "screen", "security", "log"]
        ]
        extracted_target_entity = " ".join(core_filtered_tokens).title()
        is_whatsapp_channel = "whatsapp" in normalized_text
        parsed_metadata = {
            "action": action_type,
            "target": extracted_target_entity,
            "state": detected_state,
            "is_whatsapp": is_whatsapp_channel,
            "raw_tokens": raw_tokens,
            "filtered_tokens": core_filtered_tokens
        }
        return parsed_metadata

    def master_command_router(self, command_string):
        parsed_data = self.advanced_natural_language_parser(command_string)
        try:
            if parsed_data["action"] == "communication_call":
                self.execute_call_subsystem(parsed_data["target"], parsed_data["is_whatsapp"], parsed_data["state"])
            elif parsed_data["action"] == "navigation_launch":
                self.execute_navigation_subsystem(parsed_data["target"])
            elif parsed_data["action"] == "system_status":
                self.execute_diagnostic_subsystem()
            elif parsed_data["action"] == "volume_up":
                self.adjust_volume("up")
            elif parsed_data["action"] == "volume_down":
                self.adjust_volume("down")
            elif parsed_data["action"] == "take_screenshot":
                self.take_screenshot()
            elif parsed_data["action"] == "analyze_log":
                self.analyze_security_log(parsed_data["target"])
            else:
                self.execute_fallback_subsystem(command_string)
        except Exception as error:
            self.log_event("ERROR", f"Exception encountered during command routing: {str(error)}")

    def execute_call_subsystem(self, recipient_name, use_whatsapp_flag, state_modifier):
        if use_whatsapp_flag:
            webbrowser.open(self.global_platform_registry["whatsapp"]["url"])
            self.log_event("INFO", f"Opening WhatsApp for recipient: {recipient_name}")
            time.sleep(8)
            try:
                pyautogui.hotkey('ctrl', 'alt', '/')
                time.sleep(1)
                pyautogui.typewrite(recipient_name)
                time.sleep(2)
                pyautogui.press('enter')
            except Exception as e:
                self.log_event("ERROR", f"Automation error during WhatsApp call routing: {str(e)}")

        def execute_navigation_subsystem(self, target_query):
        query_sanitized = target_query.lower()
        matched_platform_key = None
        for registry_key in self.global_platform_registry:
            if registry_key in query_sanitized:
                matched_platform_key = registry_key
                break
        if matched_platform_key:
            webbrowser.open(self.global_platform_registry[matched_platform_key]["url"])
        else:
            if target_query:
                formatted_domain_string = target_query.replace(" ", "").lower()
                target_url = f"https://www.{formatted_domain_string}.com"
                webbrowser.open(target_url)

    def execute_diagnostic_subsystem(self):
        self.log_event("INFO", "Running Enterprise System Diagnostics.")

    def execute_fallback_subsystem(self, unparsed_text):
        self.log_event("INFO", f"Executing generic universal fallback handler for string: '{unparsed_text}'")

if __name__ == "__main__":
    engine = EnterpriseAutomationEngine()
