#!/usr/bin/env python
# coding: utf-8

'''署名作成セット。'''

name = 'William Forsyth'


def call(name):
    return name


print(call(name))


def deco_wakusen(func):
    def call_kari(name):
        ret = ''
        ret += '--------------------\n'
        ret += '  ' + func(name) + '\n'
        ret += '--------------------'
        return ret
    return call_kari


call_wakusen = deco_wakusen(call)
print(call_wakusen(name))


def deco_oomoji(func):
    def call_kari(name):
        return func(name).upper()
    return call_kari


call_oomoji = deco_oomoji(call)
print(call_oomoji(name))


call_wakusen = deco_wakusen(call)
call_wakusen_oomoji = deco_oomoji(call_wakusen)
print(call_wakusen_oomoji(name))
