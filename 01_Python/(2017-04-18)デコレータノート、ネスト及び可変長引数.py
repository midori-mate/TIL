#!/usr/bin/env python
# coding: utf-8

'''パターン1
このデコレータをネストする書き方は、@省略記法にしか使えない
'''
def deco_wrapper(count_space):
    def deco_count(func):
        def func_kari(*args):
            if count_space:
                return len(func(*args))
            else:
                return len(func(*args).replace(' ', ''))
        return func_kari
    return deco_count


@deco_wrapper(True)
def call1(name):
    return name


@deco_wrapper(False)
def call2(name1, name2):
    return name1 + name2


# count_spaceをTrueにしたので5
print(call1('x x x'))

# count_spaceをFalseにしたので6
print(call2('x x x', 'y y y'))


'''パターン2
この書き方だと@省略記法は使えない。
'''
def deco_count(func, count_space):
    def func_kari(*args):
        if count_space:
            return len(func(*args))
        else:
            return len(func(*args).replace(' ', ''))
    return func_kari


def call3(name):
    return name


def call4(name1, name2):
    return name1 + name2


call3 = deco_count(call3, True)
call4 = deco_count(call4, False)

# count_spaceをTrueにしたので5
print(call3('x x x'))
# count_spaceをFalseにしたので6
print(call4('x x x', 'y y y'))


'''パターン2を@省略記法でやろうとしたパターン
これはエラー。
'''
@deco_count(True)
def call5(name):
    return name


print(call5('x x x'))

