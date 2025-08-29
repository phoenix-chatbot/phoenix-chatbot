from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# --------------------------
# Riddles and greetings data
# --------------------------
riddles = [
    {"question": "What has to be broken before you can use it?", "answer": "egg"},
    {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "candle"},
    {"question": "What month of the year has 28 days?", "answer": "all"},
    {"question": "What is full of holes but still holds water?", "answer": "sponge"},
    {"question": "What question can you never answer yes to?", "answer": "are you asleep"},
    {"question": "What is always in front of you but can’t be seen?", "answer": "future"},
    {"question": "There’s a one-story house in which everything is yellow. What color are the stairs?", "answer": "no stairs"},
    {"question": "What can you break, even if you never pick it up or touch it?", "answer": "promise"},
    {"question": "What goes up but never comes down?", "answer": "age"},
    {"question": "A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?", "answer": "bald"}
]

greetings = ["hi", "hello", "hey", "xup", "sup", "yo", "good morning", "good afternoon", "good evening"]

# Track scores per session (for now stored in memory)
scores = {"user": 0, "bot": 0}

# --------------------------
# Chatbot logic
# --------------------------
def chatbot_response(user_input):
    text = user_input.strip().lower()

    # Check greetings
    if text in greetings:
        return random.choice(["Hey there! 👋", "Hello! 😃", "What’s up? 🚀", "Yo! 🔥"])

    # Handle riddles
    if "riddle" in text:
        riddle = random.choice(riddles)
        return f"Riddle time! 🤔 {riddle['question']} (Type your answer)"

    # Check answers
    for r in riddles:
        if r["answer"] in text:
            scores["user"] += 1
            return f"✅ Correct! Your score: {scores['user']}"
    # If input doesn’t match
    return "🤖 I don’t understand… Try saying 'riddle' or greet me with 'hi'!"

# --------------------------
# Flask routes
# --------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message")
    response = chatbot_response(user_message)
    return jsonify({"reply": response})

# --------------------------
# Run the app
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)
