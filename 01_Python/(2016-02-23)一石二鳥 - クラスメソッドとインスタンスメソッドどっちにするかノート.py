# !/usr/bin/env python
# coding: utf-8

ちょっとほぞん

class GrandPa:
    def baz(self, key):
        if key == "z":
            self.bar()

    def bar(self):    # テンプレートメソッドパターン
        print("オリジナルのbarだよー")

class Parent(GrandPa):
    def foo(self):
        while 1:
            print("なんか入力してね　できたらz")
            key = input()
            self.baz(key)

    def bar(self):
        print("書き換えられたbarでーす")

class Child(GrandPa):
    def main(self):
        a = Parent()
        a.foo()


instance = Child()
instance.main()


保存２
class GrandPa:
    def __init__(self):
        self.name = "NAME"

    def baz(self, key):
        if key == "z":
            self.bar()

    def bar(self):
        self.name = "CHANGED NAME"

class Parent(GrandPa):
    def foo(self):
        while 1:
            print("なんか入力してね　できたらz")
            key = input()
            self.baz(key)
            break

    def bar(self):
        self.name = "NAME IN PARENT"

class Child(GrandPa):
    def main(self):
        a = Parent()
        a.foo()
        print(a.name)


instance = Child()
instance.main()