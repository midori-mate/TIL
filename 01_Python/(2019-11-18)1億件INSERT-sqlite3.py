"""1億件INSERT実験所 sqlite3 編

| id | c1 | c2 | c3 | c4 | c5 |
|----|----|----|----|----|----|
|  1 | c1 | c2 | c3 | c4 | c5 |
|  2 | c1 | c2 | c3 | c4 | c5 |

| 条件 ＼ INSERT 件数 |  100万  |  1000万  |    1億    |
|---------------------|---------|----------|-----------|
| 1件ずつ             | 3.37001 | 32.84212 | 344.67605 |
| いっぺんに          | 2.54530 | 23.96085 | 251.14147 |
| AI なしでいっぺんに | 2.45202 | 25.83653 | 257.36283 |

"""


import sqlite3
from contextlib import closing
import time


MILLION         =   1_000_000
TEN_MILLION     =  10_000_000
HUNDRED_MILLION = 100_000_000
INSERT_NUM = HUNDRED_MILLION


def sqlite_1():
    """AI あり、1件ずつ。"""

    # メモリ上に sqlite を作成します。
    # NOTE: closing を使うことで con.close() を書く必要がなくなります。
    with closing(sqlite3.connect(':memory:')) as con:

        # テーブル作成。
        con.execute('CREATE TABLE tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, c1, c2, c3, c4, c5)')

        # INSERT データ作成。
        values = (
            { 'c1':'c1','c2':'c2','c3':'c3','c4':'c4','c5':'c5', }
            for i in range(INSERT_NUM)
        )

        # INSERT 開始。
        with con:
            # 1件ずつ INSERT します。
            for value in values:
                con.execute('INSERT INTO tbl(c1,c2,c3,c4,c5) VALUES (:c1,:c2,:c3,:c4,:c5)', value)


def sqlite_2():
    """AI あり、全件同時。"""

    with closing(sqlite3.connect(':memory:')) as con:
        con.execute('CREATE TABLE tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, c1, c2, c3, c4, c5)')
        values = (
            { 'c1':'c1','c2':'c2','c3':'c3','c4':'c4','c5':'c5', }
            for i in range(INSERT_NUM)
        )
        with con:
            # executemany で全件同時に INSERT します。
            con.executemany('INSERT INTO tbl(c1,c2,c3,c4,c5) VALUES (:c1,:c2,:c3,:c4,:c5)', values)


def sqlite_3():
    """AI なし、全件同時。"""

    with closing(sqlite3.connect(':memory:')) as con:
        # AI を外して table 定義します。
        con.execute('CREATE TABLE tbl(id INTEGER PRIMARY KEY, c1, c2, c3, c4, c5)')
        values = (
            { 'id':i,'c1':'c1','c2':'c2','c3':'c3','c4':'c4','c5':'c5', }
            for i in range(INSERT_NUM)
        )
        with con:
            con.executemany('INSERT INTO tbl(id, c1,c2,c3,c4,c5) VALUES (:id,:c1,:c2,:c3,:c4,:c5)', values)


# func = sqlite_1
# func = sqlite_2
func = sqlite_3

start = time.time()
func()
print(f'件数:{INSERT_NUM} 経過秒数:{round(time.time() - start, 5)}')

