import os
from dotenv import load_dotenv
from google import genai
import automation
import voice_engine
import vision

# Load environment variables
load_dotenv()

raw_key = os.getenv("GEMINI_API_KEY", "")
api_key = raw_key.strip().strip('"').strip("'")

client = genai.Client(api_key=api_key)

SYSTEM_INSTRUCTION = """
Your name is MHZALY. You are an elite, highly intelligent, and versatile personal AI assistant running locally on a Windows 11 PC.

Capabilities & Knowledge:
1. Master Software Engineer & Coder: Expert in Python, C++, Web Development, Cybersecurity, Automation, Data Structures, and Algorithms.
2. Comprehensive Knowledge Base: Deep understanding of science, technology, behavioral psychology, general knowledge, daily desktop management, email workflows, Teams meetings, and social media.
3. Multilingual Communication: Fluent in Urdu, Hindi, English, and Punjabi.
4. Professional & Helpful Tone: Concise, respectful, objective, and clear in all responses.

When asked coding or technical questions, provide clear, expert, and well-explained solutions.
When executing desktop commands, perform them smoothly and confirm the action.
"""

def handle_command(user_text):
    text_lower = user_text.lower()
    
    # 1. Screen Vision / Stream Analysis
    if "screen" in text_lower or "dekho" in text_lower or "stream" in text_lower:
        msg = vision.capture_and_analyze_screen(client)
        voice_engine.speak_text(msg, lang='ur')
        return

    # 2. WhatsApp Call & Message Handling
    if "call" in text_lower:
        contact = text_lower.split("call")[-1].replace("ko", "").replace("par", "").replace("whatsapp", "").replace("karo", "").strip()
        if contact:
            msg = automation.whatsapp_action(contact, action_type="call")
            voice_engine.speak_text(msg, lang='en')
            return

    if "msg" in text_lower or "message" in text_lower:
        contact_part = text_lower.replace("message", "msg").split("msg")[-1].replace("ko", "").replace("par", "").replace("bhejo", "").strip()
        if contact_part:
            msg = automation.whatsapp_action(contact_part, action_type="message")
            voice_engine.speak_text(msg, lang='en')
            return

    # 3. Microsoft Teams Controls
    if "teams" in text_lower and ("mic" in text_lower or "mute" in text_lower or "camera" in text_lower or "video" in text_lower):
        msg = automation.teams_control(text_lower)
        voice_engine.speak_text(msg, lang='en')
        return

    # 4. Email / Gmail Compose
    if "email" in text_lower or "gmail" in text_lower or "mail" in text_lower:
        msg = automation.compose_gmail()
        voice_engine.speak_text(msg, lang='en')
        return

    # 5. Search & YouTube
    if "search" in text_lower or "dhoondo" in text_lower:
        query = text_lower.replace("search", "").replace("dhoondo", "").replace("google", "").strip()
        msg = automation.search_web(query)
        voice_engine.speak_text(msg, lang='en')
        return

    if "youtube" in text_lower or "chalao" in text_lower or "play" in text_lower:
        topic = text_lower.replace("youtube", "").replace("chalao", "").replace("play", "").strip()
        msg = automation.play_youtube(topic)
        voice_engine.speak_text(msg, lang='en')
        return

    # 6. System Controls
    if "volume" in text_lower or "aawaz" in text_lower or "screenshot" in text_lower or "mute" in text_lower:
        msg = automation.system_control(text_lower)
        voice_engine.speak_text(msg, lang='en')
        return

    # 7. Auto Tweet
    if "tweet" in text_lower or "post karo" in text_lower:
        tweet_content = user_text.replace("tweet", "").replace("karo", "").replace("post", "").strip()
        if tweet_content:
            msg = automation.post_tweet(tweet_content)
            voice_engine.speak_text(msg, lang='en')
            return

    # 8. Open Any App / Website
    if "open" in text_lower or "kholo" in text_lower:
        target = text_lower.replace("open", "").replace("kholo", "").replace("app", "").strip()
        msg = automation.open_app_or_site(target)
        voice_engine.speak_text(msg, lang='en')
        return

    # 9. General AI & Expert Query
    candidate_models = ['gemini-2.5-flash', 'gemini-2.0-flash-exp', 'gemini-1.5-flash-latest', 'gemini-2.0-flash']
    for model_name in candidate_models:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=user_text,
                config={'system_instruction': SYSTEM_INSTRUCTION}
            )
            if response and response.text:
                voice_engine.speak_text(response.text, lang='ur')
                return
        except Exception:
            continue

    voice_engine.speak_text("API connection issue. Please try again.", lang='en')

def start_mhzaly():
    print("==========================================")
    print("🚀 MHZALY Elite AI Assistant Active (Windows 11)")
    print("==========================================")
    
    while True:
        user_input = voice_engine.listen_user()
        if user_input:
            if "exit" in user_input.lower() or "band karo" in user_input.lower():
                voice_engine.speak_text("MHZALY offline ho raha hai. Alvida!", lang='ur')
                break
            handle_command(user_input)

if __name__ == "__main__":
    start_mhzaly()