from flask import Flask, render_template, request

# initialization of flask, treat this file as a web application
app = Flask(__name__)


''' defining a route for this application, whenever a user visits slash on this
application, what should happen is this function index should get called. Index
function uses render_template to return a index.html back to the user '''
@app.route("/")
def index():
    name = request.args[name]
    return render_template("index.html", placeholder=name)
