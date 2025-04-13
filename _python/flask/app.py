from flask import Flask, render_template, request

# treat this file as a web application
app = Flask(__name__)

# defining a route for this application, whenever
@app.route("/")
def index():
    return "hello, world"
