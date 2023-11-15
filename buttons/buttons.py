""" A set of python functions for the index page.

A set of functions to manipulate the DOM and add some interactivity
to the home page."""

# imports
from pyodide.ffi import create_proxy
from js import document


# do something
@create_proxy
def do_something(*args):
    """does something (up to the developer playing with this)"""
    # TODO: come up with some python code to manipulate the DOM using msg
    # for loop? something else?
    # a sample has been provided to get you started
    msg = "<p><strong>Hey</strong>! Just checking</p>"
    document.getElementById("display-canvas").innerHTML = msg


document.getElementById("load_btn").addEventListener("click", do_something)

# Call function
