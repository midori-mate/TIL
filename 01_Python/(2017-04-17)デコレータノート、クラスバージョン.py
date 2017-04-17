#!/usr/bin/env python
# coding: utf-8

'''署名作成セット。'''

name = 'William Forsyth'


class Foo:
    def __init__(self, name):
        self.name = name

    def call(self):
        return self.name


instance = Foo(name)
print(instance.call())


class Deco_Wakusen:
    def __init__(self, instance):
        self.instance = instance

    def call(self):
        ret = ''
        ret += '--------------------\n'
        ret += '  ' + self.instance.call() + '\n'
        ret += '--------------------'
        return ret


instance_wakusen = Deco_Wakusen(instance)
print(instance_wakusen.call())


class Deco_Oomoji:
    def __init__(self, instance):
        self.instance = instance

    def call(self):
        return self.instance.call().upper()


instance_oomoji = Deco_Oomoji(instance)
print(instance_oomoji.call())


instance_wakusen = Deco_Wakusen(instance)
instance_wakusen_oomoji = Deco_Oomoji(instance_wakusen)
print(instance_wakusen_oomoji.call())
