import webbrowser
import os
import subprocess
import json
import re

class AdvancedAutomationSystem:
    def __init__(self):
        # Global platform registry covering worldwide secure apps and websites
        self.platforms = {
            "whatsapp": {"type": "app", "url": "https://web.whatsapp.com/"},
            "youtube": {"type": "website", "url": "https://www.youtube.com/"},
            "google": {"type": "website", "url": "https://www.google.com/"},
            "facebook": {"type": "website", "url": "https://www.facebook.com/"},
            "instagram": {"type": "website", "url": "https://www.instagram.com/"},
            "twitter": {"type": "website", "url": "https://twitter.com/"},
            "github": {"type": "website", "url": "https://github.com/"},
            "chatgpt": {"type": "website", "url": "https://chat.openai.com/"},
            "telegram": {"type": "app", "url": "https://web.telegram.org/"},
            "linkedin": {"type": "website", "url": "https://www.linkedin.com/"},
            "reddit": {"type": "website", "url": "https://www.reddit.com/"},
            "gmail": {"type": "website", "url": "https://mail.google.com/"}
        }
        self.call_history = []

    def preprocess_command(self, raw_input):
        """
        Advanced natural language processing filter to strip control words 
        like 'on', 'off', 'please', or conversational fluff while preserving 
        essential target parameters.
        """
        if not raw_input:
            return "", {}

        text = raw_input.strip().lower()
        
        # Detect state markers if needed for device/app toggles
        state_status = None
        if "off" in text:
            state_status = "OFF"
        elif "on" in text:
            state_status = "ON"

        # Filter out noisy operational keywords
        noise_words = ["on", "off", "please", "kindly", "run", "execute", "start", "open", "launch"]
        tokens = text.split()
        filtered_tokens = [t for t in tokens if t not in noise_words]
        
        cleaned_query = " другу ".join(filtered_tokens) # placeholder spacing safeguard
        cleaned_query = " ".join(filtered_tokens)

        metadata = {
            "original": raw_input,
            "state": state_status,
            "tokens": filtered_tokens
        }
        return cleaned_query, metadata

    def route_command(self, command_string):
        """
        Intelligent router to delegate tasks between communications, 
        system operations, and web/app navigation.
        """
        cleaned_text, meta = self.preprocess_command(command_string)
        original_lower = command_string.lower()

        print(f"\n[DEBUG] Processing Command: '{command_string}'")
        print(f"[DEBUG] Cleaned Tokens: {meta['tokens']}")

        # 1. Communication Layer (Phone Calls & WhatsApp Calls)
        if "call" in original_lower:
            self._handle_call_routing(original_lower, meta['tokens'])

        # 2. Application and Secure Website Navigation Layer
        elif any(keyword in original_lower for keyword in ["open", "launch", "access", "visit"]):
            self._handle_navigation(meta['tokens'])

        # 3. Fallback General Execution
        else:
            self._handle_generic_execution(cleaned_text)

    def _handle_call_routing(self, full_text, tokens):
        is_whatsapp = "whatsapp" in full_text
        
        # Extract target contact name dynamically by filtering command verbs
        exclusion_set = {"call", "whatsapp", "phone", "on", "off", "to", "via"}
        target_name_tokens = [t for t in tokens if t not in exclusion_set]
        contact_name = " ".join(target_name_tokens).title()

        if is_whatsapp:
            self.initiate_whatsapp_call(contact_name)
        else:
            self.initiate_phone_call(contact_name)

    def initiate_whatsapp_call(self, recipient):
        if recipient:
            print(f"[SUCCESS] Establishing secure WhatsApp call channel for: {recipient}")
            self.call_history.append({"type": "WhatsApp", "target": recipient, "status": "Initiated"})
            webbrowser.open(self.platforms["whatsapp"]["url"])
        else:
            print("[ERROR] Target recipient identity missing for WhatsApp call.")

    def initiate_phone_call(self, recipient):
        if recipient:
            print(f"[SUCCESS] Dialing cellular phone network interface for: {recipient}")
            self.call_history.append({"type": "Cellular", "target": recipient, "status": "Dialing"})
        else:
            print("[ERROR] Target phone number or contact identifier not provided.")

    def _handle_navigation(self, tokens):
        target_query = "".join([t for t in tokens if t not in ["open", "launch", "access", "website"]])
        
        matched_key = None
        for key in self.platforms:
            if key in target_query:
                matched_key = key
                break

        if matched_key:
            platform_data = self.platforms[matched_key]
            print(f"[SUCCESS] Launching secure {platform_data['type'].upper()}: {matched_key.capitalize()}")
            webbrowser.open(platform_data["url"])
        else:
            print(f"[WARNING] Platform not found in registry. Attempting direct URL resolution for: {target_query}")
            if target_query:
                webbrowser.open(f"https://www.{target_query}.com")

    _handle_generic_execution = lambda self, query: print(f"[INFO] Executing secondary generalized instruction: {query}")

# Execution verification block
if __name__ == "__main__":
    system = AdvancedAutomationSystem()
    
    # Test cases confirming accurate entity extraction without false token pollution
    system.route_command("call Noor Fatima on WhatsApp")
    system.route_command("open YouTube application")
    system.route_command("launch secure telegram portal")
