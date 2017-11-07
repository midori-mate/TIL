#!/usr/bin/env python
# coding: utf-8

# 無名関数即時実行ノート

# ふつうの無名関数
lambda a, b: print(a + b)

# 定義と同時に実行
(lambda a, b: print(a + b))(1,2)  # 3

# へー! って思ったけどlambdaって一行しか書けねーし出番なさそう。

'''javascriptとかphpだと複数行書けるから、グローバルスコープの変数汚染防止のために使えるみたい。

(function() {
    echo 1;
    echo 2;
    echo 3;
})()

ただしphpはphp7からじゃないとダメ。
'''
