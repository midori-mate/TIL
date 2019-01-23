
"""Sqlite Note SqliteNote Sqlite3Note

2018-12-27
    SELECT 時にカラム名を出力してくれないのがずっと不満だった。
    が今になって改めて調べてみたら普通に方法があったのでこれを機にノート作成。
    いままでディスってすまんかった sqlite3 よ。
    今回大事なのは
        ・ con.row_factory              -> すごくよい。
        ・ :memory:                     -> 実ファイルなしに試せる。
        ・ cursor はぶっちゃけいらない。       -> conで足りる。
        ・ commit() rollback() もいらない。 -> with con で足りる。
        ・ close() もいらない。             -> contextlib.closing を使う。
"""


import sqlite3
from contextlib import closing


# :memory: を使うとメモリ上に sqlite を作ってその場で試せるよ。(つよい)
def foo():

    # 接続作成。
    with closing(sqlite3.connect(':memory:')) as con:

        # テーブル作成。 これはトランザクションでロールバックされない。
        con.execute('CREATE TABLE xy(x, y)')

        # 中身をいれてみる。
        # with で囲わなかったら con が消えるのと同時にロールバックされる。
        xys = [
            {'x':'xxx', 'y':'yyy'},
            {'x':'xxxx', 'y':'yyyy'},
        ]
        with con:
            con.executemany('INSERT INTO xy(x, y) VALUES (:x, :y)', xys)

        # いまINSERTしたものをみる。
        for row in con.execute('SELECT x, y FROM xy'):
            print(row)

        # いまINSERTしたものを消してみる。
        with con:
            print('I just deleted', con.execute('DELETE FROM xy').rowcount, 'rows')


# 接続。
# これまでは
# 使い終わったら try, finally, close() をゴテゴテ書かないといけないけど
# with closing() を使うと自動でやってくれる。
# closing は、自動で close してくれるものと考えればよさげ。
def con():
    with closing(sqlite3.connect(FILENAME)) as con:
        con.row_factory = sqlite3.Row  # これをつけるとSELECTの結果にカラム名がつく。


"""contextlib.closing って何
書かないといけない
    finally: con.close()
を省略してくれるもの。with を抜けたとき自動で close() してくれるので安心。
"""

"""いや with がそもそも close() してくれるだろ?
ファイル open の場合はしてくれるけど db 接続のときはしてくれない。
ファイル open の __exit__ には close() が書いてあるけど、
con の __exit__ にはトランザクション処理に関することしか書いてないから。
"""


# カーソル。
def cursor():
    with closing(sqlite3.connect(FILENAME)) as con:
        cur = con.cursor()


"""ぶっちゃけカーソルいらないんじゃね?
いらねーというか覚える必要なさそう。
というのも con.execute(SQL) とかやると裏で勝手に cursor 作られてんだよ。
"""


# SELECT
# いくつか方法がある
#     conを使う, cursorを使って execute, fetchone, fetchall のどれかを使う。
# だけどシンプルに con でいいんじゃね?
def select():
    sql = ' '.join([
        'SELECT',
            '*',
        'FROM table',
        'WHERE id=:id',
    ])
    _ = con.execute(sql, {'id':1,})
    for row in _:
        print(dict(row))  # row_factory を設定してればカラム名つきで取得できる。


# トランザクション。
# with を使うと便利!
#     成功時: 勝手に con.commit() が呼ばれる。
#     失敗時: 勝手に con.rollback() が呼ばれる。
def transaction():
    with con:
        con.execute('INSERT ...')


# INSERT
def insert():
    sql= ' '.join([
        'INSERT INTO table',
            '(x, y)',
        'VALUES',
            '(:x, :y)',
    ])
    values = [
        {'x':'xxx', 'y':'yyy'},
        {'x':'xxx', 'y':'yyy'},
    ]

    # こうやって複数 SQL を一気に実行できるよ。
    with con:
        con.executemany(sql, values)


# これが欲しいんだろ? テーブル名の一覧と、フィールドの一覧。
def get_table_info(con):
    sql = ' '.join([
        'SELECT',
            'tbl_name',
        'FROM sqlite_master',
        'WHERE type=:type',
        'ORDER BY tbl_name',
    ])
    bind = { 'type': 'table', }
    tables = [dict(row)['tbl_name'] for row in con.execute(sql, bind)]

    table_info = {}
    for table in tables:
        sql = ''.join([
            f'PRAGMA TABLE_INFO({table})'
        ])
        table_info[table] = [dict(row)['name'] for row in con.execute(sql)]
    return table_info
