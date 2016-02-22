# !/usr/bin/env python
# coding: utf-8

# ==============================
# x = 1 ～ (1 ～ 10)
# xの値はどんな確率で分布するのかを出すスクリプト
# ==============================

# 自由に変えてね
START = 1
END   = 10

def foo():
    resultsList = []
    x = range(START, END + 1)

    for i in x:
        result1 = 1 / len(x)          # 最初のサイコロでiが出る確率
        result2 = 0
        for j in range(i, END + 1):   # 最初のサイコロで出た値から1までをまわす
            result2 += (1 / j)
        result = result1 * result2
        resultsList.append(result)
        print("結果が%sになる確率は%sです" % (i, round(result, 3)))

    print("(確認のため)合計は", sum(resultsList))

foo()