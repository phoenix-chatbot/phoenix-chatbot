import pyttsx3
import random
import speech_recognition as sr

# Text-to-speech setup
engine = pyttsx3.init()

# Riddles
riddles = [
    {"question": "What has to be broken before you can use it?", "answer": "egg"},
    {"question": "What goes up but never comes down?", "answer": "age"},
    {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "candle"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "What has keys but can’t open locks?", "answer": "piano"},
    {"question": "What gets wetter the more it dries?", "answer": "towel"},
]

# Voice input
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("🎙️ Listening...")
            audio = r.listen(source, timeout=5)
            user_input = r.recognize_google(audio)
            return user_input
        except:
            return ""

# Greet user
print("🔥 Phoenix Chatbot Activated. Ready to riddle, vibe, and talk!\n")
name = input("👤 What's your name? ").strip()
print(f"\n🤖 Hello {name}! I'm ready to chat. Type 'exit' to quit or speak your message.\n")
engine.say(f"Hello {name}! I'm ready to chat.")
engine.runAndWait()

# Chat loop
while True:
    print(f"\n{name}, you can type or speak. 🎙️ Waiting for input...")
    user_input = input(f"{name}: ").strip().lower()

    if not user_input:
        user_input = get_voice_input().lower()
        print(f"(You said): {user_input}")

    if "exit" in user_input or "bye" in user_input:
        farewell = f"Alright {name}, goodbye for now. 🔥"
        print("Bot:", farewell)
        engine.say(farewell)
        engine.runAndWait()
        break

    elif "hello" in user_input:
        reply = f"Hey there, {name}! 👋"
    elif "how are you" in user_input:
        reply = "Alive, upgraded, and coded. You?"
    elif "who are you" in user_input:
        reply = f"I'm Phoenix — your fiery Python chatbot assistant. 🐍"
    elif "music" in user_input:
        reply = "I can’t hear music, but Asake’s name sounds like vibes. 🎶"
    elif "sad" in user_input:
        reply = "Even bots feel down sometimes. But we rise, Phoenix style. 🔥"
    elif "riddle" in user_input:
        riddle = random.choice(riddles)
        print(f"🤔 Bot (riddle): {riddle['question']}")
        engine.say(riddle['question'])
        engine.runAndWait()
        answer = input(f"{name} (answer): ").strip().lower()
        if riddle['answer'] in answer:
            reply = "✅ Correct! You're still sharp. 👑"
        else:
            reply = f"❌ Nope. The answer was '{riddle['answer']}'."
    else:
        reply = "🤖 I didn't catch that... try a riddle, vibe, or just say 'exit'."

    print("Bot:", reply)
    engine.say(reply)
    engine.runAndWait()
