from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        return f"<h1>POST received: {user_input}</h1><a href='/'>Go back</a>"
    return '''
        <form method="POST">
            <input name="user_input" />
            <button type="submit">Send</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
