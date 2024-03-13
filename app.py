from flask import Flask, flash, make_response, render_template, request, session

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


@app.route("/cookie_set")
def cookie_set():
    response = make_response(
        render_template("index.html", message="Cookies set successfully.")
    )
    response.set_cookie("cookie_name", "cookie_value")

    return response


@app.route("/cookies_get")
def cookie_get():
    cookie_value = request.cookies.get("cookie_name")
    message = cookie_value if cookie_value else "No cookie with this name"
    return render_template("index.html", message=message)


@app.route("/cookies_delete")
def cookie_delete():
    response = make_response(
        render_template("index.html", message="Cookies deleted successfully.")
    )
    response.set_cookie("cookie_name", expires=0)

    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "leo" and password == "1234":
            flash_message = "Login Successfully."

        else:
            flash_message = "Login Failed."

        flash(flash_message)
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
