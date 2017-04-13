#!/usr/bin/env python
# coding: utf-8

'''pythonデコレータノート
bottleフレームワークで遊んでるとき出会ったデコレータ表記がわかんなかったのでてめーで書いてみたもの。

# こんなの。わけわかんなかった
@route('/hello/:name')
def hello(name='CINEVA'):
    return template('template_02', name=name)
'''


'''簡単な例'''


# funcを受け取ってinnerを返す
def outer(func):

    # outerの受け取ったfuncの実行結果に1足して返す
    def inner():
        ret = func()
        return ret + 1

    return inner


def foo():
    return 1


# foo + 何らかの処理 というデコレーション版関数
foo = outer(foo)
print(foo())


'''もう少し実用的例
x,yの座標ペアを保持するライブラリがあるが、加算減算機能がない。
加算減算を付与したい。
'''


# 上述のライブラリ。x,yを保持するくせに加算減算がねえ。
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # このインスタンスをrepr(ins)で覗いたときに表示されるもの。
    # print(ins)でも表示されるけど、__str__のほうは優先度が上。
    def __repr__(self):
        return 'Coordinateオブジェクト: ' + str(self.__dict__)

    # このインスタンスをstr(ins)で覗いたときに表示されるもの。
    # print(ins)でも表示されますよ。
    def __str__(self):
        return 'このオブジェクトにゃ以下の連中が含まれてるにょーん: ' + str(self.__dict__)


def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
print(repr(add(one, two)))
print(repr(sub(one, two)))


'''できたぜ! しかし、もし「結果の最低値を0とする」って前提が増えたらどうする?
いやadd()とsub()にそれぞれ下限チェックを入れてもいいけど、もう少しスマートになんない?
そこでデコレータですよ!
'''


def wrapper(func):
    # デコレータを使わない場合、このcheckerの中身をaddとsubにそれぞれ書かないといけなかったのです。
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(
                ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker


add = wrapper(add)
sub = wrapper(sub)
print(repr(add(one, two)))
print(repr(sub(one, two)))


'''いやぶっちゃけこれを書いてる時点ではサクサクッと理解できてないがつまり、
既存の関数になんか機能を追加したいときに使えるってことだろ?
クラスの継承はもう分かってて、メソッドの上書きも理解してるけど、
確かにメソッドを「上書きじゃなくて機能追加をしたい」ってときはある。
もしかしてデコレータはそれを実現さしてくれんのか?
ちょっと自分でやってみよう。
'''

import random


# 機能を追加したい関数。aDbをやってくれますわよ。
def original_func_aaa(a, b):
    ret = 0
    for i in range(a):
        ret += random.randint(1, b)
    return ret


# 普通に実行すると1〜6のダイスになる。
print(original_func_aaa(1, 6))


# そこに「引数は1以上の整数のみ」を入れたい。
def wrapper_func_aaa(func):
    def checker(a, b):
        if a <= 0 or b <= 0 or type(a) != int or type(b) != int:
            print('値が不正のためしゅーりょー。')
            exit()
        ret = func(a, b)
        return ret
    return checker


decorated_func_aaa = wrapper_func_aaa(original_func_aaa)
# print(decorated_func_aaa(1, 6))
# print(decorated_func_aaa(1, 0))  # 値が不正のためしゅーりょーと出る


'''デコレータの記述は@で代用できる
上で自分で作ったやつは以下のように書き換えられる。
'''


# あっまあこの書き方だとdecorated_func_aaaって名前じゃなくなっちゃうけどね。
@wrapper_func_aaa
def original_func_aaa(a, b):
    ret = 0
    for i in range(a):
        ret += random.randint(1, b)
    return ret


# print(original_func_aaa(1, 0))  # 値が不正のためしゅーりょーと出る
