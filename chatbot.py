<<<<<<< HEAD
import json
import os
import random
import pyttsx3
import speech_recognition as sr

print("🚀 Phoenix Chatbot is starting...")  # Early marker so you see startup

# -------------------------------
# Files & persistence
# -------------------------------
SCORES_FILE = "scores.json"

def load_scores():
    """Load all players' scores safely. Never crash on bad/corrupt JSON."""
    try:
        if not os.path.exists(SCORES_FILE):
            return {}
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
    except (json.JSONDecodeError, OSError, ValueError):
        # Auto-recover from corrupt file
        print("⚠️  scores.json was invalid — starting fresh.")
        return {}

def save_scores(scores: dict):
    """Atomically save scores so we don't create empty/corrupt files."""
    tmp = SCORES_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(scores, f)
    os.replace(tmp, SCORES_FILE)

# -------------------------------
# Text-to-speech (safe)
# -------------------------------
def init_tts():
    try:
        eng = pyttsx3.init()
        return eng
    except Exception as e:
        print(f"⚠️  TTS init failed, continuing without voice. ({e})")
        return None

engine = init_tts()

def speak(text: str):
    if engine is None:
        return
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"⚠️  TTS speak failed: {e}")

# -------------------------------
# Mic input (safe)
# -------------------------------
def get_voice_input(timeout_sec=5) -> str:
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            audio = r.listen(source, timeout=timeout_sec)
        try:
            return r.recognize_google(audio)
        except Exception:
            return ""
    except Exception as e:
        print(f"⚠️  Mic not available: {e}")
        return ""

# -------------------------------
# Riddles
# -------------------------------
=======
import pyttsx3
import random
import speech_recognition as sr

# Text-to-speech setup
engine = pyttsx3.init()

# Riddles
>>>>>>> cca9003390c4cd4ec63e2143f37f4bda2de88e59
riddles = [
    {"question": "What has to be broken before you can use it?", "answer": "egg"},
    {"question": "What goes up but never comes down?", "answer": "age"},
    {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "candle"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "What has keys but can’t open locks?", "answer": "piano"},
<<<<<<< HEAD
    {"question": "What gets wetter the more it dries?", "answer": "towel"}
]

# -------------------------------
# Levels
# -------------------------------
def get_level(score: int) -> str:
    if score < 5:
        return "Beginner Riddler 🌱"
    elif score < 10:
        return "Smart Thinker 💡"
    elif score < 20:
        return "Sharp Mind ⚡"
    else:
        return "Phoenix Master 👑🔥"

# -------------------------------
# Greeting & player setup
# -------------------------------
print("🔥 Phoenix Chatbot Activated. Ready to riddle, vibe, and talk!\n")
name = input("👤 What's your name? ").strip() or "Player"
name_key = name.lower()

# Load scores AFTER we know the player's name (avoids early JSON crashes)
scores = load_scores()
score = int(scores.get(name_key, 0))

hello_line = f"Hello {name}! I'm ready to chat. Type 'help' for commands."
print("\n🤖 " + hello_line + "\n")
speak(hello_line)

# -------------------------------
# Command help
# -------------------------------
HELP_TEXT = (
    "📜 Commands:\n"
    "  - riddle        → get a random riddle\n"
    "  - score         → show your score & level\n"
    "  - reset score   → set your score to 0\n"
    "  - hello / bye   → greet or exit\n"
    "  - help          → show this help\n"
    "You can type OR just press Enter to speak."
)

# -------------------------------
# Chat loop
# -------------------------------
try:
    while True:
        print(f"\n{name}, you can type or speak. 🎙️ Waiting for input...")
        user_input = input(f"{name}: ").strip().lower()

        if not user_input:
            heard = get_voice_input().strip().lower()
            if heard:
                user_input = heard
                print(f"(You said): {user_input}")
            else:
                print("🤖 I didn't catch anything.")
                continue

        if user_input in ("exit", "bye", "quit"):
            farewell = f"Alright {name}, goodbye for now. 🔥 Your score is {score} ({get_level(score)})."
            print("Bot:", farewell)
            speak(farewell)
            scores[name_key] = score
            save_scores(scores)
            break

        elif user_input in ("help", "commands", "?"):
            print(HELP_TEXT)
            speak("Here are your commands.")

        elif "hello" in user_input:
            reply = f"Hey there, {name}! 👋"
            print("Bot:", reply)
            speak(reply)

        elif "how are you" in user_input:
            reply = "Alive, upgraded, and coded. You?"
            print("Bot:", reply)
            speak(reply)

        elif "who are you" in user_input:
            reply = "I'm Phoenix — your fiery Python chatbot assistant. 🐍"
            print("Bot:", reply)
            speak(reply)

        elif "music" in user_input:
            reply = "I can’t hear music, but Asake’s name sounds like vibes. 🎶"
            print("Bot:", reply)
            speak(reply)

        elif "sad" in user_input:
            reply = "Even bots feel down sometimes. But we rise, Phoenix style. 🔥"
            print("Bot:", reply)
            speak(reply)

        elif user_input == "score":
            reply = f"🔥 {name}, your current score is {score}. Level: {get_level(score)}."
            print("Bot:", reply)
            speak(reply)

        elif user_input == "reset score":
            score = 0
            scores[name_key] = score
            save_scores(scores)
            reply = "✅ Score reset to 0. Back to the grind!"
            print("Bot:", reply)
            speak(reply)

        elif "riddle" in user_input:
            riddle = random.choice(riddles)
            print(f"🤔 Bot (riddle): {riddle['question']}")
            speak(riddle["question"])
            answer = input(f"{name} (answer): ").strip().lower()
            if riddle["answer"] in answer:
                score += 1
                reply = f"✅ Correct! Your score is now {score}. Level: {get_level(score)}."
            else:
                reply = f"❌ Nope. The answer was '{riddle['answer']}'. Score: {score}. Level: {get_level(score)}."
            print("Bot:", reply)
            speak(reply)
            scores[name_key] = score
            save_scores(scores)

        else:
            reply = "🤖 I didn't catch that... type 'help', try a riddle, or say 'exit'."
            print("Bot:", reply)
            speak(reply)

except KeyboardInterrupt:
    # Graceful Ctrl+C exit
    print("\n🛑 Interrupted. Saving your progress...")
    scores[name_key] = score
    save_scores(scores)
    print("✅ Saved. Bye!")
=======
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
>>>>>>> cca9003390c4cd4ec63e2143f37f4bda2de88e59
