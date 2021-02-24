#!/usr/bin/env python3

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hi():
    return "Hi my friend!"


@app.route("/es")
def hola():
    return "Hola mi amigo!"


@app.route("/fr")
def salut():
    return "Salut mon ami!"


if __name__ == "__main__":
    app.run()
