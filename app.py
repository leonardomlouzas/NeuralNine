from flask import Flask, render_template, session

app = Flask(__name__, template_folder="templates")
app.secret_key = "Secret Key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/session_set")
def session_set():
    session["username"] = "Leo"
    session["message"] = "Hello, World"

    return render_template("index.html", message="Session data set successfully")


if __name__ == "__main__":
    app.run(debug=True)
