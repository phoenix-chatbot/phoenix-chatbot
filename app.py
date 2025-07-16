from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple response logic (replace this with your real chatbot logic)
def get_bot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I help you today?"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! 😄"
    elif "bye" in message:
        return "Goodbye! Talk to you later."
    else:
        return "Phoenix is thinking... 🤔 Try asking something else!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = get_bot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
