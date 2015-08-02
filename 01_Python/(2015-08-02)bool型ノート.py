# coding: utf-8

# bool について
# ブール型は True か False の値のみをもつ。

print(True) # True
print(type(True)) # <type 'bool'>
print(type(False))

# True は1, False は0として振る舞える。

print(1 + True) # 2
print(0 + False) # 1

# ただしブール型と整数型は異なる。

print(1 is 1) # True
print(1 is True) # False

