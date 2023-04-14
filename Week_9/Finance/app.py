import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
# raise RuntimeError("API_KEY not set")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "POST":
        user_id = session["user_id"]

        # If the buy button is hit
        if request.form["button"][0] == "B":

            # Get symbol for the buy
            symbol = request.form.get("button")
            symbol = symbol.split(" ")[1]

            # Get the amount of shares
            shares = int(request.form.get("shares"))

            stock = lookup(symbol)

            name = stock["name"]
            price = stock["price"]
            rel_sym = stock["symbol"]

            # Calculate the total price of offering
            tot_price = shares*price

            # Check total price does no exceed cash amount
            cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

            if cash < tot_price:
                return apology("Not enough cash for that!")

            # If there is enough cash then complete the transaction
            else:
                db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - tot_price, user_id)
                db.execute("INSERT INTO transactions (user_id, symbol, name, price, type, number, recent_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           user_id, rel_sym, name, price, "buy", shares, price)
                return redirect("/")

        if request.form["button"][0] == "S":
            # Get symbol for the sale
            symbol = request.form.get("button")
            symbol = symbol.split(" ")[1]

            # Get the amount of shares
            shares = int(request.form.get("shares"))

            # Get total holdings
            tot_holdings = db.execute("SELECT SUM(number)as totnum FROM transactions WHERE user_id=? GROUP BY symbol", user_id)[
                0]["totnum"]

            if shares > tot_holdings:
                return apology("You do not hold enough shares for this sale")

            # Most up to date info for sale
            sold = lookup(symbol)
            rel_sym = sold["symbol"]
            name = sold["name"]
            price = sold["price"]

            tot_sale = price*shares
            cash = db.execute("SELECT cash FROM users WHERE id= ?", user_id)[0]["cash"]

            # Change transaction table
            db.execute("INSERT INTO transactions (user_id, symbol, name, price, type, number, recent_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       user_id, rel_sym, name, price, "sell", -shares, -price)
            # Change cash in user table
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + tot_sale, user_id)
            return redirect("/")

    else:
        # Set user ID
        user_id = session["user_id"]

        # Create dictionry for holdings grouped by symbol and with number summed
        stocks = db.execute(
            "SELECT symbol, name, recent_price, SUM(number) AS totnum FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)

        # Create dictionry for cash held by user
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # Reset total holdings figure before for loop
        tot_hold = 0

        # Loop through the stocks check most recent price and add to recent_price column of stocks for give stock
        for stock in stocks:
            check = lookup(stock["symbol"])
            rec_price = check["price"]
            symbol = check["symbol"]
            db.execute("UPDATE transactions SET recent_price = ? WHERE symbol = ?", rec_price, symbol)
            tot_hold += stock["totnum"]*rec_price

        return render_template("index.html", stocks=stocks, usd=usd, cash=cash, tot_hold=tot_hold)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Set user_id
        user_id = session["user_id"]

        # Get symbol and check exists
        symbol = request.form.get("symbol")
        symbol = symbol.upper()
        if not symbol:
            return apology("You must enter a symbol")

        # Use symbol in lookup function and check if valid
        stock = lookup(symbol)
        if not stock:
            return apology("You must enter a valid symbol")
        name = stock["name"]
        price = stock["price"]
        rel_sym = stock["symbol"]

        # Get amount of shares from form and check it is positive integer
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Must be whole number")

        if shares <= 0:
            return apology("Must be a positive number")

        # Calculate the total price of offering
        tot_price = shares*price

        # Check total price does no exceed cash amount
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        if cash < tot_price:
            return apology("Not enough cash for that!")

        # If there is enough cash then complete the transaction
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - tot_price, user_id)
            db.execute("INSERT INTO transactions (user_id, symbol, name, price, type, number, recent_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       user_id, rel_sym, name, price, "buy", shares, price)
            return redirect("/")
    else:
        return render_template("/buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Set user ID
    user_id = session["user_id"]

    # Create dictionry for holdings grouped by symbol and with number summed
    transactions = db.execute("SELECT symbol, number, price, time FROM transactions WHERE user_id = ?", user_id)

    return render_template("history.html", transactions=transactions, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

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
    if request.method == "POST":

        # Get the symbol from the form
        symbol = request.form.get("symbol")
        symbol = symbol.upper()
        if not symbol:
            return apology("Must provide symbol")

        # Use lookup function to get a quote
        quote = lookup(symbol)

        # If not a real symbol deliver apology
        if not quote:
            return apology("Invalid symbol")

        # Return the quoted template with active quotes
        return render_template("/quoted.html", quote=quote, usd=usd)
    else:
        return render_template("/quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Get user name and passwords
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # check if user name and passwords are present
        if not username:
            return apology("Must input username")

        if not password:
            return apology("Must input password")

        if not confirmation:
            return apology("Must re-input password")

        # Check if passwords match
        if password != confirmation:
            return apology("Your passwords did not match")

        # Check if username is unique
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
            return redirect("/")
        except:
            return apology("Username already taken")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    if request.method == "POST":
        # Get symbol
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Missing symbol")

        # Get amount of shares from form and check it is positive integer
        shares = int(request.form.get("shares"))
        if shares <= 0:
            return apology("Must be a positive number")

        # Get total holdings
        tot_holdings = db.execute("SELECT SUM(number)as totnum FROM transactions WHERE user_id=? GROUP BY symbol", user_id)[
            0]["totnum"]

        # Check if user has the amount of shares to sell
        if shares > tot_holdings:
            return apology("You do not hold enough shares for this sale")

        # Get most uptodate info for sale
        sold = lookup(symbol)
        rel_sym = sold["symbol"]
        name = sold["name"]
        price = sold["price"]

        # Calculate total price
        tot_sale = price*shares

        # Get amount of cash
        cash = db.execute("SELECT cash FROM users WHERE id= ?", user_id)[0]["cash"]

        # Change transaction table
        db.execute("INSERT INTO transactions (user_id, symbol, name, price, type, number, recent_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   user_id, rel_sym, name, price, "sell", -shares, -price)
        # Change cash in user table
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + tot_sale, user_id)

        return redirect("/")

    else:
        # Get symbols for list
        symbols = db.execute("SELECT symbol, SUM(number) as totnum FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)

        return render_template("/sell.html", symbols=symbols)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)