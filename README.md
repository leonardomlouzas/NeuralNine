# Lesson 4

In this lesson we learn about forms, file upload and download, and javascript requests.

## Basic forms

Let's talk about forms. We can retrieve information about a submitted form by accessing the form object of the request sent and use it the way we want, let's handle a login to use forms as example:

First, let's create a route that with GET and POST methods, one to display the form when we access the endpoint and the other to submit the form and log in.

```python
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
      return "Success"

    else:
      return "Failure"


if __name__ == "__main__":
  app.run(debug=True)
```

> We are making a simple string comparison to validate the log in just for the simplicity sake.

Create the `index.html` template:

```html
{% extends "base.html" %} {% block title %}Index Page{% endblock %} {% block
content %}
<h1>1</h1>
<form method="POST" action="{{url_for('index')}}">
  <input type="text" name="username" placeholder="Username" /><br />
  <input type="password" name="password" placeholder="Password" /><br />
  <input type="submit" value="Login" />
</form>
{% endblock %}
```

Pay attention that the `name` defined on the each input of the form in the template is what we use on the `request.form.get(<name>)` python code.

### File upload

What if we want to upload a file through the forms? Easy. Let's see how:

> For this example, we are going to use simple text files and spreadsheets files, so we must install (`pip install pandas`) and import (`import pandas as pd`) pandas to handle them.

The python code would look like this:

```python
@app.route("/file_upload", methods=["GET", "POST"])
def file_upload():
  if request.method == "GET":
    return render_template("file_upload.html")

  elif request.method == "POST":
    file = request.files["file"]

    # If the file is a simple .txt, the endpoint will read and return it as a string.
    if file.content_type == "text/plain":
      return file.read().decode()

    # If the file is a spreadsheet, it will use pandas to read the file and return it as an html.
    elif file.content_type in [
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "application/vnd.ms-excel",
    ]:
      df = pd.read_excel(file)
      return df.to_html()
```

The html template should look like this:

```html
{% extends "base.html" %} {% block title %} File Upload{% endblock %} {% block
content %}
<h1>2</h1>
<form
  method="POST"
  action="{{url_for('file_upload')}}"
  enctype="multipart/form-data"
>
  <input
    type="file"
    name="file"
    accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel, text/plain"
    required="required"
  />
  <input type="submit" value="upload file" />
</form>
{% endblock %}
```

As you can see, this form contain a few new things. the `enctype` attribute is used to indicate that the form will be submitting binary data, such as files. The `accept` attribute is used to specify the types of files that the server will accept when the form is submitted.

### Basic file download

Now that we have a file upload, let's see an easy way to download it from the server. For this example let's create a route that will receive a spreadsheet from the form, convert it to csv and download it on the user machine automatically.

Add the `Response` object into the import list of flask:

```python
from flask import Flask, Response, render_template, request
```

Create a route to handle the `GET` and `POST`:

```python
@app.route("/convert_to_csv")
def convert_to_csv():
  if request.method == "GET":
    return render_template("convert_to_csv.html")

  elif request.method == "POST":
    file = request.files["file"]

    df = pd.read_excel(file)

    # Creates a new Response object containing the converted file and the necessary properties to make it valid.
    response = Response(
      df.to_csv(),
      mimetype="text/csv",
      headers={"Content-Disposition": "attachment; filename=result.csv"},
    )

    return response
```

The html template looks like this:

```html
{% extends "base.html" %} {% block title %}File Convert{% endblock %} {% block
content %}
<h1>3</h1>
<form
  method="POST"
  action="{{url_for('convert_to_csv')}}"
  enctype="multipart/form-data"
>
  <input
    type="file"
    name="file"
    accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
    required="required"
  />
  <input type="submit" value="upload file" />
</form>
{% endblock %}
```

### Proper file download

Now that we have an understanding of how a file can be download, let's create proper endpoints which will take the file, store it in our server and return a download button to the user.

For that, let's import `os` to define where the files are going to be saved, `uuid` to name the files and prevent repeated names, and the `send_from_directory` function from flask:

```python
import os
import uuid
from flask import Flask, Response, render_template, request, send_from_directory
```

The route will look like this:

```python
@app.route("/convert_to_csv_proper", methods=["GET", "POST"])
def convert_to_csv_proper():
  if request.method == "GET":
    return render_template("convert_to_csv_proper.html")

  elif request.method == "POST":
    file = request.files["file"]

    df = pd.read_excel(file)

    # Creates the downloads folder if it doesn't exist
    if not os.path.exists("downloads"):
      os.makedirs("downloads")

    filename = f"{uuid.uuid4()}.csv"

    df.to_csv(os.path.join("downloads", filename))

    return render_template("download.html", filename=filename)


@app.route("/download<filename>")
def download(filename):
  return send_from_directory("downloads", filename, download_name="result.csv")
```

The `convert_to_csv_proper.html` template will look like this:

```html
{% extends "base.html" %} {% block title %}File Upload{% endblock %} {% block
content %}
<h1>4</h1>
<form
  method="POST"
  action="{{url_for('convert_to_csv_proper')}}"
  enctype="multipart/form-data"
>
  <input
    type="file"
    name="file"
    accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
    required="required"
  />
  <input type="submit" value="upload file" />
</form>
```

And the `download.html` template will look like this:

```html
{% extends "base.html" %} {% block title %}Download{% endblock %} {% block
content %}
<h1>Download</h1>

<a href="{{url_for('download', filename=filename)}}">Download file</a>
{% endblock %}
```

## JavaScript requests

Now let's check how we can send, access and save information through javascript and json.

First, add the `jsonify` to the flask import list

```python
from flask import Flask, Response, jsonify, render_template, request, send_from_directory
```

Create the route:

```python
@app.route("/javascript", methods=["GET", "POST"])
def javascript():
  if request.method == "GET":
    return render_template("js.html")

  elif request.method == "POST":
    # Retrieves the variables from the request body sent in json format.
    greeting = request.json.get("greeting")
    name = request.json.get("name")

    # Writes it down in a file in the server
    with open("./files/file.txt", "w") as f:
      f.write(f"{greeting}, {name}")

    # returns a json to the user
    return jsonify({"message": "Success."})
```

The template will be a bit bigger because the use of vanilla JavaScript and will look like this:

```html
{% extends "base.html" %} {% block title %}JavaScript{% endblock %} {% block
content %}
<h1>5</h1>
<button id="post_button">Send Post Request</button>
<textarea type="text" id="greeting" placeholder="greeting"></textarea>
<textarea type="text" id="name" placeholder="name"></textarea>

<script type="text/javascript">
  const  postButton = document.getElementById("post_button");

  postButton.addEventListener("click", () => {
    const greeting = document.getElementById("greeting").value;
    const name = document.getElementById("name").value;
    const jsonData = {name: name, greeting: greeting};

    fetch("{{ url_for("javascript") }}", {
      method: "POST",
      headers: {
        "Content-Type": "application/json; charset=utf-8"
      },

      body: JSON.stringify(jsonData)
    })
      .then(response => response.json())
      .then(data => console.log("Success:", data))
      .catch((error) => {
        console.error("Error:", error)
      });
  });
</script>
{% endblock %}
```
