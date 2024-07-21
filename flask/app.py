from flask import Flask, render_template, request

app = Flask(__name__) # signals that this is a web app

@app.route("/")
def index():
	name = request.args["name"]
	return render_template("index.html", placeholder=name)
