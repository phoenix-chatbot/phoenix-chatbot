from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load Q&A database
with open("qa.json", "r", encoding="utf-8") as f:
    qa = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower().strip()

    # Search in qa.json
    reply = qa.get(message, "🤔 Sorry, I don’t understand that yet.")
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
