#!/usr/bin/env python
# coding: utf-8

'''code_golf?

多重リストの中の[0]:[3]をディクショナリにしたい。
'''

lis = [
    ['10032', 'clinic', 'pw', 'http://10032:pw'],
    ['10033', 'clinic', 'pw', 'http://10033:pw'],
    ['10046', 'clinic', 'pw', 'http://10046:pw'],
    ['aaa',   'clinic', 'pw', 'http://10046:pw']
]

'''もともとはこれ。最近mapとかlambdaとか使えるようになったからこれを一行にしてみたい。

ret = {}
for row in lis:
    if row[0].isdigit():
        ret[row[0]] = row[3]
'''

# 俺の作品。filterと内包表記の応用。
# ret = {l[0]: l[3] for l in filter(lambda dic: dic[0].isdigit(), lis)}

# ナカオさんの作品。こんなふうにifをかけたのかー!
ret = {l[0]: l[3] for l in lis if l[0].isdigit()}

print(ret)
# こうなってほしい
# {'10032': 'http://10032:pw', '10033': 'http://10033:pw', '10046': 'http://10046:pw'}


# ==========================
# おまけ 内包表記がわかってきたので手遊び書いた。

# 偶数 かつ 3の倍数 をまわすリスト
for i in [i for i in range(10) if (i % 2 == 0) and (i % 3 == 0)]:
    print(i)
