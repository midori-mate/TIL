# coding: utf-8
# カレントディレクトリ移動ノート

import os
import sys

# __file__          :このファイルの名前。Sublime上で実行すると絶対パスで出してくれる。ナゼ?
# os.path.abspath() :絶対パス出してくれる。
# os.path.dirname() :ファイルのあるディレクトリ名。
# os.chdir()        :cd
os.chdir(os.path.dirname(os.path.abspath(__file__)))

##### cx_freezeするなら以下 ####

def cd_():
    # sys.frozenを返す。存在しなければFalseになる。
    if hasattr(sys, 'frozen'):
        os.chdir(os.path.dirname(sys.executable))
    else:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
cd_()

print(os.getcwd())

# 注意:これをcx_freezeするときはbaseをNoneで行うこと! Win32GUIで固めると出力ができないからね。
