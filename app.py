from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_reply():
    user_message = request.json.get("message")
    bot_response = get_response(user_message)
    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
