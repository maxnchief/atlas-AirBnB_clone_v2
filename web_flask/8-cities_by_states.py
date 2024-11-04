#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

"""
This module defines a Flask web application that displays a list of cities by states.

Routes:
    /cities_by_states: Displays a HTML page with a list of all State objects and their related City objects.

Functions:
    cities_by_states(): Retrieves all State objects from storage, sorts them by name, and renders them in a template.
    teardown_db(exception): Closes the storage session after each request.

Usage:
    Run this script to start the Flask web application. The application listens on all public IPs on port 5000.
"""


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
