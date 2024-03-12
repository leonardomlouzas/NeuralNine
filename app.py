import os
import uuid

import pandas as pd
from flask import (
    Flask,
    Response,
    jsonify,
    render_template,
    request,
    send_from_directory,
)

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


@app.route("/convert_to_csv", methods=["GET", "POST"])
def convert_to_csv():
    if request.method == "GET":
        return render_template("convert_to_csv.html")

    elif request.method == "POST":
        file = request.files["file"]

        df = pd.read_excel(file)

        response = Response(
            df.to_csv(),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=result.csv"},
        )

        return response


@app.route("/convert_to_csv_proper", methods=["GET", "POST"])
def convert_to_csv_proper():
    if request.method == "GET":
        return render_template("convert_to_csv_proper.html")

    elif request.method == "POST":
        file = request.files["file"]

        df = pd.read_excel(file)

        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        filename = f"{uuid.uuid4()}.csv"

        df.to_csv(os.path.join("downloads", filename))

        return render_template("download.html", filename=filename)


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory("downloads", filename, download_name="result.csv")


@app.route("/javascript", methods=["GET", "POST"])
def javascript():
    if request.method == "GET":
        return render_template("js.html")

    elif request.method == "POST":
        greeting = request.json.get("greeting")
        name = request.json.get("name")

        with open("./files/file.txt", "w") as f:
            f.write(f"{greeting}, {name}")

        return jsonify({"message": "Successfully written"})


if __name__ == "__main__":
    app.run(debug=True)
