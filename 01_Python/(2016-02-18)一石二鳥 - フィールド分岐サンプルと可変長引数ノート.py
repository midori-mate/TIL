# !/usr/bin/env python
# coding: utf-8

# ==============================
# フィールド分岐のサンプル
#     eval()を使った可変のクラス名で、インスタンス無しでそのメソッドが呼べることがわかった
#     加えて、可変長引数を使えばデータ種類の増加ごとにメソッド側でいちいち仮引数の表記を増やさなくていいこともわかった。
# ==============================

class Start:
    def start(self, fieldName):
        aaaa = "AAAA"
        bbbb = "BBBB"
        eval(fieldName + "Field").main(name=fieldName, a=aaaa, b=bbbb)

class NagoyaField:
    def main(**args):
        print("here is %s field" % args["name"])
        print(args)

class NagakuteField:
    def main(**args):
        print("here is %s field" % args["name"])
        print(args)

if __name__ == "__main__":
    name = "Nagoya"
    a = Start()
    a.start(name)


