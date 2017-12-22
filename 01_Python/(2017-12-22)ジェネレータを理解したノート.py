#!/usr/bin/env python
# coding: utf-8

# 関数諸君はリストを返さずジェネレータを返そう!
# でっかいリストをどかっと返すよりもメモリの節約になるぞ!


# ふつーのジェネレータを作ってみる。
def my_generator(string):
    '''もらった文字列を一文字ずつ返すジェネレータです。'''
    for s in string:
        yield s

generator = my_generator('あなかしこ')
print(next(generator))  # あ
print(next(generator))  # な
print(list(generator))  # ['か', 'し', 'こ']


# ふつーのジェネレータを作ってみる2。
def my_generator():
    yield 'あ'
    yield 'な'
    yield 'か'
    yield 'し'
    yield 'こ'

generator = my_generator()
print(next(generator))  # あ
print(next(generator))  # な
print(list(generator))  # ['か', 'し', 'こ']


# こういう動きをするオブジェクトをイテレータという。
# じゃあマイ・イテレータを作ってみようぜ!


class MyIterator:
    def __iter__(self):
        yield 'あ'
        yield 'な'
        yield 'か'
        yield 'し'
        yield 'こ'

# for文にイテレータオブジェクトを入れると、
iterator = MyIterator()
for i in iterator:
    print(i)
for i in iterator:
    print(i)

print(iterator)
