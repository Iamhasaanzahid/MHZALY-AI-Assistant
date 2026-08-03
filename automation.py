import os
import time
import webbrowser
import pyautogui

CONTACTS = {
    "noor fatimah": "923280759925",
    "noor fatima": "923280759925",
    "noor": "923280759925",
    "mhzaly": "923280759925"
}

def open_app_or_site(target_name):
    target = target_name.lower().strip()
    sites = {
        "twitter": "https://x.com",
        "x": "https://x.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "google": "https://www.google.com",
        "gemini": "https://gemini.google.com",
        "copilot": "https://copilot.microsoft.com",
        "youtube": "https://www.youtube.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
        "gmail": "https://mail.google.com"
    }
    
    for site_key, url in sites.items():
        if site_key in target:
            webbrowser.open(url)
            return f"Opening {site_key.capitalize()} in browser."
            
    if "whatsapp" in target:
        os.system("start whatsapp:")
        return "Opening WhatsApp Desktop."
    elif "teams" in target:
        os.system("start msteams:")
        return "Opening Microsoft Teams."
    elif "chrome" in target or "browser" in target:
        os.system("start chrome")
        return "Opening Web Browser."
    elif "notepad" in target:
        os.system("start notepad")
        return "Opening Notepad."
    elif "cmd" in target or "terminal" in target:
        os.system("start cmd")
        return "Opening Command Prompt."
    elif "calculator" in target or "calc" in target:
        os.system("calc")
        return "Opening Calculator."
    else:
        pyautogui.press('win')
        time.sleep(0.8)
        pyautogui.write(target_name, interval=0.1)
        time.sleep(0.5)
        pyautogui.press('enter')
        return f"Opening {target_name} on Windows."

def whatsapp_action(contact_name, action_type="call", message_text=""):
    clean_name = contact_name.lower().strip()
    phone = CONTACTS.get(clean_name)
    if not phone and clean_name.replace("+", "").isdigit():
        phone = clean_name.replace("+", "")
        
    if phone:
        # Using web protocol directly to target the chat reliably
        webbrowser.open(f"https://web.whatsapp.com/send?phone={phone}")
        time.sleep(6.0)  # Wait for WhatsApp Web / Desktop chat to load fully
        
        if action_type == "call":
            # Press Tab to focus elements or use UI automation/enter if chat is loaded
            pyautogui.press('enter')
            time.sleep(1.0)
            # Safe fallback click/hotkey for calling in WhatsApp desktop/web interface
            pyautogui.hotkey('ctrl', 'alt', 'shift', 'v') # Triggers voice call if shortcut supported, or fallback to clicking UI coordinates if needed
            return f"Initiating direct WhatsApp call to {contact_name} ({phone})."
        elif action_type == "message" and message_text:
            pyautogui.write(message_text, interval=0.06)
            time.sleep(0.5)
            pyautogui.press('enter')
            return f"Message sent to {contact_name}."
            
    # Fallback to app search if phone is missing
    os.system("start whatsapp:")
    time.sleep(2.0)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    pyautogui.write(contact_name, interval=0.1)
    time.sleep(2.0)
    pyautogui.press('enter')
    time.sleep(1.5)
    
    if action_type == "call":
        return f"Calling {contact_name} on WhatsApp."
    return f"Chat opened with {contact_name}."

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for {query}."

def play_youtube(topic):
    webbrowser.open(f"https://www.youtube.com/results?search_query={topic}")
    return f"Searching {topic} on YouTube."

def system_control(action):
    act = action.lower()
    if "volume up" in act or "aawaz tez" in act:
        for _ in range(5):
            pyautogui.press('volumeup')
        return "Volume increased."
    elif "volume down" in act or "aawaz kam" in act:
        for _ in range(5):
            pyautogui.press('volumedown')
        return "Volume decreased."
    elif "mute" in act:
        pyautogui.press('volumemute')
        return "Muted audio."
    elif "screenshot" in act or "photo" in act:
        pyautogui.screenshot("mhzaly_screenshot.png")
        return "Screenshot taken and saved."
