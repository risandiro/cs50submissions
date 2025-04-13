from flask import Flask, render_template, request

# initialization of flask, treat this file as a web application
app = Flask(__name__)


''' defining a route for this application, whenever a user visits slash on this
application, what should happen is this function index should get called. Index
function uses render_template to return a index.html back to the user '''
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name = name)
