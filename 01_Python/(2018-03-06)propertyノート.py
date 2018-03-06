#!/usr/bin/env python
# coding: utf-8

# ====================================
# @property ノート
# ====================================


# ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
# Homeworkクラスの変数gradeは、参照は自由。だけど値を変えるとき、0から100の間じゃないといけないとする。

class Homework:

    def __init__(self):
        self._grade = 0

    # これでgradeはメソッドじゃなくてインスタンス変数みたいに呼び出せるようになった。
    @property
    def grade(self):
        return self._grade

    # これでインスタンス変数gradeへ値代入するとき起こることを改造できる。
    @grade.setter
    def grade(self, new_grade):
        if not (0 <= new_grade <= 100):
            raise ValueError('grade は0〜100じゃないとダメ。')
        self._grade = new_grade

myHomework = Homework()
myHomework.grade = 50
# myHomework.grade = 150  ValueError: grade は0〜100じゃないとダメ。
