#!/usr/bin/env python3

from flask import Flask
from flask import redirect, url_for, request, render_template


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = "admin"
        password = "fluffyunicorns"
        r_user = request.form.get("user")
        r_password = request.form.get("password")
        print(r_user, r_password)
        if r_user == user and r_password == password:
            return redirect(url_for("logged_in"))
        else:
            return redirect(url_for("failed_to_login"))
    else:
        return render_template("login.html")


@app.route("/logged_in")
def logged_in():
    return "You guessed right!"


@app.route("/failed_to_login")
def failed_to_login():
    return render_template("login.html", failed=True)


if __name__ == "__main__":
    app.run()
