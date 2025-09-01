# chatbot_ai.py
import os
import openai

# Load key from environment (DO NOT hardcode)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set. Set it in your environment before running.")

openai.api_key = OPENAI_API_KEY

# A compact system prompt to ensure helpful multilingual answers
SYSTEM_PROMPT = (
    "You are Phoenix Chatbot — a helpful, safe assistant that replies concisely and correctly. "
    "When a user asks in any language, respond in the same language. "
    "If the user asks to translate, translate. If the user asks something you can't answer, politely say you do not know."
)

def ask_ai(user_text: str) -> str:
    """
    Send the user_text to OpenAI Chat API and return assistant message.
    """
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            max_tokens=512,
            temperature=0.2
        )
        text = resp["choices"][0]["message"]["content"].strip()
        return text
    except Exception as e:
        # Keep error text user-safe and short
        return "Sorry, I couldn't get an answer right now. Try again in a bit."

# Optional quick test when running this file directly
if __name__ == "__main__":
    while True:
        q = input("You: ").strip()
        if q.lower() in {"exit", "quit"}:
            break
        print("Bot:", ask_ai(q))
