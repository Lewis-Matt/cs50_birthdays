import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    # The user submitted something via form
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        # Get form data
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Insert into db
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)",
        name,
        month,
        day
        )

        # Back to homepage
        return redirect("/")

    # The user is just getting the website
    else:
        # TODO: Display the entries in the database on index.html
        # Query db to get access to all the bdays and pass into index - bdays saved into list called birthdays
        birthdays = db.execute("SELECT * FROM birthdays")
        # Pass to template variable named birthdays that is equal to the birthdays list
        return render_template("index.html", birthdays=birthdays)

# REMEMBER, use "/ $ flask run" to run the application
