#!/usr/bin/env python3

import os
import random

from flask import Flask, render_template, request, send_file
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


@app.route("/gimme_excel", methods=["GET", "POST"])
def gimme_excel():
    if request.method == "GET":
        return "Please Post JSON"
    if not os.path.exists("docs"):
        os.mkdir("docs")
    j_data = request.json
    j_df = pd.DataFrame(j_data)
    f_name = f"{random.randint(1,1000000)}.xlsx"
    j_df.to_excel(f"docs/{f_name}")
    return f'<h1>Download Your New File Here:<h1><br><a href="/docs/{f_name}>/docs/{f_name}</a>'


@app.route("/docs/<filename>")
def download_doc(filename):
    docs_dir = os.path.join(os.getcwd(), "docs")
    return send_file(f"{docs_dir}/{filename}")


if __name__ == "__main__":
    read_excel("example.xlsx")
    app.run(host="0.0.0.0", port=2224)
