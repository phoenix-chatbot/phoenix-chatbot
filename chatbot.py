import json

# Load Q&A from qa.json
with open("qa.json", "r", encoding="utf-8") as f:
    qa = json.load(f)

def get_response(user_input):
    user_input = user_input.lower().strip()
    return qa.get(user_input, "Sorry, I don't understand that yet.")

if __name__ == "__main__":
    print("Phoenix Chatbot (Q&A only). Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye 👋")
            break
        print("Bot:", get_response(user_input))
