
"""何年前スクリプト

与えられた datetime を「何 日/月/年 前」という文字列に変換する。
変換ルールは作者の都合によるものなので、あなたの感覚とは違う可能性もある。

まあそういうことなんだけれど、読みづらい上にまとまりがない。
なんとかもっと見やすくしたい。
"""

from datetime import datetime

def calc_delta(now, dt):

    years       = now.year - dt.year
    months      = now.month - dt.month
    days        = now.day - dt.day
    actual_days = (now - dt).days

    print( years,months,days,actual_days )

    if actual_days == 0:
        return '今日'

    before_today_of_each_year = months >= 0 and days >= 0
    if not before_today_of_each_year:
        years -= 1

    before_today_of_each_month = days >= 0
    if not before_today_of_each_month:
        months = 11 if months == 0 else months - 1

    print( years,months,days,actual_days )

    for num, label in zip([years,  months, actual_days], ['年', '月', '日']):
        if num > 0:
            return f'{num}{label}前'


NOW = datetime(2000, 8, 15)
cases = [
    [datetime(1998,  8, 15), '2年前'],
    [datetime(1998,  8, 16), '1年前'],
    [datetime(1999,  8, 15), '1年前'],
    [datetime(1999,  8, 16), '11月前'],
    [datetime(2000,  3, 15), '5月前'],
    [datetime(2000,  6, 16), '1月前'],
    [datetime(2000,  7, 15), '1月前'],
    [datetime(2000,  7, 16), '30日前'],
    [datetime(2000,  8, 14), '1日前'],
    [datetime(2000,  8, 15), '今日'],
]
for case in cases:
    print(case[1])
    actual   = calc_delta(NOW, case[0])
    expected = case[1]
    print()
    assert actual == expected, f'ほしかったのは"{expected}"、実際にできたのが"{actual}"'
print( 'ハイ OK デス。' )
