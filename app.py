from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
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
        <p>Your smart assistant.</p>
    </body>
    </html>
    """)
# Route to serve AdSense verification file
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)  # Important: use port 10000 for Render
