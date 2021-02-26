#!/usr/bin/env python3

from flask import Flask, render_template, request
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)


def read_excel(filename):
    file_data = pd.read_excel(filename)
    file_json = file_data.to_json()
    print(file_json)
    return file_json


@app.route("/")
@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":  # if method is a get (same as "/upload")
        return render_template("upload.html")
    if request.method == "POST":
        f = request.files["file"]
        new_filename = secure_filename(f.filename)
        f.save(new_filename)
        file_json = read_excel(new_filename)
        return file_json


if __name__ == "__main__":
    read_excel("example.xlsx")
    app.run(host="0.0.0.0", port=2224)
