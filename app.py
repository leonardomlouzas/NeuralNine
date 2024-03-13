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


@app.route("/session_get")
def session_get():
    name = session.get("username")
    message = session.get("message")

    formatted_message = (
        f"{name}. {message}." if name and message else "Session not valid."
    )

    return render_template("index.html", message=formatted_message)


@app.route("/session_delete")
def session_delete():
    # This delete only one info in the session
    session.pop("username")

    # This clear all info in the session
    session.clear()

    return render_template("index.html", message="Session data deleted successfully.")


if __name__ == "__main__":
    app.run(debug=True)
