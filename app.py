from flask import Flask, request, render_template_string
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key (secure this later!)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Best practice: set in Render's environment

# HTML with chat form
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Phoenix Chatbot</title>
    <meta name="google-adsense-account" content="ca-pub-5149547050862927">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5149547050862927" crossorigin="anonymous"></script>
</head>
<body>
    <h1>Welcome to Phoenix Chatbot</h1>
    <form method="POST">
        <label>Ask something:</label><br>
        <input type="text" name="user_input" style="width:300px;" required>
        <button type="submit">Send</button>
    </form>
    {% if reply %}
        <p><strong>Phoenix:</strong> {{ reply }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    reply = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Phoenix, a helpful chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
    return render_template_string(HTML_PAGE, reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
