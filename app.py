from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template_string("""
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
        <form method="POST">
            <input name="user_input" placeholder="Type your message..." />
            <button type="submit">Send</button>
        </form>
        {% if request.method == 'POST' %}
            <p><strong>You said:</strong> {{ request.form.get('user_input') }}</p>
        {% endif %}
    </body>
    </html>
    """)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
