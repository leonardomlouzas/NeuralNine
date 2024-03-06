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


@app.route("/conditionals")
def conditionals():
    user_name = "Leonardo"
    return render_template("conditionals.html", name=user_name)


@app.route("/allofit")
def allofit():
    colors = ["red", "black", "red", "black"]
    return render_template("allofit.html", items=colors)


@app.route("/extending")
def extending():
    return render_template("extending.html")


@app.route("/filters")
def filters():
    user_name = "Leonardo"
    return render_template("filters.html", name=user_name)


@app.route("/custom_filters")
def custom_filters():
    user_name = "Leonardo"
    return render_template("custom_filters.html", name=user_name)


@app.template_filter("reverse_string")
def reverse_string(s):
    return s[::-1]


@app.template_filter("repeat")
def repeat(s, times=2):
    return s * times


@app.template_filter("alternate_case")
def alternate_case(s):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


if __name__ == "__main__":
    app.run()
