import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    '''Home page overview'''

    # get cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = cash[0]["cash"]

    # get user's portfolio
    holdings = db.execute("SELECT * FROM holdings WHERE id = ?", session["user_id"])

    # create a list of dictionries that combines all the information about each individual holding of the user
    portfolio_balance = 0
    portfolio = []
    for holding in holdings:
        quote = lookup(holding["symbol"])
        stock = {"name": quote["name"], "symbol": holding["symbol"], "quantity": holding["quantity"],
                 "current_price": quote["price"], "holding_value": (quote["price"]*holding["quantity"])}
        portfolio.append(stock)
        portfolio_balance += quote["price"]*holding["quantity"]

    return render_template("index.html", cash=cash, portfolio=portfolio, portfolio_balance=portfolio_balance)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    '''Buy a stock'''

    if request.method == "POST":

        # validate symbol
        quote = lookup(request.form.get("symbol").upper())
        if not quote:
            return apology("stock symbol doesn't exist", 400)

        # validate quantity
        try:
            quantity = int(request.form.get("shares"))
        except ValueError:
            return apology("invalid quantity", 400)
        if quantity <= 0:
            return apology("invalid quantity", 400)

        # validate if user can afford the purchase
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_cash = user_cash[0]["cash"]
        total_cost = quote["price"] * quantity
        if not int(total_cost) <= user_cash:
            return apology("not enough cash for the purchase", 400)

        # process the transaction
        buy = "B"
        db.execute(
            "INSERT INTO transactions (id, name, symbol, quantity, price, side) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"], quote["name"], request.form.get(
                "symbol").upper(), quantity, quote["price"], buy
        )

        # update user's cash
        db.execute(
            "UPDATE users SET cash = :new_total WHERE id = :user_id",
            new_total=user_cash-total_cost, user_id=session["user_id"]
        )

        # update user's holdings
        stock = db.execute(
            "SELECT quantity FROM holdings WHERE id = :user_id AND symbol = :symbol",
            user_id=session["user_id"], symbol=quote["symbol"]
        )

        if stock:
            db.execute(
                "UPDATE holdings SET quantity = :new_quantity WHERE symbol = :symbol AND id = :user_id",
                new_quantity=stock[0]["quantity"]+quantity, symbol=quote["symbol"], user_id=session["user_id"]
            )
        else:
            db.execute(
                "INSERT INTO holdings (id, symbol, quantity) VALUES (?, ?, ?)",
                session["user_id"], quote["symbol"], quantity
            )

        # render success message
        price = quote["price"]
        total_cost = int(quantity)*price
        flash(f"Bought {quantity} shares of {quote["symbol"]} for {total_cost}!")

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    transactions = db.execute("SELECT * FROM transactions")
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("stock symbol doesn't exist", 400)
        return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # check if not blank
        if not request.form.get("username"):
            return apology("must provide username", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        # check if passwords match
        elif password != confirmation:
            return apology("passwords don't match", 400)

        # check if username isn't taken
        name_check = db.execute(
            "SELECT * FROM users WHERE username = ?", username)

        if len(name_check) == 1:
            return apology("username is already taken", 400)

        # add the user to the databse
        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)",
            username, generate_password_hash(password))

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    ''' Sell a stock'''

    if request.method == "POST":

        # validate symbol
        quote = lookup(request.form.get("symbol").upper())
        if not quote:
            return apology("stock symbol doesn't exist", 403)

        # validate quantity
        try:
            quantity = int(request.form.get("quantity"))
        except ValueError:
            return apology("invalid quantity", 403)
        if quantity <= 0:
            return apology("invalid quantity", 403)

        # get the number of shares user owns
        available_quantity = db.execute(
            "SELECT quantity FROM holdings WHERE id = :user_id AND symbol = :symbol",
            user_id=session["user_id"], symbol=quote["symbol"])

        # validate if user actually owns the shares he wants to sell
        if not available_quantity:
            return apology("you don't own any shares of this stock", 403)
        if available_quantity[0]["quantity"] < quantity:
            return apology("you can't sell more shares than you own", 403)

        # process the transaction
        sell = "S"
        db.execute(
            "INSERT INTO transactions (id, name, symbol, quantity, price, side) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"], quote["name"], request.form.get(
                "symbol"), quantity, quote["price"], sell
        )

        # update user's cash
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        user_cash = user_cash[0]["cash"]
        total_cost = quote["price"]*quantity

        db.execute(
            "UPDATE users SET cash = :new_total WHERE id = :user_id",
            new_total=user_cash+total_cost, user_id=session["user_id"]
        )

        # update user's holdings
        db.execute(
            "UPDATE holdings SET quantity = :new_quantity WHERE symbol = :symbol AND id =:user_id",
            new_quantity=available_quantity[0]["quantity"]-quantity, symbol=quote["symbol"], user_id=session["user_id"]
        )

        return redirect("/")

    else:
        return render_template("sell.html")


@app.route("/addcash", methods=["GET", "POST"])
@login_required
def addcash():
    '''Add cash'''

    if request.method == "POST":
        # validate input
        try:
            amount = float(request.form.get("amount"))
            amount = round(amount, 2)
        except ValueError:
            return apology("invalid amount", 403)

        if amount <= 0:
            return apology("amount must be higher than $0", 403)

        # update user's cash
        current = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        current = current[0]["cash"]

        new_total = round(current+amount, 2)
        db.execute(
            "UPDATE users SET cash = :new_total WHERE id = :user_id",
            new_total=new_total, user_id=session["user_id"]
        )

        return render_template("addcash.html", amount=amount, new_total=new_total)

    else:
        return render_template("addcash.html")
