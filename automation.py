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
            "whatsapp": {"category": "communication", "type": "app", "url": "https://web.whatsapp.com", "secure": True},
            "telegram": {"category": "communication", "type": "app", "url": "https://telegram.org", "secure": True},
            "signal": {"category": "communication", "type": "app", "url": "https://signal.org", "secure": True},
            "discord": {"category": "communication", "type": "app", "url": "https://discord.com", "secure": True},
            "slack": {"category": "communication", "type": "app", "url": "https://slack.com", "secure": True},
            "messenger": {"category": "communication", "type": "app", "url": "https://messenger.com", "secure": True},
            "skype": {"category": "communication", "type": "app", "url": "https://skype.com", "secure": True},
            "zoom": {"category": "communication", "type": "app", "url": "https://zoom.us", "secure": True},
            "facebook": {"category": "social", "type": "website", "url": "https://facebook.com", "secure": True},
            "instagram": {"category": "social", "type": "website", "url": "https://www.instagram.com/", "secure": True},
            "twitter": {"category": "social", "type": "website", "url": "https://twitter.com", "secure": True},
            "linkedin": {"category": "social", "type": "website", "url": "https://www.linkedin.com/", "secure": True},
            "reddit": {"category": "social", "type": "website", "url": "https://www.reddit.com/", "secure": True},
            "tiktok": {"category": "social", "type": "website", "url": "https://www.tiktok.com/", "secure": True},
            "pinterest": {"category": "social", "type": "website", "url": "https://pinterest.com", "secure": True},
            "snapchat": {"category": "social", "type": "website", "url": "https://snapchat.com", "secure": True},
            "github": {"category": "dev", "type": "website", "url": "https://github.com/", "secure": True},
            "gitlab": {"category": "dev", "type": "website", "url": "https://gitlab.com", "secure": True},
            "stackoverflow": {"category": "dev", "type": "website", "url": "https://stackoverflow.com/", "secure": True},
            "chatgpt": {"category": "ai", "type": "website", "url": "https://openai.com", "secure": True},
            "gemini": {"category": "ai", "type": "website", "url": "https://google.com", "secure": True},
            "claude": {"category": "ai", "type": "website", "url": "https://claude.ai", "secure": True},
            "google": {"category": "utility", "type": "website", "url": "https://google.com", "secure": True},
            "youtube": {"category": "media", "type": "website", "url": "https://www.youtube.com/", "secure": True},
            "netflix": {"category": "media", "type": "website", "url": "https://netflix.com", "secure": True},
            "spotify": {"category": "media", "type": "website", "url": "https://spotify.com", "secure": True},
            "gmail": {"category": "productivity", "type": "website", "url": "https://google.com", "secure": True},
            "drive": {"category": "productivity", "type": "website", "url": "https://google.com", "secure": True},
            "notion": {"category": "productivity", "type": "website", "url": "https://notion.so", "secure": True}
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

    # 1. FIXED INTERFACE METHOD FOR STREAMLIT (MAPS TO APP/SITE LOGIC)
    def open_app_or_site(self, target):
        normalized_name = target.lower().strip()
        if normalized_name in self.global_platform_registry:
            self.open_site(normalized_name)
            return f"Successfully opened site: {target.title()}"
        else:
            # Fallback to general web search if target is not registered
            search_url = f"https://google.com{target}"
            webbrowser.open(search_url)
            self.log_event("INFO", f"Searching Google for: {target}")
            return f"Platform '{target}' not found in registry. Searching Google instead."

    # 2. ADDED METHOD REQUIRED BY YOUR STREAMLIT APP BUTTONS
    def whatsapp_action(self, contact, action_type="call"):
        self.log_event("INFO", f"Initiating WhatsApp {action_type} to: {contact}")
        
        # Opens WhatsApp Web interface with search or action parameters
        # Note: True automated deep linking requires phone numbers, this opens web interface as a base.
        base_url = "https://whatsapp.com"
        webbrowser.open(base_url)
        
        return f"WhatsApp Engine triggered for contact: '{contact.title()}' with action: '{action_type}'"

    def open_site(self, name):
        self.log_event("INFO", f"Opening site: {name}")
        normalized_name = name.lower().strip()
        if normalized_name in self.global_platform_registry:
            webbrowser.open(self.global_platform_registry[normalized_name]["url"])
        else:
            self.log_event("ERROR", f"Platform '{name}' registry mein nahi mili.")

    def adjust_volume(self, direction):
        self.log_event("INFO", f"Adjusting volume {direction}")
        if direction == "up":
            pyautogui.press("volumeup")
        elif direction == "down":
            pyautogui.press("volumedown")

    def take_screenshot(self):
        self.log_event("INFO", "Taking screenshot...")
        try:
            filename = f"screenshot_{int(time.time())}.png"
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            self.log_event("SUCCESS", f"Screenshot saved: {filename}")
        except Exception as e:
            self.log_event("ERROR", f"Screenshot failed: {e}")

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
        elif any(k in normalized_text for k in ["volume", "awaz", "sound"]):
            if any(k in normalized_text for k in ["up", "tez", "increase", "unche"]):
                action_type = "volume_up"
            elif any(k in normalized_text for k in ["down", "kam", "decrease", "halke"]):
                action_type = "volume_down"
        elif "screen" in normalized_text or "screenshot" in normalized_text:
            action_type = "take_screenshot"
        elif "security log" in normalized_text:
            action_type = "analyze_log"
            
        raw_tokens = normalized_text.split()
        core_filtered_tokens = [
            token for token in raw_tokens 
            if token not in self.noise_vocabulary and token not in ["call", "whatsapp", "phone", "volume", "screen", "security", "log", "screenshot"]
        ]
        extracted_target_entity = " ".join(core_filtered_tokens).title()
        is_whatsapp_channel = "whatsapp" in normalized_text
        
        return {
            "action": action_type,
            "target": extracted_target_entity,
            "state": detected_state,
            "is_whatsapp": is_whatsapp_channel
        }

    def execute_call_subsystem(self, target, is_whatsapp, state):
        channel = "WhatsApp" if is_whatsapp else "Phone"
        self.log_event("INFO", f"Calling {target} via {channel} (State: {state})")
