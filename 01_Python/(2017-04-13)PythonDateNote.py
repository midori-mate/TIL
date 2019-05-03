#!/usr/bin/env python
# coding: utf-8

'''python日付時刻ノート このノートはそのまま実行できるよ。(python3.6) DatetimeNote
1. 今の時間は?
2-1. フォーマットで文字列にするには?
2-2. じゃ数値にするには?
3. 明日の時間、数分後の時間は?(加算減算)
4. 時間の差分を求めるには?
5. 日付をタイムスタンプに変換するには?
'''

import time
import datetime
from dateutil.relativedelta import relativedelta


# 1. 今の時間は?
print(datetime.datetime.now())


# 2-1. フォーマットで文字列にするには?
#     注意:マジで原因不明だが、strftime()で作った「日本語含む」文字列はsublimeビルドで表示できねえ。
#     普通のprint('あ')は大丈夫なんだけどねえ…
# yyyy-mm-dd %Y-%m-%d
# yyyymmdd %Y%m%d
# yyyymm %Y%m
print(datetime.datetime.now().strftime('Year:%Y,month:%m,date:%d,Hour(24):%H,Minute:%M,Second:%S,A(day):%A'))
print(datetime.datetime.now().strftime(
    'HMS:%X'
    ))


# 2-2. じゃ数値にするには?
print(
    datetime.datetime.now().year,
    datetime.datetime.now().month,
    datetime.datetime.now().day,
    datetime.datetime.now().hour,
    datetime.datetime.now().minute,
    datetime.datetime.now().second
    )


# 3. 明日の時間、数分後の時間は?(加算減算)
print(datetime.datetime.now() + datetime.timedelta(
        weeks=1, days=1, hours=1, minutes=-1, seconds=-1
    ))


# 4-1. 時間の差分を求めるには?
a = datetime.datetime.now()
# /// なんか時間のかかる処理 ///
for i in range(100000):
    pass
# /// ///
b = datetime.datetime.now()
print((b - a).total_seconds())


# 4-2. 時間の差分、二通りめ
a = time.time()
for i in range(100000):
    pass
b = time.time()
print((b - a))


# 5. 日付をタイムスタンプに変換するには?
a = datetime.datetime.strptime('2018-11-19', '%Y-%m-%d')  # %Y-%m-%d %H:%M:%S
print(a)  # type は <class 'datetime.datetime'>
print(type(time.mktime(a.timetuple())))  # type は <class 'float'>


# 6. 月初
today = datetime.datetime.now()
print(datetime.datetime(today.year, today.month, 1))

# 7. 月末
print(datetime.datetime(today.year, today.month, 1) + relativedelta(months=1))
