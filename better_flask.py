#!/usr/bin/env python3

from flask import Flask
from flask import redirect, url_for, request


app = Flask(__name__)


@app.route("/")
@app.route("/en")
def hi(name="my friend"):
    name = request.args.get('name')
    greeting = f"Hi {name}"
    return greeting


@app.route("/es")
def hola(name="mi amigo"):
    name = request.args.get('name')
    greeting = f"Hola {name}"
    return greeting


@app.route("/fr")
def salut(name="mon ami"):
    name = request.args.get('name')
    greeting = f"Salut {name}"
    return greeting


@app.route("/<user>/<lang>")
def greet_them(user, lang="en"):
    if lang == "es":
        red = redirect(url_for("hola", name=user))
    elif lang == "fr":
        red = redirect(url_for("salut", name=user))
    else:
        red = redirect(url_for("hi", name=user))
    return red


if __name__ == "__main__":
    app.run()
