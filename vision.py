import pyautogui
import os
from google import genai
from google.genai import types

def capture_and_analyze_screen(client):
    """Captures Laptop Screen and Analyzes it using Gemini Vision"""
    print("📸 MHZALY is looking at your screen...")
    
    # 1. Take Screenshot
    screenshot_path = "screen_capture.png"
    pyautogui.screenshot(screenshot_path)
    
    try:
        # 2. Upload Screen Image to Gemini
        with open(screenshot_path, "rb") as f:
            image_bytes = f.read()
            
        # 3. Analyze Screen using Gemini Vision
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                "Describe what is currently visible on my laptop screen in concise Urdu/English and explain what I should do next."
            ]
        )
        
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
            
        return response.text
    except Exception as e:
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
        return f"Screen vision error: {e}"