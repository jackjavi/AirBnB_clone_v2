#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Display 'HBNB'
    /c/<text>: Displays 'C' followed by the value of <text>
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of <text>."""
    return 'C' + text.replace('_', ' ')

@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays 'Python', followed by the value of the text variable
       (replace underscore _ symbols with a space )

    The default value of text is “is cool”
    """
    text = text.replace("_", " ")
    return "python {}".format(text)

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    if (type(int(n) == int)):
        return "{} is a number".format(n)

@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer."""
    if (type(int(n) == int)):
        return render_template("5-number.html", n=n)
 




if __name__ == '__main__':
    app.run(host='0.0.0.0')
