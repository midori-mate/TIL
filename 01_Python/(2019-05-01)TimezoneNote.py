
"""TimezoneNote
"""


import datetime
import pytz


"""まとめ

・ tz付datetimeつくりたい -> PYTZを引数に
・ 文字列変換             -> %z が該当
・ タイムゾーン確認       -> DATETIME.tzinfo
・ あとからtzを付与       -> PYTZ.localize()
・ あとからtzを変更       -> DATETIME.astimezone(PYTZ)

"""

# いま
print( datetime.datetime.now(tz=pytz.timezone('utc')) )

# 特定の時間 8個目にtz指定しよう!
print( datetime.datetime(2019, 1, 31, 1, 2, 3, 4, pytz.timezone('utc')) )

# strptime
print( datetime.datetime.strptime('2018-02-14' + '+0000', '%Y-%m-%d%z') )

# strftime
_ = datetime.datetime.now(tz=pytz.timezone('utc'))
print( datetime.datetime.strftime(_, '%Y-%m-%d %z') )

# タイムゾーン情報を持っていることの確認。
#     もっているもの: aware  と呼ぶ
#     もってないもの: native と呼ぶ
aware  = datetime.datetime.now(tz=pytz.timezone('utc'))
native = datetime.datetime.now()
print(aware , '----', type(aware.tzinfo) , aware.tzinfo )
print(native, '----', type(native.tzinfo), native.tzinfo)

# native を aware にする
_ = datetime.datetime.now()
print( pytz.timezone('utc').localize(_) )

# タイムゾーンを変換 これは若干時間がかかる 実行すればわかる。
_ = datetime.datetime.now(tz=pytz.timezone('utc'))
print( _.astimezone(pytz.timezone('Asia/Tokyo')) )


"""Django では下記メソッドでタイムゾーンつき現在時刻を取得できる
"""
# from django.utils import timezone
# timezone.now()        UTC
# timezone.localtime()  設定したタイムゾーン
