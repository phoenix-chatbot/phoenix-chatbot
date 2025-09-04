import json
import difflib

# Load Q&A data from qa.json
with open("qa.json", "r", encoding="utf-8") as f:
    qa = json.load(f)

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Exact match first
    if user_input in qa:
        return qa[user_input]

    # Fuzzy match: find closest key in qa.json
    closest_matches = difflib.get_close_matches(user_input, qa.keys(), n=1, cutoff=0.4)
    if closest_matches:
        best_match = closest_matches[0]
        return qa[best_match]

    # If nothing matches
    return "Hmm... I’m not sure, but I’ll keep learning! 😊"

if __name__ == "__main__":
    print("Phoenix Chatbot (fuzzy). Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", get_response(user_input))
