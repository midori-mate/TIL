# !/usr/bin/env python
# coding: utf-8

# ==============================
# assert 条件式, 出すメッセージ
#     条件式がFalseのとき例外を飛ばす
# raise エラーの種類(出すメッセージ)
#     assertと違って条件は式の中に書けない
#     あと種類を知ってないといけない

# 俺の場合エラーの種類調べるの面倒がってassertばっかり使いそう

# しかしオライリーには「assertはraiseより使用頻度は落ちるでしょう」と書いてある
# 初心者はだいたい邪道をいくものデスヨネー。(ﾄｦｲﾒ)
# ==============================


def checkRaise():
    for i in range(10):
        if i > 5:
            raise ValueError('Problem occurs! num=' + str(i))
        else:
            print(i)

def checkAssert():
    a = 3
    b = 2
    # 条件式がFalseのとき
    assert a < b, 'aがb以上になっちゃってるよ'

# このtryを外すとふつーの例外がもさっと出力されるよ
try:
    checkRaise()
except Exception as e:
    print(e)
try:
    checkAssert()
except Exception as e:
    print(e)

