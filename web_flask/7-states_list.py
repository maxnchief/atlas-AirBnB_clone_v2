#!/usr/bin/python3
"""
This module defines a Flask web application that serves a list of states.

Routes:
    /states_list: Displays an HTML page with the states listed in alphabetical order.

Functions:
    states_list: Retrieves the list of states from the storage and renders the HTML template.
    teardown_db: Closes the storage on teardown of the Flask app context.

Usage:
    Run this script to start the Flask web application. The app will be accessible
    at http://0.0.0.0:5000/states_list.
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')