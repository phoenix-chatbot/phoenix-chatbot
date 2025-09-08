import json
import wikipedia
import markdown2

# Load predefined Q&A
with open("qa.json", "r", encoding="utf-8") as f:
    qa = json.load(f)

def format_response(text: str) -> str:
    """Convert Markdown reply into safe HTML."""
    return markdown2.markdown(text)

def get_response(user_input: str) -> str:
    text = user_input.lower().strip()

    # 1. Check in qa.json
    if text in qa:
        return format_response(f"💡 **{qa[text]}**")

    # 2. Wikipedia fallback
    if len(text.split()) > 1:
        try:
            summary = wikipedia.summary(text, sentences=2)
            if len(summary) > 300:
                summary = summary[:300] + "..."
            return format_response(f"📘 **Here’s what I found:**\n\n{summary}")
        except:
            return format_response("⚠️ _Sorry, I couldn’t find info on that._")

    # 3. Greetings
    greetings = ["hi", "hello", "hey", "xup", "good morning", "good night"]
    if text in greetings:
        return format_response("👋 **Hello there!** How can I help you today?")

    # 4. Default response
    return format_response("🤖 _I'm **Phoenix** — your AI assistant. Try asking me anything!_")
