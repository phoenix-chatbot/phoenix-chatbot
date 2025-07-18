from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Phoenix Chatbot</title>
        <style>
            body { font-family: Arial; max-width: 600px; margin: auto; padding: 30px; background: #f4f4f4; }
            #chatbox { border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: scroll; background: white; }
            .msg { margin: 10px 0; }
            .user { color: blue; }
            .bot { color: green; }
        </style>
        <script>
            async function sendMessage() {
                const userInput = document.getElementById("userInput").value;
                const chatbox = document.getElementById("chatbox");
                chatbox.innerHTML += '<div class="msg user"><b>You:</b> ' + userInput + '</div>';
                document.getElementById("userInput").value = "";
                const res = await fetch("/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message: userInput })
                });
                const data = await res.json();
                chatbox.innerHTML += '<div class="msg bot"><b>Phoenix:</b> ' + data.reply + '</div>';
                chatbox.scrollTop = chatbox.scrollHeight;
            }
        </script>
    </head>
    <body>
        <h2>Phoenix Chatbot</h2>
        <div id="chatbox"></div>
        <input type="text" id="userInput" placeholder="Type your message..." onkeydown="if(event.key==='Enter') sendMessage()"/>
        <button onclick="sendMessage()">Send</button>
    </body>
    </html>
    """)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    # 🧠 Replace this with your real logic later
    reply = f"You said: {user_message}"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
