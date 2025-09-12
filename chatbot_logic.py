import json
from difflib import get_close_matches

# Load Q&A from qa.json
with open("qa.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

def get_response(user_input):
    # Fuzzy match
    matches = get_close_matches(user_input.lower(), qa_data.keys(), n=1, cutoff=0.6)
    if matches:
        return qa_data[matches[0]]
    else:
        return "Phoenix: I'm not sure, but I'll keep learning 🔥"
