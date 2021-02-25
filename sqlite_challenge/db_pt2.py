#!/usr/bin/env python3

import sqlite3


def create_table(table_name="COMPANY"):
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
     (ID INT PRIMARY KEY     NOT NULL,
     NAME           TEXT    NOT NULL,
     AGE            INT     NOT NULL,
     ADDRESS        CHAR(50),
     SALARY         REAL);''')
    print(f"Table '{table_name}' created successfully")
    conn.close()


def insert_data(id, name, age, address, salary, table_name="COMPANY"):
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f"INSERT INTO {table_name} (ID,NAME,AGE,ADDRESS,SALARY) VALUES ({id}, '{name}', {age}, '{address}', {salary})")
    conn.commit()
    print("Records created successfully")
    conn.close()


def select_data(selector, table_name="COMPANY"):
    """
    :param selector: sting - comma separated like 'id, name, salary'
    :param table_name: string - name of table
    """
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    cursor = conn.execute(f"SELECT {selector} from COMPANY")
    rows = []
    for row in cursor:
        print(row)
        rows.append(row)
    print("Operation done successfully")
    conn.close()
    return rows


def update_data(set_param, set_value, where_param, where_value, table_name="COMPANY"):
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f"UPDATE {table_name} set {set_param} = '{set_value}' where {where_param} = '{where_value}'")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)
    db_info = select_data("id, name, address, salary")
    for row in db_info:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print("Operation done successfully")
    conn.close()


def delete_data(where_param, where_value, table_name="COMPANY"):
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute(f"DELETE from {table_name} where {where_param} = '{where_value}';")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    db_info = select_data("id, name, address, salary")
    for row in db_info:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print("Operation done successfully")
    conn.close()


if __name__ == "__main__":
    create_table("COMPANY")
    insert_data(22, "CHAD", 34, "carlisle", 900000)
    select_data("id, name")
    update_data("SALARY", 800000, "name", "CHAD")
    delete_data("name", "CHAD")
