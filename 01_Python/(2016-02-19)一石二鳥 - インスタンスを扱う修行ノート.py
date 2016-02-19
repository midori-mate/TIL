# !/usr/bin/env python
# coding: utf-8

# ==============================
# クラスMainのメソッドstart内で、fieldNameを参考にNagoyaFieldのインスタンスを生成する。
# NagoyaField内でfieldNameがSuwaに変えて、インスタンスを廃棄する。
# ふたたびメソッドstart内でインスタンスを生成するが、今度はSuwaFieldのインスタンス。
# というように異なる種類のインスタンスを動的に生成、廃棄するプログラム。
# 全編を通して保持したいパラメータは、クラスDataのインスタンスdataのインスタンス属性として保存する。
# だから、Fieldのインスタンスを出たり入ったりするときは、記録装置としてインスタンスdataを受け渡すことになる。
# ==============================

class Main:
    def start(self):
        fieldName, step = DB.load()
        data  = Data(fieldName, step)
        print("開始時点のdata:", data.fieldName, data.step)
        while 1:
            field = eval(data.fieldName + "Field")(data)
            data  = field.walk(data)
            del field
            if data.fieldName == "Niigata":
                break
        print("start()終了時点のdata:", data.fieldName, data.step)

class DB:
    def load():
        # 実際はDBにアクセスすると思うけどここは単純に
        return "Nagoya", 0

class Data:
    def __init__(self, fieldName, step):
        self.fieldName = fieldName
        self.step      = step

class NagoyaField:
    def __init__(self, data):
        self.fieldName = data.fieldName
        self.step      = data.step

    def walk(self, data):
        self.step     += 100
        self.fieldName = "Suwa"
        data.fieldName = self.fieldName
        data.step      = self.step
        print("Nagoya.walk()終了時点のdata:", data.fieldName, data.step)
        return data

class SuwaField:
    def __init__(self, data):
        self.fieldName = data.fieldName
        self.step      = data.step

    def walk(self, data):
        self.step     += 50
        self.fieldName = "Niigata"
        data.fieldName = self.fieldName
        data.step      = self.step
        print("Suwa.walk()終了時点のdata:", data.fieldName, data.step)
        return data

if __name__ == "__main__":
    main = Main()
    main.start()

# ==============================
# 実行結果
# 開始時点のdata              : Nagoya  0
# Nagoya.walk()終了時点のdata : Suwa    100
# Suwa.walk()終了時点のdata   : Niigata 150
# start()終了時点のdata       : Niigata 150
# ==============================


# ==============================
# ぶっちゃけインスタンスつかわなくても、
# 以下のような感じでもいい。
# ==============================
"""
class Main:
    def start(self):
        fieldName, step = DB.load()
        data  = Data(fieldName, step)
        print("開始時点のdata:", data.fieldName, data.step)
        while 1:
            data = eval(data.fieldName + "Field").walk(data)
            if data.fieldName == "Niigata":
                break
        print("start()終了時点のdata:", data.fieldName, data.step)

class DB:
    def load():
        # 実際はDBにアクセスすると思うけどここは単純に
        return "Nagoya", 0

class Data:
    def __init__(self, fieldName, step):
        self.fieldName = fieldName
        self.step      = step

class NagoyaField:
    def walk(data):
        data.step     += 100
        data.fieldName = "Suwa"
        print("Nagoya.walk()終了時点のdata:", data.fieldName, data.step)
        return data

class SuwaField:
    def walk(data):
        data.step     += 50
        data.fieldName = "Niigata"
        print("Suwa.walk()終了時点のdata:", data.fieldName, data.step)
        return data

if __name__ == "__main__":
    main = Main()
    main.start()
"""