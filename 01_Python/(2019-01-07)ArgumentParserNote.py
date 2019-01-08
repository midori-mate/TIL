
"""ArgumentParserNote

コマンドライン引数を受け取るために sys.argv を使っていただろ?
ちょっと高度なのを使ってみよう。

実行例:
    python "(2019-01-07)ArgumentParserNote.py" みどりん -a 89 -f 0.12 --true
    python "(2019-01-07)ArgumentParserNote.py" -h
"""

import argparse

# パーサを作ります。
parser = argparse.ArgumentParser(description='★このプログラムの説明★')

# 必須の引数は - をつけずに指定します。
parser.add_argument('name', help='これは必須の引数です。')

# オプション引数は - をつけます。 ふたつ書くと省略形もつくれます。
parser.add_argument('-a', '--age', help='これはオプション引数です。')

# デフォルト値がほしいときは default です。
parser.add_argument('-i', '--int', default=0, help='デフォルトでは0になります。')

# 型指定もできます。
parser.add_argument('-f', '--float', type=float, help='float 限定の引数です。')

# フラグ。
parser.add_argument('-t', '--true', action='store_true')

# 解析します。 引数のエラーとかはここで出ます。 -h を指定するとここで止まります。
args = parser.parse_args()

# こういうふうに中身を取り出します。
print(args)
print(args.name)
print(args.age)
print(args.int)
print(args.float)
print(args.true)
