from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Phoenix Chatbot</title>
    <meta name="google-adsense-account" content="ca-pub-5149547050862927">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5149547050862927"
        crossorigin="anonymous"></script>
    <style>
        body { font-family: Arial; padding: 20px; background: #f9f9f9; text-align: center; }
        input[type=text] { width: 60%; padding: 10px; font-size: 16px; }
        button { padding: 10px 20px; font-size: 16px; background: orange; color: white; border: none; cursor: pointer; }
        button:hover { background: darkorange; }
        .chat-box { margin-top: 30px; background: white; padding: 20px; border-radius: 10px; max-width: 600px; margin: 30px auto 0 auto; text-align: left; }
    </style>
</head>
<body>
    <h1>🔥 Phoenix is online and ready to chat 🔥</h1>
    <form method="POST">
        <input type="text" name="user_input" placeholder="Type your message..." required />
        <button type="submit">Send</button>
    </form>

    {% if user_input %}
    <div class="chat-box">
        <p><strong>You:</strong> {{ user_input }}</p>
        <p><strong>Phoenix:</strong> {{ response }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    user_input = ""
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        # Simulate chatbot response (replace this with your real logic)
        response = f"I heard you say: {user_input}"
    return render_template_string(html_template, user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
