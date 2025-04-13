from flask import Flask, render_template, request

# treat this file as a web application
app = Flask(__name__)

# defining a route for this application, whenever a human visits slash on this
# application, what should happen is this function index should get called
@app.route("/")
def index():
    return "hello, world"
