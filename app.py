# app.py
import os
from flask import Flask, render_template, request, jsonify
from chatbot_ai import ask_ai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_reply():
    data = request.get_json() or {}
    user_text = data.get("message", "").strip()
    if not user_text:
        return jsonify({"reply": "Please type a question."})

    # ask AI and get a reply (AI will reply in user's language)
    reply = ask_ai(user_text)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    # In production set debug=False
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
