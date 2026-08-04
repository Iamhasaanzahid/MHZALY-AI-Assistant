import datetime
import json
import os
import re
import subprocess
import sys
import time
import webbrowser
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
        self.log_event("INFO", f"Analyzing security log: {log_entry}")
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
        else:
            self.log_event("ERROR", f"Platform '{name}' not found in registry.")

    def adjust_volume(self, direction):
        self.log_event("INFO", f"Adjusting volume {direction}")
        if direction == "up":
            pyautogui.press("volumeup")
        elif direction == "down":
            pyautogui.press("volumedown")

    def take_screenshot(self):
        self.log_event("INFO", "Taking screenshot")
        try:
            filename = f"screenshot_{int(time.time())}.png"
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            self.log_event("SUCCESS", f"Screenshot saved successfully as {filename}")
        except Exception as e:
            self.log_event("ERROR", f"Failed to take screenshot: {e}")

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
        elif "volume" in normalized_text or any(k in normalized_text for k in ["awaz", "volume", "sound"]):
            if any(k in normalized_text for k in ["up", "tez", "increase", "unche"]):
                action_type = "volume_up"
            elif any(k in normalized_text for k in ["down", "kam", "decrease", "halke"]):
                action_type = "volume_down"
        elif "screen" in normalized_text or "screenshot" in normalized_text:
            action_type = "take_screenshot"
        elif "security log" in normalized_text or "analyze" in normalized_text:
            action_type = "analyze_log"
            
        raw_tokens = normalized_text.split()
        core_filtered_tokens = [
            token for token in raw_tokens 
            if token not in self.noise_vocabulary and token not in ["call", "whatsapp", "phone", "volume", "screen", "security", "log", "screenshot"]
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

    # Subsystem Implementation Stubs to keep code functional
    def execute_call_subsystem(self, target, is_whatsapp, state):
        channel = "WhatsApp" if is_whatsapp else "Standard Phone"
        self.log_event("INFO", f"Initiating {channel} call to target: {target} (State: {state})")

    def execute_navigation_subsystem(self, target):
        self.open_site(target)

    def execute_diagnostic_subsystem(self):
        self.log_event("INFO", f"Engine Version: {self.version} | Active Session: {self.active_session_start}")

    def master_command_router(self, command_string):
        """
        Routes the natural language command string to the correct engine subsystem.
        """
        parsed_data = self.advanced_natural_language_parser(command_string)
        action = parsed_data["action"]
        
        try:
            if action == "communication_call":
                self.execute_call_subsystem(parsed_data["target"], parsed_data["is_whatsapp"], parsed_data["state"])
            elif action == "navigation_launch":
                # Fallback to checking the raw text if the target parsing cleared out registry items
                target_site = parsed_data["target"] if parsed_data["target"] else command_string
                self.execute_navigation_subsystem(target_site)
            elif action == "system_status":
              167             self.execute_diagnostic_subsystem()
        elif action == "volume_up":
            self.adjust_volume("up")
        elif action == "volume_down":
             self.adjust_volume("down")
        elif action == "take_screenshot":
            self.take_screenshot()
        elif action == "analyze_log":
            self.analyze_security_log(command_string)
        else:
        self.log_event("WARNING", f"Command router received an unhandled action: {action}")

