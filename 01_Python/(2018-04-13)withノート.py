# coding: utf-8

# 久々にpython触ったらwithすら忘れてたのでwithの使い方ノート withノート

with open("aaaaa.sql", 'r', encoding='utf8') as f:
    print(f.read())

import datetime
with open(datetime.datetime.today().strftime('%Y.%m.%d_%H%M%S'), 'w', encoding='utf8') as f:
    f.write('smt\n')
