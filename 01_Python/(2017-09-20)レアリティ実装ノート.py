#!/usr/bin/env python
# coding: utf-8

# レアリティ実装ノート


# パターン1 =========================================================

items = {
    "Fox"       : 5,  # よく出る
    "Reactive"  : 3,
    "Whitehorse": 1,  # 一番レア
}
lis = []
for item in items:
    lis.extend(item.split(" ") * items[item])
# こういうのができる
# lis = ['Whitehorse', 'Reactive', 'Reactive', 'Reactive',
#        'Fox', 'Fox', 'Fox', 'Fox', 'Fox']

import random
print(random.choice(lis))
# 5/9でFox、1/9でWhitehorseが出る

# パターン1感想:
#     この手口の気になるところはlisの長さ。
#     なんども発生するであろう作業のたびに、
#     クソ長いリストを生成するのはどうにもエコノミックじゃない気がする。


# パターン2 =========================================================

items = {
    "Fox"       : 5,   # よく出る
    "Reactive"  : 3,
    "Whitehorse": 1,   # 一番レア
    }
itemList = list(items.keys())
popList  = [items[item] for item in itemList]

# itemList : ['Whitehorse', 'Reactive', 'Fox']
# popList  : [1, 3, 5]

# レアリティの数値を全部積み上げたもの 今回なら9
maximum = sum(popList)
# 9を上限とした乱数を出し、アイテム4つからなる層(popList)のどこに位置するか調査する
target = random.randint(1, maximum)
i = 0
for index in range(len(popList)):
    i += popList[index]
    if target <= i:
        print(itemList[index])
        # print(list(itemList)[index])

# これを9000回行い、アイテムが何度ずつドロップしたか集計してみた結果が以下。
# {'Whitehorse': 1027, 'Reactive': 2941, 'Fox': 5032}
#     1:3:5になってる。

# パターン2感想:
#     ビューリホー…。今回の最適解としてはコレかな。
