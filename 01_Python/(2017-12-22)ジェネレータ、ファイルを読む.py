#!/usr/bin/env python
# coding: utf-8

import os

# ファイルつくる
with open('foo.txt', 'w', encoding='utf8') as f:
    f.write('このファイルは' + os.linesep + '消される運命' + os.linesep + 'なのです……')

# テキストを一行ずつ抜き出す(改行コードつき)
f = open('foo.txt', 'r', encoding='UTF8')
gene = (a.strip() for a in f)

# ここでクローズするとエラーになる。
# f.close()

print(next(gene))  # このファイルは
print(next(gene))  # 消される運命
print(next(gene))  # なのです……

f.close()

# 疑問
# ジェネレータのいいところは、メモリ上にいっぺんにデータを置かないから、エコなことだったはず。
# 今回、ファイルを削除したあとも以降の行がprintできるってことは、どこかに内容を保存しているのでは?
# それじゃエコじゃないんじゃない?
