# !/usr/bin/env python
# coding: utf-8

import sys, time
wait = lambda sec: time.sleep(sec)

# ==============================
# 上書き出力 sys.stdout.write("\r") の実験ノート
# どういう仕組みなんだ?
#
# どうやら、\rはカーソルを行頭へ移動させる。
# \rは文字列を消すとかそういう効果ではなかったのだね。
# こういうのをキャリッジリターンと言うようだ。
# ==============================

# 1の3秒後に 1234 行頭に戻してから1を表示するのでふつーに1234
"     ";sys.stdout.write("\r1")
wait(1);sys.stdout.write("2")
wait(1);sys.stdout.write("3")
wait(1);sys.stdout.write("4")

# 1の3秒後に 234 1のあとで行頭に戻すので234
"     ";sys.stdout.write("1\r")
wait(1);sys.stdout.write("2")
wait(1);sys.stdout.write("3")
wait(1);sys.stdout.write("4")

# 1の3秒後に 423 123表示してから行頭に戻して4
"     ";sys.stdout.write("\r1")
wait(1);sys.stdout.write("2")
wait(1);sys.stdout.write("3")
wait(1);sys.stdout.write("\r4")

# 1の3秒後に 43 1表示したあと行頭に戻して23、また行頭いって4なので43
"     ";sys.stdout.write("1\r")
wait(1);sys.stdout.write("2")
wait(1);sys.stdout.write("3")
wait(1);sys.stdout.write("\r4")

# 1の3秒後に 423 行頭に戻して223表示してから行頭で4
"     ";sys.stdout.write("1\r")
wait(1);sys.stdout.write("22")
wait(1);sys.stdout.write("3")
wait(1);sys.stdout.write("\r4")

# 1の3秒後に 234 1のあと行頭から234表示して最後に行頭へ(何も起きない)
"     ";sys.stdout.write("1\r")
wait(1);sys.stdout.write("2")
wait(1);sys.stdout.write("3")
wait(1);sys.stdout.write("4\r")








