
"""Hundred million
1億件INSERT実験所。

■ 前提1
| id | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8 | c9 |
|----|----|----|----|----|----|----|----|----|----|
| AI |    |    |    |    |    |    |    |    |    |
こんなテーブルに1億件INSERTして時間を測るぜ。

■ 前提2
一件ずつINSERT、いっぺんにINSERT、オートインクリメント不使用でINSERT(なんかAIあると遅くなるってよ)で試す。
SQLをべた書きするsqliteライブラリと、今風のsqlalchemyライブラリを試す。

★ 1,000,000(百万)件での結果
    <INFO> 「sqliteライブラリで」「一件ずつ」。           経過時間: 4.15887
    <INFO> 「sqliteライブラリで」「いっぺんに」。          経過時間: 3.36102
    <INFO> 「sqliteライブラリで」「いっぺんに」「AI抜き」。    経過時間: 2.96409
    <INFO> 「sqlalchemyライブラリで」「一件ずつ」。       経過時間: 95.36684
    <INFO> 「sqlalchemyライブラリで」「いっぺんに」。      経過時間: 90.67611
    <INFO> 「sqlalchemyライブラリで」「いっぺんに」「AI抜き」。経過時間: 65.10438
この時点で sqlalchemy は切り捨て。

★ 100,000,000(一億)件での結果。
    <INFO> 「sqliteライブラリで」「一件ずつ」。経過時間: 420.95453
    <INFO> 「sqliteライブラリで」「いっぺんに」。経過時間: 347.19524
    <INFO> 「sqliteライブラリで」「いっぺんに」「AI抜き」。経過時間: 315.41997

● 今回の結論
大量にINSERTしてみるときは……
    SQLべた書き系ライブラリを使おう。
    「いっぺんに」「AI抜き」でやろう。
    AI抜きってのはテーブルに定義自体あっちゃダメってこと。
"""


import sqlite3
from contextlib import closing
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

HUNDRED_MILLION = 1000000


# sqliteライブラリで一件ずつ。
def sqlite_1():
    # メモリ上にsqlite作成。
    with closing(sqlite3.connect(':memory:')) as con:
        con.row_factory = sqlite3.Row
        # テーブル作成。
        con.execute('CREATE TABLE tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, c1, c2, c3, c4, c5, c6, c7, c8, c9)')
        # さあいくぜ1億件。
        values = (
            { 'c1':'c1','c2':'c2','c3':'c3','c4':'c4','c5':'c5','c6':'c6','c7':'c7','c8':'c8','c9':'c9',}
            for i in range(HUNDRED_MILLION)
        )
        with con:
            for value in values:
                con.execute('INSERT INTO tbl(c1,c2,c3,c4,c5,c6,c7,c8,c9) VALUES (:c1,:c2,:c3,:c4,:c5,:c6,:c7,:c8,:c9)', value)

# sqliteライブラリでいっぺんに。
def sqlite_2():
    # メモリ上にsqlite作成。
    with closing(sqlite3.connect(':memory:')) as con:
        con.row_factory = sqlite3.Row
        # テーブル作成。
        con.execute('CREATE TABLE tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, c1, c2, c3, c4, c5, c6, c7, c8, c9)')
        # さあいくぜ1億件。
        values = (
            { 'c1':'c1','c2':'c2','c3':'c3','c4':'c4','c5':'c5','c6':'c6','c7':'c7','c8':'c8','c9':'c9',}
            for i in range(HUNDRED_MILLION)
        )
        with con:
            con.executemany('INSERT INTO tbl(c1,c2,c3,c4,c5,c6,c7,c8,c9) VALUES (:c1,:c2,:c3,:c4,:c5,:c6,:c7,:c8,:c9)', values)

# sqliteライブラリでAIを設定せずいっぺんに。
def sqlite_3():
    # メモリ上にsqlite作成。
    with closing(sqlite3.connect(':memory:')) as con:
        con.row_factory = sqlite3.Row
        # テーブル作成。
        con.execute('CREATE TABLE tbl(id INTEGER PRIMARY KEY, c1, c2, c3, c4, c5, c6, c7, c8, c9)')
        # さあいくぜ1億件。
        values = (
            { 'id':i,'c1':'c1','c2':'c2','c3':'c3','c4':'c4','c5':'c5','c6':'c6','c7':'c7','c8':'c8','c9':'c9',}
            for i in range(HUNDRED_MILLION)
        )
        with con:
            con.executemany('INSERT INTO tbl(c1,c2,c3,c4,c5,c6,c7,c8,c9) VALUES (:c1,:c2,:c3,:c4,:c5,:c6,:c7,:c8,:c9)', values)

# sqlalchemyライブラリで一件ずつ。
def sqlalchemy_1():
    # メモリ上にsqlite作成。
    engine = create_engine('sqlite:///:memory:')
    # テーブル作成。
    Base = declarative_base()
    class Tbl(Base):
        __tablename__ = 'tbl'
        id = Column(Integer, primary_key=True, autoincrement=True)
        c1 = Column(String(10))
        c2 = Column(String(10))
        c3 = Column(String(10))
        c4 = Column(String(10))
        c5 = Column(String(10))
        c6 = Column(String(10))
        c7 = Column(String(10))
        c8 = Column(String(10))
        c9 = Column(String(10))
    Base.metadata.create_all(engine)
    # セッション開始。
    session = sessionmaker(bind=engine)()
    # さあいくぜ1億件。
    values = (
        Tbl(c1='c1',c2='c2',c3='c3',c4='c4',c5='c5',c6='c6',c7='c7',c8='c8',c9='c9')
        for i in range(HUNDRED_MILLION)
    )
    for value in values:
        session.add(value)
    session.commit()

# sqlalchemyライブラリでいっぺんに。
def sqlalchemy_2():
    # メモリ上にsqlite作成。
    engine = create_engine('sqlite:///:memory:')
    # テーブル作成。
    Base = declarative_base()
    class Tbl(Base):
        __tablename__ = 'tbl'
        id = Column(Integer, primary_key=True, autoincrement=True)
        c1 = Column(String(10))
        c2 = Column(String(10))
        c3 = Column(String(10))
        c4 = Column(String(10))
        c5 = Column(String(10))
        c6 = Column(String(10))
        c7 = Column(String(10))
        c8 = Column(String(10))
        c9 = Column(String(10))
    Base.metadata.create_all(engine)
    # セッション開始。
    session = sessionmaker(bind=engine)()
    # さあいくぜ1億件。
    values = (
        Tbl(c1='c1',c2='c2',c3='c3',c4='c4',c5='c5',c6='c6',c7='c7',c8='c8',c9='c9')
        for i in range(HUNDRED_MILLION)
    )
    session.add_all(values)
    session.commit()

# sqlalchemyライブラリでAIを設定せずいっぺんに。
def sqlalchemy_3():
    # メモリ上にsqlite作成。
    engine = create_engine('sqlite:///:memory:')
    # テーブル作成。
    Base = declarative_base()
    class Tbl(Base):
        __tablename__ = 'tbl'
        id = Column(Integer, primary_key=True)
        c1 = Column(String(10))
        c2 = Column(String(10))
        c3 = Column(String(10))
        c4 = Column(String(10))
        c5 = Column(String(10))
        c6 = Column(String(10))
        c7 = Column(String(10))
        c8 = Column(String(10))
        c9 = Column(String(10))
    Base.metadata.create_all(engine)
    # セッション開始。
    session = sessionmaker(bind=engine)()
    # さあいくぜ1億件。
    values = (
        Tbl(id=i, c1='c1',c2='c2',c3='c3',c4='c4',c5='c5',c6='c6',c7='c7',c8='c8',c9='c9')
        for i in range(HUNDRED_MILLION)
    )
    session.add_all(values)
    session.commit()


if __name__ == '__main__':

    print('---------------------------------------------------------------------------')
    start = time.time()
    sqlite_1()
    print(f'<INFO> 「sqliteライブラリで」「一件ずつ」。経過時間: {round(time.time() - start, 5)}')

    print('---------------------------------------------------------------------------')
    start = time.time()
    sqlite_2()
    print(f'<INFO> 「sqliteライブラリで」「いっぺんに」。経過時間: {round(time.time() - start, 5)}')

    print('---------------------------------------------------------------------------')
    start = time.time()
    sqlite_3()
    print(f'<INFO> 「sqliteライブラリで」「いっぺんに」「AI抜き」。経過時間: {round(time.time() - start, 5)}')

    # print('---------------------------------------------------------------------------')
    # start = time.time()
    # sqlalchemy_1()
    # print(f'<INFO> 「sqlalchemyライブラリで」「一件ずつ」。経過時間: {round(time.time() - start, 5)}')

    # print('---------------------------------------------------------------------------')
    # start = time.time()
    # sqlalchemy_2()
    # print(f'<INFO> 「sqlalchemyライブラリで」「いっぺんに」。経過時間: {round(time.time() - start, 5)}')

    # print('---------------------------------------------------------------------------')
    # start = time.time()
    # sqlalchemy_3()
    # print(f'<INFO> 「sqlalchemyライブラリで」「いっぺんに」「AI抜き」。経過時間: {round(time.time() - start, 5)}')
