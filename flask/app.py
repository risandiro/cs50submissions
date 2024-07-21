from flask import Flask, render_template, request

app = Flask(__name__) # signals that this is a web app

@app.route("/")
def index():
	return render_template("index.html")
