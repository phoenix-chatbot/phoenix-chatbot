# app.py
from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
import os
import openai
from dotenv import load_dotenv
import random

# Load .env
load_dotenv()

# Configure OpenAI key and Flask secret from environment
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment (.env or platform env).")

openai.api_key = OPENAI_KEY

app = Flask(__name__)
# use environment variable for secret; fallback to a default for dev only
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-in-production")

# -----------------------
# Server-side session config (filesystem) - avoids cookie-size limits
# For production, prefer Redis/DB-backed session store.
# -----------------------
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = "./flask_session"
app.config["SESSION_PERMANENT"] = False
Session(app)  # apply server-side sessions

# -----------------------
# Riddles (internal flow)
# -----------------------
RIDDLES = [
    {"question": "What has to be broken before you can use it?", "answer": "egg"},
    {"question": "What goes up but never comes down?", "answer": "age"},
    {"question": "I’m tall when I’m young, and short when I’m old. What am I?", "answer": "candle"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "What has keys but can’t open locks?", "answer": "piano"},
    {"question": "What gets wetter the more it dries?", "answer": "towel"},
]

# -----------------------
# Helper: safe message extraction (accept JSON or form)
# -----------------------
def get_user_message(req):
    # prefer JSON (fetch/axios), fallback to form-encoded (jQuery $.post)
    data = {}
    if req.is_json:
        data = req.get_json()
    else:
        data = req.form
    return (data.get("message") or "").strip()

# -----------------------
# Trim history to last N messages to avoid token overload
# -----------------------
def trim_history():
    msgs = session.get("messages", [])
    max_messages = 12  # number of role-content pairs to keep
    if len(msgs) > max_messages:
        session["messages"] = msgs[-max_messages:]

# -----------------------
# Routes
# -----------------------
@app.route("/")
def home():
    # initialize session state if missing
    session.setdefault("messages", [])
    session.setdefault("score", 0)
    session.setdefault("current_riddle", None)
    return render_template("index.html", messages=session["messages"], score=session["score"])

@app.route("/chat", methods=["POST"])
def chat():
    user_message = get_user_message(request)
    if not user_message:
        return jsonify({"reply": "Please type something.", "score": session.get("score", 0)})

    # ensure keys exist
    session.setdefault("messages", [])
    session.setdefault("score", 0)
    session.setdefault("current_riddle", None)

    lower = user_message.lower()

    # ---------- Riddle flow handled internally ----------
    # If user asks for a riddle, send one and store expected answer.
    if "riddle" in lower:
        r = random.choice(RIDDLES)
        session["current_riddle"] = r  # store dict with 'question' and 'answer'
        reply = f"🤔 Riddle: {r['question']}"
        # save user utterance and bot reply in history
        session["messages"].append({"role": "user", "content": user_message})
        session["messages"].append({"role": "assistant", "content": reply})
        trim_history()
        return jsonify({"reply": reply, "score": session["score"]})

    # If a riddle is active, check the user's attempt
    if session.get("current_riddle"):
        expected = session["current_riddle"]["answer"].lower()
        # a simple contains check — feels okay for short riddles
        if expected in lower:
            session["score"] += 1
            reply = f"✅ Correct! The answer was '{expected}'. Your score: {session['score']}. Want another riddle?"
            session["current_riddle"] = None
        else:
            reply = "❌ Not quite. Try again or type 'riddle' for a new one."
        session["messages"].append({"role": "user", "content": user_message})
        session["messages"].append({"role": "assistant", "content": reply})
        trim_history()
        return jsonify({"reply": reply, "score": session["score"]})

    # ---------- General chat via OpenAI for everything else ----------
    # Append the user message to conversation
    session["messages"].append({"role": "user", "content": user_message})
    trim_history()

    # Optionally include a system message to guide persona (only once at the head)
    system_prompt = {
        "role": "system",
        "content": "You are Phoenix Chatbot — friendly, concise, and playful. Keep replies short and helpful."
    }
    # prepare messages for OpenAI API: start with system prompt then session messages
    messages_for_api = [system_prompt] + session["messages"]

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in messages_for_api],
            temperature=0.7,
            max_tokens=300,
        )
        bot_reply = resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        bot_reply = f"⚠️ OpenAI error: {str(e)}"

    # Save assistant reply and trim history
    session["messages"].append({"role": "assistant", "content": bot_reply})
    trim_history()

    return jsonify({"reply": bot_reply, "score": session["score"]})

if __name__ == "__main__":
    app.run(debug=True)
