# Lesson 3

In this lesson we learn about HTML templates, the basic of Jinja2 with Flask (variables, functions, conditionals, filters) and also how to use dynamic end-points and redirects.

## HTML templates

Up to this point we only returned strings or loose html code to the endpoint. Now we will learn how to use HTML templates.

First of all, create a folder which will hold all the templates. The common practice is to create a folder, on the root directory, called "templates".

Then go to the `app.py` and edit the app creation to add the keyword argument `template_folder` which contains the directory where the "templates" folder is located.

```python
app = Flask(__name__, template_folder="templates")
```

> if you use the common practice name and location, you don't need to add the keyword argument

Let's create a basic html file in the "templates" folder for the home page.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Flask App</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

Now that we have a folder for the templates and a basic template, let's use it on our app. For that, we need to import the `render_template` function from `flask`.

```python
from flask import Flask, render_template
```

And that's how we use it:

```python
@app.route('/')
def index():
    return render_template('index.html')
```

## Jinja2

Jinja2 is a templating language that help us with using programming logic in our html templates.

### Variables

We can pass and use variables from our python code in our html templates by passing them as arguments to the `render_template` function. For example:

```python
@app.route('/')
def variables():
    user_name = "Leonardo"
    return render_template("variables.html", name=user_name)
```

> `name` will be the variable name used in the html template.

And in the html template we use the syntax `{{ variable_name }}` to use the variable. For example:

```html
<h1>Hello, {{ name }}</h1>
```

### Loops

We can use for loops in our html templates by passing a list as an argument in the `render_template` function and using the `{% for %}` and `{% endfor %}` syntax. For example:

```html
<ul>
  {% for item in items %}
  <li>{{ item }}</li>
  {% endfor %}
</ul>
```

### Conditionals

We can use conditionals in our html templates by using the `{% if %}` and `{% else %}` syntax. For example:

```html
{% if name == "Leonardo" %}
<h1>Hello, {{ name }}</h1>
{% else %}
<h1>Hello, stranger</h1>
{% endif %}
```

**Example of them together**

We can easily put them together to make a more concise code. Like this:

```html
<ul>
    {% for item in items %}
        <li {% if item == "red" %} style = "color: red" {% endif %}> {{ item }} </li>
    {% endfor %}
</ul>
```

## Extending templates

To help us with dealing with repeating common code between our templates, we can extend templates and use them in other templates. Let's see how it works.

First we need to create a base template and use the `{% block %}` and `{% endblock %}` syntax to signal where we want to insert the other templates. For example:

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
    {% block content %} Default Content {% endblock %}
  </body>
</html>
```

> Notice how we can add default values in case we don't pass any template.

Now we can create a template that extends the base template using the `{% extends %}` syntax. For example:

```html
{% extends "base.html" %} {% block title %}Extending Templates{% endblock %} {%
block content %}
<h1>This was extended</h1>
{% endblock %}
```

### Basic filters

In Jinja2 it's not really possible to use methods on the variables we pass to the templates. To circumvent this, we use filters.

In the templates, instead of using `.upper()` for example, we use `{{ variable|upper }}`, piping the variable to the filters we want to use.

> [Here](https://tedboy.github.io/jinja2/templ14.html) is a list of built-in filters.

For example:

```html
<h1>Hello, {{ name|upper }}</h1>
<h1>Hello, {{ name|lower }}</h1>
<h1>Hello, {{ name|title }}</h1>
<h1>Hello, {{ name|capitalize }}</h1>
<h1>Hello, {{ name|length }}</h1>
<h1>Hello, {{ name|replace("o", "a") }}</h1>
<h1>Hello, {{ name|replace("o", "a")|upper }}</h1>
```

### Custom filters

If we need a filter that is not present in the built-in list, we can create our own. For that, lets create a function that will be used as our filter. Add the decorator `@app.template_filter("filter_name")` on top to make it usable as a filter in the templates. For example:

```python
@app.template_filter("reverse_string")
def reverse_string(s):
  return s[::-1]
```

Now you can go to the template and use it like this:

```html
{{ variable|reverse_string }}
```

## Dynamic End-points

Sometimes we need to change the endpoint route on our application, and if we have it statically defined in our code/templates, we would have to change it everywhere. But flask help us with that by using the `url_for("function_name")` function. For example:

```html
<a href="{{ url_for('index') }}">Home</a>
```

> It can also be used in the python code, more on that later.

## Redirects

If we want to redirect the user to another endpoint through the python code, we can do so by using the `redirect` function. For that, we need to import it:

```python
from flask import Flask, render_template, redirect, url_for
```

> Notice that we also need to import the `url_for` function.

Then we can use it like this:

```python
@app.route('/redirect')
def redirect_page():
    return redirect(url_for('index'))
```
