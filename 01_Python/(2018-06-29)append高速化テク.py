#!/usr/bin/env python
# coding: utf-8

'''list.append() の高速化!

こうしとく
lis = []
lis_push = lis.append

'''


import time

start = time.time()

# add 10000 things for 10000 loops.
for i in range(10000):
    arr = []
    arr_push = arr.append
    for i in range(10000):
        arr_push('foo')

margin = time.time() - start
print(f'結果: {margin}秒')

# ↑ took 7.9849 sec


start = time.time()

# add 10000 things for 10000 loops.
for i in range(10000):
    arr = []
    for i in range(10000):
        arr.append('foo')

margin = time.time() - start
print(f'結果: {margin}秒')

# ↑ took 11.9248 sec
