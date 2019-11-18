"""1億件INSERT実験所 sqlalchemy 編

| id | c1 | c2 | c3 | c4 | c5 |
|----|----|----|----|----|----|
|  1 | c1 | c2 | c3 | c4 | c5 |
|  2 | c1 | c2 | c3 | c4 | c5 |

| 条件 ＼ INSERT 件数 |   100万  |     1億     |
|---------------------|----------|-------------|
| 1件ずつ             | 80.42750 | MemoryError |
| いっぺんに          | 79.35631 | MemoryError |
| AI なしでいっぺんに | 54.97433 | MemoryError |

"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time


MILLION         =   1_000_000
TEN_MILLION     =  10_000_000
HUNDRED_MILLION = 100_000_000
INSERT_NUM = TEN_MILLION


def alchemy_1():
    """AI あり、1件ずつ。"""

    # メモリ上に sqlite を作成します。
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
    Base.metadata.create_all(engine)

    # セッション開始。
    session = sessionmaker(bind=engine)()

    # INSERT データ作成。
    values = (
        Tbl(c1='c1',c2='c2',c3='c3',c4='c4',c5='c5')
        for i in range(INSERT_NUM)
    )

    # 1件ずつ INSERT します。
    for value in values:
        session.add(value)
    session.commit()


def alchemy_2():
    """AI あり、全件同時。"""

    engine = create_engine('sqlite:///:memory:')
    Base = declarative_base()
    class Tbl(Base):
        __tablename__ = 'tbl'
        id = Column(Integer, primary_key=True, autoincrement=True)
        c1 = Column(String(10))
        c2 = Column(String(10))
        c3 = Column(String(10))
        c4 = Column(String(10))
        c5 = Column(String(10))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    values = (
        Tbl(c1='c1',c2='c2',c3='c3',c4='c4',c5='c5')
        for i in range(INSERT_NUM)
    )
    # add_all で全件同時に INSERT します。
    session.add_all(values)
    session.commit()


def alchemy_3():
    """AI なし、全件同時。"""

    engine = create_engine('sqlite:///:memory:')
    Base = declarative_base()
    class Tbl(Base):
        __tablename__ = 'tbl'
        # AI を外して table 定義します。
        id = Column(Integer, primary_key=True)
        c1 = Column(String(10))
        c2 = Column(String(10))
        c3 = Column(String(10))
        c4 = Column(String(10))
        c5 = Column(String(10))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    values = (
        Tbl(id=i, c1='c1',c2='c2',c3='c3',c4='c4',c5='c5')
        for i in range(INSERT_NUM)
    )
    session.add_all(values)
    session.commit()


func = alchemy_1
# func = alchemy_2
# func = alchemy_3

start = time.time()
func()
print(f'件数:{INSERT_NUM} 経過秒数:{round(time.time() - start, 5)}')
