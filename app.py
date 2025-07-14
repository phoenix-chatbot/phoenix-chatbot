from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    # 🔥 Replace this with your AI logic later
    bot_reply = f"You said: {user_message}"
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
