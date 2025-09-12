from flask import Flask, render_template, request, jsonify
import json
from fuzzywuzzy import process

app = Flask(__name__)

# Load Q&A
with open("qa.json", "r", encoding="utf-8") as f:
    qa_pairs = json.load(f)

def get_answer(user_input):
    questions = list(qa_pairs.keys())
    best_match, score = process.extractOne(user_input, questions)
    if score > 70:
        return qa_pairs[best_match]
    return "Hmm 🤔 I don’t understand that yet."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_reply = get_answer(user_message)
    return jsonify({"reply": bot_reply})

@app.route("/terms")
def terms():
    return render_template("terms.html")

if __name__ == "__main__":
    app.run(debug=True)
