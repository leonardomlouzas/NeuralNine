from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/templates")
def index():
    return render_template("templates.html")


if __name__ == "__main__":
    app.run()
