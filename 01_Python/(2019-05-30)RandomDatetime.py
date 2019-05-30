
"""RandomDatetime
ランダムで日付時刻を生成する。
"""

import random
import datetime


def get_random_datetime(start, end, fmt):
    stime = datetime.datetime.strptime(start, fmt)
    etime = datetime.datetime.strptime(end  , fmt)
    rtime = stime + (etime - stime) * random.random()
    return rtime.strftime(fmt)


print( 'ランダム日付'    , get_random_datetime('2019-01-01 10:00', '2019-12-31 23:59', '%Y-%m-%d %H:%M') )
print( 'ランダム日付のみ', get_random_datetime('2019-01-01'      , '2019-12-31'      , '%Y-%m-%d'      ) )
print( 'ランダム時刻のみ', get_random_datetime('10:00'           , '23:59'           , '%H:%M'         ) )
