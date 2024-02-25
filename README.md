# Lesson 1

In this lesson we learn how to create and run a Flask project, going through the all the steps needed from start to finish.
We will create a virtual environment, install Flask, create a Flask project, and run the Flask project.

## Step 1: Virtual Environment

First thing we must do to work with Flask is create and activate a virtual environment to separate our project libraries from our system libraries.

1. Run `python -m venv .venv` to create a virtual environment.
2. Run `source .venv/bin/activate` to activate the virtual environment.

## Step 2: Install Flask

Now that we have a virtual environment, we can install Flask.

1. Run `pip install Flask` to install Flask.

## Step 3: Create a Flask Project

After that we can create our Flask project.

1. In the root directory of our project, create a file called `app.py`.
2. Inside the `app.py` file, insert this:

   ```
   from flask import Flask


   app = Flask(__name__)

   @app.route("/")
   def hello_world():
       return "<p>Hello, World!</p>"


   if __name__ == "__main__":
       app.run(debug=True)

   ```

## Step 4: Run the Flask Project

After that, we successfully have created a minimal Flask project. Let's see if we can run it.

1. Run `python app.py` to run the Flask project.
2. Open your browser and go to `http://127.0.0.1:5000/` to see the result
