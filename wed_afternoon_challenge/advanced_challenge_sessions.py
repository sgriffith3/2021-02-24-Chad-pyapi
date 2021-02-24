#!/usr/bin/env python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)
app.secret_key = "any random string"
groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

## If the user hits the root of our API
@app.route("/")
def index():
  ## if the key "username" has a value in session
  if "username" in session:
    username = session["username"]
    return redirect(url_for("adder"))

  ## if the key "username" does not have a value in session
  return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route("/add_ip", methods=["POST", "GET"])
def adder():
    if "username" in session:
        if request.method == "POST":
            hostname = request.form.get("hostname")
            ip = request.form.get("ip")
            fqdn = request.form.get("fqdn")
            groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
            print(groups)
            return redirect(url_for('adder'))
        else:
            print("Groups again")
            print(groups)
            return render_template("hostsfile.html", groups=groups)
    else:
        return redirect(url_for("login"))


## If the user hits /login with a GET or POST
@app.route("/login", methods = ["GET", "POST"])
def login():
   ## if you sent us a POST because you clicked the login button
   if request.method == "POST":

      ## request.form["xyzkey"]: use indexing if you know the key exists
      ## request.form.get("xyzkey"): use get if the key might not exist
      session["username"] = request.form.get("username")

      if session["username"] == "Chad":
          return redirect(url_for("index"))
      else:
          return redirect(url_for("login"))

   ## return this HTML data if you send us a GET
   return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
   # remove the username from the session if it is there
   session.pop("username", None)
   return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host="127.0.0.1", port=2224)
