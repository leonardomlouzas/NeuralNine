# Lesson 4

In this lesson we learn about handling static files in our application and use that knowledge to add bootstrap into it.

## Static files

Static files are files that are served directly to the client without any processing by the server. In those types of files are included images, css and javascript, for example.

First thing we need to do is create a folder to store those types of file. In the root folder of our project, create a folder called `static` which will contain those folders inside: `css`, `js`, `img`.

> Those are just the common practice names and you can change them to whatever you like.

After that, we need to make that folder available to our application. The `static_folder="static_folder_location"` will determine the location of the static files and the `static_url_path=""` will specify the URL path prefix for static files.

```python
app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
```

> if you use the common practice name and location for them, you don't need to add their keyword arguments.

### Images

Great! Now we have the foundation to use static files. Let's see it in action with an image.

Add the image of your preference to the img folder and in a html template, simply add the html `img` tag and the property `src` containing the path to the image starting from where the `static_url_path` was defined.

```html
{% extends "base.html" %} {% block title %}Index Page{% endblock %} {% block
content %}
<h1>Image</h1>
<img src="/img/image.jpg" alt="Simple image" />
{% endblock %}
```

### CSS

The same principle will apply for CSS files. For example, save a .css file in the css folder:

```css
h1 {
  color: red;
  font-size: 18pt;
}
```

And modify the base.html file to add the css call, with the `href` property referencing the path to the css file, starting from where the `static_url_path` was defined.

```html
<link rel="stylesheet" type="text/css" href="/css/style.css" />
```

### Javascript

The process for JavaScript is basically the same as the other two. Let's create a js function that shows a popup after 5 seconds after the index page loads as an example:

Create the js file and place it inside the js folder:

```js
window.onload = function () {
  setTimeout(function () {
    alert("Hello, World");
  }, 5000);
};
```

Then simply call the script tag, in your template, with the `src` property referencing the path to the js file, starting from where the `static_url_path` was defined.

```html
<script src="/js/alert.js"></script>
```

## Bootstrap

At last, let's see how to add Bootstrap to our project by downloading the compiled files and using them.

After download the zip file from the [bootstrap website](https://getbootstrap.com/docs/4.1/getting-started/download/), extract them to their respective folders in our project. CSS files into css folder, JS files into JS folder.

And combining what we did in the CSS and Javascript section, modify the base.html file to add the bootstrap call, with the `href` property referencing the path to the bootstrap css file, starting from where the `static_url_path` was defined, and the script call with the `src` property referencing the path to the bootstrap js file, starting from where the `static_url_path` was defined.

```html
<!-- Inside the head tag -->
<link rel="stylesheet" type="text/css" href="/css/bootstrap.css" />

<!-- inside the body tag-->
<script src="/js/bootstrap.js"></script>
```
