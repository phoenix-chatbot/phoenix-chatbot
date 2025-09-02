from flask import Flask, render_template, request, jsonify
import json
import difflib  # for fuzzy matching

app = Flask(__name__)

# Load Q&A data from qa.json
with open("qa.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

# Convert Q&A into dictionary (all lowercase)
qa_dict = {item["question"].lower(): item["answer"] for item in qa_data}


def get_answer(user_input):
    # Normalize user input
    user_input = user_input.lower().strip()

    # If exact match exists
    if user_input in qa_dict:
        return qa_dict[user_input]

    # Otherwise, find closest match using difflib
    possible_matches = difflib.get_close_matches(user_input, qa_dict.keys(), n=1, cutoff=0.6)
    if possible_matches:
        return qa_dict[possible_matches[0]]

    # If no match at all
    return "Sorry, I don't have an answer for that yet."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json.get("message")
    response = get_answer(user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
