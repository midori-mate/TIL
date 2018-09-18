#!/usr/bin/env python
# coding: utf-8

# https://twitter.com/methane/status/960775969563750400
# Pythonのグローバル名前空間は辞書（変数にアクセスするたびに変数名を文字列で探索してる）で糞遅いので、ループは関数の中でした方が良いです。
# 多分100倍遅いのが30倍遅いくらいにはなると思います。

import time

start = time.time()
lis = []
for i in range(10000000):
    lis.append(i)
    lis.pop()
margin = time.time() - start
print(f'結果: {margin}秒')  # 結果: 5.9079749584198秒



start = time.time()
def foo():
    lis = []
    for i in range(10000000):
        lis.append(i)
        lis.pop()
foo()
margin = time.time() - start
print(f'結果: {margin}秒')  # 結果: 5.282521963119507秒
