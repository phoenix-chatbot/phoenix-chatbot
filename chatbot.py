import random

# Expanded riddles list
riddles = [
    {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo", "hint": "It repeats what you say."},
    {"question": "What has to be broken before you can use it?", "answer": "egg", "hint": "Breakfast food."},
    {"question": "The more of me you take, the more you leave behind. What am I?", "answer": "footsteps", "hint": "You leave them on the ground."},
    {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "candle", "hint": "It melts as it burns."},
    {"question": "What goes up but never comes down?", "answer": "age", "hint": "Everyone has it, and it increases yearly."},
    {"question": "The more you take away from me, the bigger I get. What am I?", "answer": "hole", "hint": "You dig it."},
    {"question": "What has hands but can’t clap?", "answer": "clock", "hint": "It tells time."},
    {"question": "The more you share me, the less I become. What am I?", "answer": "secret", "hint": "Don’t tell anyone."},
    {"question": "What can travel around the world while staying in the same corner?", "answer": "stamp", "hint": "It sticks to letters."},
    {"question": "What has many keys but can’t open a lock?", "answer": "piano", "hint": "It makes music."},
    {"question": "What gets wetter as it dries?", "answer": "towel", "hint": "You use it after bathing."},
    {"question": "What has one eye but cannot see?", "answer": "needle", "hint": "Used in sewing."},
    {"question": "What belongs to you but others use it more than you?", "answer": "name", "hint": "People call you by it."},
    {"question": "What has a heart that doesn’t beat?", "answer": "artichoke", "hint": "A type of vegetable."},
]

# Greeting & small talk responses
responses = {
    "hi": "Hey there! 👋 Ready for a riddle?",
    "hello": "Hello! 😃 Want to try a riddle?",
    "xup": "I’m good! How about you? Ready for a riddle?",
    "sup": "All good here! 💯 Want a riddle?",
    "hey": "Hey! 🔥 Let’s play riddles.",
    "good morning": "Good morning ☀️ Hope your day goes well! Want a riddle?",
    "good afternoon": "Good afternoon 😎 Ready to test your brain?",
    "good evening": "Good evening 🌙 Let’s end the day with a riddle!",
    "how are you": "I’m doing great, thanks for asking! You?",
    "fine": "That’s good to hear! 🎉",
    "i’m fine": "Awesome! Let’s have some fun with a riddle.",
    "am fine": "Nice one 😃 Shall we do a riddle?",
}

# Main chatbot function
def chatbot():
    print("Phoenix Chatbot 🔥")
    print("Type 'quit' to exit anytime.")
    print("Type 'hint' if you need a clue.")

    score = 0
    while True:
        user_input = input("\nYou: ").lower().strip()

        # Exit
        if user_input == "quit":
            print(f"Chatbot: Bye 👋 Your final score is {score}.")
            break

        # Greetings & small talk
        if user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
            continue

        # Random riddle
        riddle = random.choice(riddles)
        print(f"Chatbot: 🤔 {riddle['question']}")

        # Answer loop
        while True:
            answer = input("You: ").lower().strip()

            if answer == "quit":
                print(f"Chatbot: Bye 👋 Your final score is {score}.")
                return

            if answer == "hint":
                print(f"Chatbot: 🔑 Hint → {riddle['hint']}")
                continue

            if answer == riddle["answer"]:
                print("Chatbot: ✅ Correct! Nice one.")
                score += 1
                print(f"Chatbot: 🎯 Your score: {score}")
                break
            else:
                print("Chatbot: ❌ Nope, try again or type 'hint'.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
