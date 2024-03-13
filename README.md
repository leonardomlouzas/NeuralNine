# Lesson 6

In this lesson we learn about how to handle Sessions and Cookies.
Sessions and cookies are both used to store information about the client, the difference between them is where the information is stored. Sessions are stored on the server, while cookies are stored on the client's computer.
We will also see about message flashing, which is a way to display messages to the user.

## Sessions

Sessions usually contain sensitive information about the client that the server must be able to trust. That means the client can't access nor modify this information.

To be able to use sessions in our application we must import `session` from flask:

```python
from flask import Flask, render_template, session
```

And define a secret key for our app. In practice the secret key should be well constructed and well stored for security, for this lesson we are gonna use a simple string:

```python
app.secret_key = "Secret Key"
```

### Create

Let's create an endpoint and use it to see how to set our session:

```python
@app.route("/session_set")
def session_set():
  session["name"] = "Leo"
  session["message"] = "Hello, World!"

  return render_template("index.html", message="Session data set successfully.")
```

As you can see, we used the `session` to add the `name` and `message`. You can check in the cookies tab of the Inspect Elements window of your browser to see the session set.

### Access

Let's create an endpoint and use it to see how to get our session:

```python
@app.route("/session_get")
def session_get():
  name = session.get("username")
  message = session.get("message")

  formatted_message = f"{name}. {message}." if name and message else "Session not valid."

  return render_template("index.html", message=formatted_message)
```

To access the information stored in the session, we just need to use the `session` we imported from flask and retrieve it as a dictionary.

### Delete

Let's create an endpoint and use it to see how to delete our session:

```python
@app.route("/session_delete")
def session_delete():
  # This delete only one info in the session
  session.pop("name")

  # This clear all info in the session
  session.clear()

  return render_template("index.html", message="Session data deleted successfully.")
```

And that's how we delete one or all the session information stored.

## Cookies

Cookies usually do not contain sensitive information about the client and the client can easily modify it through the Inspect Element.

To be able to use cookies in our application we must import `make_response` and `request` from flask. First will be used to instruct the client browser to save/delete the cookies and the second to access the cookies:

```python
from flask import Flask, render_template, session, make_response, request
```

### Create

Let's create an endpoint and use it to see how to set our session:

```python
@app.route("/cookie_set")
def cookie_set():
  response = make_response(render_template("index.html", message="Cookies set successfully."))
  response.set_cookie("cookie_name", "cookie_value")

  return response
```

After creating the response using make_response, we use the `set_cookie` to add a new cookie.

### Access

Let's create an endpoint and use it to see how to get our cookies:

```python
@app.route("/cookies_get")
def cookie_get():
  cookie_value = request.cookies.get("cookie_name")
  message = cookie_value if cookie_value else "No cookie with this name"
  return render_template("index.html", message=message)
```

To access the information stored in the cookies, we just need to use the `request` we imported from flask and retrieve it as a dictionary.

### Delete

Let's create an endpoint and use it to see how to delete our session:

```python
@app.route("/cookies_delete")
def cookie_delete():
  response = make_response(render_template("index.html", message="Cookies deleted successfully."))
  response.set_cookie("cookie_name", expires=0)

  return response
```

To delete the cookie, we use the `set_cookie` again but this time with the `expires=0` to make that cookie expire immediately.

## Message flashing

Message flashing is a way to display messages to the user. It is useful for displaying messages that need to be displayed only once, such as error messages or success messages.

For this example we are going to make it very basic and not stylized at all. It will be a simple unordered list containing the messages.

For that, let's modify the template of where we wanna display the messages:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %} Default Title {% endblock %}</title>
  </head>

  <body>
    {% with messages = get_flashed_messages() %} {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
    </ul>
    {% endif %} {% endwith %} {% block content %} Default Content {% endblock %}
  </body>
</html>
```

Let's import the flash function from flask to our project:

```python
from flask import Flask, make_response, render_template, request, session, flash
```

And now let's create a login html template for this example where the login status will be displayed after a login attempt:

```html
{% extends "base.html" %} {% block title %}Login Page{% endblock %} {% block
content %}
<h1>Login</h1>
<form action="{{ url_for('login') }}" method="POST">
  <input type="text" name="username" placeholder="Username" />
  <input type="text" name="password" placeholder="Password" />
  <input type="submit" value="Login" />
</form>
{% endblock %}
```

And the route that will render the login and also flash the message:

```python
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
```
