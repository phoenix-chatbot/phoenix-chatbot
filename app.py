from flask import Flask, request, render_template_string
import openai
import os

app = Flask(__name__)

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Phoenix Chatbot</title>
    <meta name="google-adsense-account" content="ca-pub-5149547050862927">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5149547050862927"
        crossorigin="anonymous"></script>
</head>
<body>
    <h1>Welcome to Phoenix Chatbot</h1>
    <form method="post">
        <input type="text" name="user_input" placeholder="Ask me anything..." required>
        <button type="submit">Send</button>
    </form>
    {% if user_input %}
        <p><strong>You:</strong> {{ user_input }}</p>
        <p><strong>Phoenix:</strong> {{ response }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    user_input = None

    if request.method == "POST":
        user_input = request.form["user_input"]

        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant named Phoenix."},
                    {"role": "user", "content": user_input}
                ]
            )
            response = completion.choices[0].message.content.strip()
        except Exception as e:
            response = "Sorry, something went wrong."

    return render_template_string(html_template, user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
