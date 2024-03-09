import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Leo" and password == "1234":
            return "Success."

        else:
            return "Failure."


@app.route("/file_upload", methods=["GET", "POST"])
def file_upload():
    if request.method == "GET":
        return render_template("file_upload.html")

    if request.method == "POST":
        file = request.files["file"]

        if file.content_type == "text/plain":
            return file.read().decode()

        elif file.content_type in [
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "application/vnd.ms-excel",
        ]:
            df = pd.read_excel(file)
            return df.to_html()


if __name__ == "__main__":
    app.run(debug=True)
