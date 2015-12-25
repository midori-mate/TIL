# coding: utf-8

"""
python34--scriptsでcmd pip install PyMySQL でモジュールをインストール。
"""

### PyMySQL ###
import pymysql.cursors

connection = pymysql.connect(
    host        = "localhost",
    user        = "root",
    password    = "",
    db          = "mate",
    charset     = "utf8",
    cursorclass = pymysql.cursors.DictCursor)

### pms SELECT ###
with connection.cursor() as cursor:
    query = "SELECT * FROM members;"
    cursor.execute(query)
    result = cursor.fetchall() # or fetchone()
    print(result)              # [{'age': '25', 'id': 1, 'name': 'Watashi'},...]

### pms INSERT etc ###
with connection.cursor() as cursor:
    query = "INSERT INTO members (name, age) VALUES (%s, %s);"
    cursor.execute(query, ("Shin", 24))
    connection.commit()

connection.close()

### Sqlite3 ###
import sqlite3

connection = sqlite3.connect("mate.sqlite3")
cursor = connection.cursor()

### sqlite SELECT ###
def assoc(trash):                   # sqlite3はassocの無いクソ野郎なので自分で作る
    COLUMNS = ["id", "name", "age"] # ここにカラムを順番通りに書く
    rows    = []
    for i in range(len(trash)):
        rows.append({})
        for j in range(len(trash[i])):
            rows[i][COLUMNS[j]] = trash[i][j]
    return rows
query = "SELECT * FROM members;"
cursor.execute(query)
trash = cursor.fetchall()
rows  = assoc(trash)                # [{'id': 1, 'name': 'Watashi', 'age': 25},...]
print(rows)

### sqlite INSERT etc ###
query = "INSERT INTO members (name,age) VALUES (?,?)"
cursor.execute(query, ("Wada", 26))
connection.commit()

cursor.close()
connection.close()
