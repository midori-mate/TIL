#!/usr/bin/env python
# coding: utf-8

'''署名作成セット。'''

name = 'William Forsyth'


def deco_wakusen_arg(x):
    def deco_wakusen(func):
        def call_kari(name):
            ret = ''
            ret += '--------------------\n'
            ret += '  ' + func(name) + x + '\n'
            ret += '--------------------'
            return ret
        return call_kari
    return deco_wakusen


def deco_oomoji(func):
    def call_kari(name):
        return (func(name)).upper()
    return call_kari


@deco_wakusen_arg('デス★')
@deco_oomoji
def call(name):
    return name


print(call(name))
