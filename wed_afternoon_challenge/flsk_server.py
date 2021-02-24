#!/usr/bin/env python3
#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template, url_for, redirect


app = Flask(__name__)

groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/", methods=["POST", "GET"])
@app.route("/add_ip", methods=["POST", "GET"])
def adder():
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


app.run(port=2224)
