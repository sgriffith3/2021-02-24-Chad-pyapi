#!/usr/bin/env python3

import sqlite3

from flask import Flask, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    html = """
    <h1> Welcome to your COMPANY Database! </h1>
    <h3> What would you like to do? </h3>
    <a href="/create_table">Create a Table</a>
    <a href="/insert_data">Insert Data</a>
    <a href="/select_data">Select Data</a>
    <a href="/update_data">Update Data</a>
    <a href="/delete_data">Delete Data</a>
    """
    return html


@app.route("/create_table")
def create_table(table_name="Company"):
    table_name = request.args.get("table_name") if request.args.get("table_name") else table_name
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
     (ID INT     NOT NULL,
     NAME           TEXT    NOT NULL,
     AGE            INT     NOT NULL,
     ADDRESS        CHAR(50),
     SALARY         REAL);''')
    print("Table created successfully")
    conn.close()
    return f"Table {table_name} created!"


@app.route("/insert_data")
def insert_data(id=8675309, name="Bob", age=32, address="here", salary=50000, table_name="COMPANY"):
    # Set var = this value IF <expression>==True ELSE that value
    id = request.args.get("id") if request.args.get("id") else id
    name = request.args.get("name") if request.args.get("name") else name
    age = request.args.get("age") if request.args.get("age") else age
    address = request.args.get("address") if request.args.get("address") else address
    salary = request.args.get("salary") if request.args.get("salary") else salary
    table_name = request.args.get("table_name") if request.args.get("table_name") else table_name
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f"INSERT INTO {table_name} (ID,NAME,AGE,ADDRESS,SALARY) VALUES ({id}, '{name}', {age}, '{address}', {salary})")
    conn.commit()
    print("Records created successfully")
    conn.close()
    return f"INSERT INTO {table_name} (ID,NAME,AGE,ADDRESS,SALARY) VALUES ({id}, '{name}', {age}, '{address}', {salary})"


@app.route("/select_data")
def select_data(selector="name", table_name="COMPANY"):
    """
    :param selector: string - comma separated like 'id, name, salary'
    :param table_name: string - name of table

    try out the path /select_data?selector=id,%20name,%20age
    """
    selector = request.args.get("selector") if request.args.get("selector") else selector
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    cursor = conn.execute(f"SELECT {selector} from COMPANY")
    rows = []
    for row in cursor:
        print(row)
        rows.append(row)
    print("Operation done successfully")
    conn.close()
    data = {"command": f"SELECT {selector} from COMPANY", "result": rows}
    return jsonify(data)


@app.route("/update_data")
def update_data(set_param="salary", set_value=0, where_param="id", where_value=1, table_name="COMPANY"):
    set_param = request.args.get("set_param") if request.args.get("set_param") else set_param
    set_value = request.args.get("set_value") if request.args.get("set_value") else set_param
    where_param = request.args.get("where_param") if request.args.get("where_param") else where_param
    where_value = request.args.get("where_value") if request.args.get("where_value") else where_value
    table_name = request.args.get("table_name") if request.args.get("table_name") else table_name
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f"UPDATE {table_name} set {set_param} = '{set_value}' where {where_param} = '{where_value}'")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)
    conn.close()
    return redirect(url_for("select_data", selector="*"))


@app.route("/delete_data")
def delete_data(where_param="id", where_value=1, table_name="COMPANY"):
    where_param = request.args.get("where_param") if request.args.get("where_param") else where_param
    where_value = request.args.get("where_value") if request.args.get("where_value") else where_value
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f"DELETE from {table_name} where {where_param} = '{where_value}';")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    conn.close()
    return redirect(url_for("select_data", selector="*"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
