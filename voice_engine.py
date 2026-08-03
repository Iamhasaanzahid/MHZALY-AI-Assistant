import asyncio
import edge_tts
import pygame
import os

# Microsoft Neural Urdu Voices:
# 1. "ur-PK-UzmaNeural" (Pakistani Female)
# 2. "ur-PK-AsadNeural" (Pakistani Male)
# 3. "ur-IN-GulNeural"  (Urdu Female)
# 4. "ur-IN-SalmanNeural" (Urdu Male)

SELECTED_VOICE = "ur-PK-UzmaNeural"  # Change to "ur-PK-AsadNeural" for Male voice

def listen_user():
    """Tries microphone input; falls back to console text input if PyAudio is missing"""
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("\n🎤 MHZALY Sun raha hai... (Speak Urdu/Hindi/English)")
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="ur-PK")
            print(f"👤 Aapne kaha: {text}")
            return text
    except Exception:
        text = input("\n💬 MHZALY Command Type Karein (Urdu/Hindi/English): ")
        return text

async def _edge_tts_speak(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("response.mp3")

def speak_text(text, lang='ur', voice=SELECTED_VOICE):
    """High-Quality Microsoft Neural Voice Output"""
    print(f"🤖 MHZALY: {text}")
    try:
        # Generate natural neural voice
        asyncio.run(_edge_tts_speak(text, voice))
        
        # Play audio
        pygame.mixer.init()
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit()
        
        if os.path.exists("response.mp3"):
            os.remove("response.mp3")
    except Exception as e:
        print(f"Speech output error: {e}")