#!/usr/bin/python3
"""
This module sets up a simple Flask web application with a single route.

Routes:
    /: Returns the string "Hello HBNB!" when accessed.

Usage:
    Run this script to start the Flask web application. The application will be accessible
    at http://0.0.0.0:5000/.

Example:
    $ python3 0-hello_route.py

Dependencies:
    Flask: A micro web framework for Python.

Functions:
    hello_hbnb(): Returns a greeting string "Hello HBNB!" when the root URL is accessed.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)