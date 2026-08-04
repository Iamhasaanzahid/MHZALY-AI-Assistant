import asyncio
import os
import pygame
import speech_recognition speech_recognition as sr
from edge_tts import Communicate

LANGUAGE_VOICES = {
    "ur": "ur-PK-UzmaNeural",
    "en": "en-US-AndrewNeural",
    "es": "es-ES-ElenaNeural",
    "ar": "ar-SA-HamdanNeural",
    "fr": "fr-FR-DeniseNeural",
    "de": "de-DE-KatjaNeural",
    "zh": "zh-CN-XiaoxiaoNeural"
}

def listen_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for input...")
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None

async def edge_tts_speak(text, voice_name):
    output_file = "response.mp3"
    try:
        communicate = Communicate(text, voice_name)
        await communicate.save(output_file)

        pygame.mixer.init()
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        pygame.mixer.quit()

        if os.path.exists(output_file):
            os.remove(output_file)

    except Exception as e:
        print(f"TTS Error: {e}")

def speak_text(text, lang_code="en"):
    voice = LANGUAGE_VOICES.get(lang_code, "en-US-AndrewNeural")
    print(f"MHZALY: {text}")
    asyncio.run(edge_tts_speak(text, voice))

if __name__ == "__main__":
    while True:
        user_input = listen_user()
        if user_input:
            speak_text(user_input, lang_code="en")
