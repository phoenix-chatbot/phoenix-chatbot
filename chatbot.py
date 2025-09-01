from googletrans import Translator

translator = Translator()

# Q&A knowledge base
qa_pairs = {
    "hi": "Hello! How can I help you today?",
    "xup": "I'm doing great! How about you?",
    "who are you": "I am Phoenix, your friendly chatbot assistant.",
    "bye": "Goodbye! Have a nice day.",
    "help": "Sure, I'm here to help. What do you need?",
}

def get_response(user_input):
    try:
        # Detect user language
        detected_lang = translator.detect(user_input).lang

        # Translate input to English (our base language)
        translated_input = translator.translate(user_input, src=detected_lang, dest="en").text.lower()

        # Match input with known Q&A (fuzzy match)
        response = None
        for key, value in qa_pairs.items():
            if key in translated_input:  # substring match
                response = value
                break

        # If no match found
        if not response:
            response = "Sorry, I don’t understand that yet."

        # Translate response back to user's language
        final_response = translator.translate(response, src="en", dest=detected_lang).text
        return final_response

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
