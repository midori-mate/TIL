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
