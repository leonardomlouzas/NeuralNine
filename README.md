# Lesson 2

In this lesson we learn about routes, URL parameters/path, dynamic URLs and different types of requests.

## Routes

In Flask, we can create as many endpoint as we want. For that, simply create a function with the `@app.route('/$endpoint_name')` decorator. The name of the function doesn't need to match the name of the endpoint.

```python
@app.route('/hello')
def new_route():
    return "<p>Hello, World!</p>"
```

## Dynamic URLs

We can also create dynamic URLs.

Using variables in the URL itself:

```python
@app.route('/greet/<username>')
def greet(username):
    return f"<p>Hello, {username}</p>"
```

Variables are treated as strings by default. We can change that by specifying the type of the variables on the url:

```python
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"<p>{num1} + {num2} = {num1 + num2}</p>"
```

## URL parameters

Using url parameters is a little different than using variables. Before anything, we have to import `request` from flask, so we get access to the whole request, including the parameters.

```python
from flask import request
```

Now we can access the parameters using `request.args`. and use them as we want inside our route function:

```python
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    return f"<p>Hello, {name}</p>"
```

## HTTP methods

By default, Flask functions only supports GET requests. But we can easily change that by adding a new argument on the function decorator of our route. For example, if we want to support both GET and POST requests, we can do this:

```python
@app.route('/greet', methods=['GET', 'POST'])
```

With that we can change our function behavior depending on the request method. But before anything, we have to import `request` from flask, so we get access to the whole request, including the parameters.

```python
from flask import request
```

Finally, we can check the request method with `request.method` and act accordingly:

```python
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "<p>You made a GET request!</p>"
    elif request.method == 'POST':
        return "<p>You made a POST request!</p>"
```

## Status Codes

By default, the status code of the response is 200, which means "OK". But there are different ways to change that status code.

The easiest way would be by specifying the status code as the second parameter of the `return` function:

```python
@app.route('/status_code_easy')
def easy():
    return "<p>easy method</p>", 201
```

A more refined way of doing it would be by creating the response object and adding the status code in there. For that, we need to import `make_response` from flask:

```python
from flask import make_response
```

Now we can create the response object and add the status code:

```python
@app.route('/status_code_complex')
def complex():
    response = make_response("<p>complex method</p>")
    response.status_code = 201
    return response
```
