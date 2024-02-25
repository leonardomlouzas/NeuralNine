from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Routes
@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"

# Dynamic URLS
@app.route('/greet/<username>')
def greet(username):
    return f"<p>Hello, {username}</p>"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"<p>{num1} + {num2} = {num1 + num2}</p>"

# URL parameters
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    return f"<p>Hello, {name}</p>"

# HTTP methods
@app.route('/hello', methods=['GET', 'POST'])
def greet():
    if request.method == 'GET':
        return "<p>You made a GET request!</p>"
    elif request.method == 'POST':
        return "<p>You made a POST request!</p>"


if __name__ == "__main__":
    app.run(debug=True)
