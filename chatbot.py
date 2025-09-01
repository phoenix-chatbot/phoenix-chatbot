import json
from googletrans import Translator

# Load Q&A from JSON file
with open("qa.json", "r", encoding="utf-8") as f:
    qa_pairs = json.load(f)

# Create translator object
translator = Translator()

def get_response(user_input):
    try:
        # Detect language
        detected = translator.detect(user_input)
        user_lang = detected.lang

        # Translate user input to English
        translated_text = translator.translate(user_input, src=user_lang, dest="en").text.lower()

        # Find best match
        response = None
        for question, answer in qa_pairs.items():
            if question in translated_text:
                response = answer
                break

        if not response:
            response = "Sorry, I don’t understand that yet."

        # Translate response back to original language
        final_response = translator.translate(response, src="en", dest=user_lang).text

        return final_response

    except Exception as e:
        return "Error: " + str(e)
