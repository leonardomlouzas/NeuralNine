from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/templates")
def templates():
    return render_template("templates.html")


@app.route("/variables")
def variables():
    user_name = "Leonardo"
    return render_template("variables.html", name=user_name)


@app.route("/loops")
def loops():
    fruits = ["apple", "banana", "cherry"]
    return render_template("loops.html", items=fruits)


if __name__ == "__main__":
    app.run()
