from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# This is a copy-paste for getting the sessions to work
''' this ensures the session is deleten when you quit the browser '''
app.config["SESSION_PERMANENT"] = False
''' this ensures the contents of the session are stored
in the server's files, not the cookie istelf for privacy's sake '''
app.config["SESSION_TYPE"] = "filesystem"
''' this activates the use of sessions in this app '''
Session(app)

@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))

@app.route("/login",  methods=["GET", "POST"])
def login():
    # if user submitted their name via POST
    if request.method == "POST":
        # store their namein the session
        session["name"] = request.form.get("name")
        # redirect user back to the homepage
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    # clears the session
    session.clear()
    return redirect("/")
