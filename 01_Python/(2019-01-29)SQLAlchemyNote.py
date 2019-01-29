
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


# スラッシュは3本要ります。
engine = create_engine('sqlite:///:memory:')

# モデルのベースを作成します。
Base = declarative_base()

# ベースを継承してモデルクラスを定義します。djangoでこういうのやったよね!
class Post(Base):

    # これよくね?
    __tablename__ = 'post'

    # フィールドたち。
    id = Column(Integer, primary_key=True)
    title_ja = Column(String(80))
    body_ja = Column(Text)

# モデルを使ってテーブルの作成をします。
Base.metadata.create_all(engine)

# セッションを介してクエリを実行します。
Session = sessionmaker(bind=engine)
session = Session()

# INSERT
session.add(Post(id=1, title_ja='はじめての記事', body_ja='さあー書くぞおーー。'))
# Commit
session.commit()

# 複数INSERT
session.add_all([
    Post(id=2, title_ja='ふたつめの記事', body_ja='さあー書くぞおーー。2'),
    Post(id=3, title_ja='みっつめの記事', body_ja='さあー書くぞおーー。3'),
    Post(id=4, title_ja='よっつめの記事', body_ja='さあー書くぞおーー。4'),
])
session.commit()

# SELECT
rows = session.query(Post).all()  # allは省略してもいい。
for row in rows:
    print(row.id, row.title_ja, row.body_ja)

# SELECT WHERE !!! filter_by のときはキーワード引数的にわたす !!!
row = session.query(Post).filter_by(id=3).one()
print(row.id, row.title_ja, row.body_ja)

# SELECT 存在しないときはException(NoResultFound)が飛ぶから注意。
try:
    row = session.query(Post).filter_by(id=100).one()
except NoResultFound as ex:
    print(ex)

# idで取得するときはget()が使えます。
row = session.query(Post).get(4)
print(row.id, row.title_ja)

# このとき存在しなくてもNoResultFoundじゃなくてNoneが返ってくる。間違ってフィールドを参照しようとするとAttributeErrorでまずいなー。
row = session.query(Post).get(100)
print(row)

# 並び替え。
for row in session.query(Post).order_by(Post.id.desc()):  # もちろん asc() もある。
    print(row.id)

# 行数指定はスライス。スライス大好き。
for row in session.query(Post).order_by(Post.id.desc())[1:3]:
    print(row.id)

# いろんなWHERE !!! filter のときはキーワード引数的には渡さない !!!
rows = (
    session.query(Post)
    .filter(Post.id==4, Post.id!=3, Post.id>1)  # 一致系の条件
    .filter(Post.title_ja.like('%記事%'))  # 部分一致
    .filter((Post.id>1) | (Post.id<4))  # or カッコの位置気をつけて
)
for row in rows:
    print(row.id, row.title_ja, row.body_ja)

# レコード数の取得。
session.query(Post).count()

# UPDATE
post = session.query(Post).filter(Post.id==4).one()
post.title_ja = 'よっつめの記事だよーガンガン書くぜ'
session.add(post)
session.commit()
print([row.title_ja for row in session.query(Post)])

# DELETE
post = session.query(Post).filter(Post.id==4).one()
session.delete(post)
session.commit()
print([row.title_ja for row in session.query(Post)])

# DELETEはこうでもよさそう。
session.query(Post).filter(Post.id==3).delete()
session.commit()
print([row.title_ja for row in session.query(Post)])

# 全件DELETE
session.query(Post).delete()
session.commit()
print([row.title_ja for row in session.query(Post)])

# セッションを終わるときはこれ。
session.close()
