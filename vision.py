import os
import time
import pyautogui
from google import genai
from google.genai import types

def capture_and_analyze_screen(client):
    """Captures the laptop screen, sends it to the Gemini API, and returns the analysis."""
    print("MHZALY AI is looking at your screen...")
    
    screenshot_path = "screen_capture.png"
    pyautogui.screenshot(screenshot_path)
    
    try:
        with open(screenshot_path, "rb") as f:
            image_bytes = f.read()

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type='image/png',
                ),
                "Analyze the current screen and provide a concise Urdu/English description, highlighting MHZALY system status and recommended actions."
            ]
        )
        return response.text

    except Exception as e:
        return f"Vision processing error: {e}"

    finally:
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

if __name__ == "__main__":
    # Ensure you have initialized your client properly with your API key
    client = genai.Client()
    analysis = capture_and_analyze_screen(client)
    print(analysis)
