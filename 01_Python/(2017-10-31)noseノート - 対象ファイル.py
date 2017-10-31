#!/usr/bin/env python
# coding: utf-8


class Foo:

    # test_1 と test_2 で扱うよー。
    @staticmethod
    def static_method(x, y):
        return x + y

    # test_3 と test_4 で扱うよー。
    @staticmethod
    def exception_method(x):
        if x is True:
            raise TypeError()
        elif x is False:
            raise ValueError()
        elif x == 1:
            return x
        else:
            return None

    # test_5 で扱うよー。
    @staticmethod
    def use_other_class_method():
        return Bar.static_method()


class Bar:

    # test_5 で扱うよー。
    @staticmethod
    def static_method():
        return 1

    # test_7 で扱うよー。
    X = 1

    # test_7 で扱うよー。
    @classmethod
    def class_method(cls):
        return cls.X
