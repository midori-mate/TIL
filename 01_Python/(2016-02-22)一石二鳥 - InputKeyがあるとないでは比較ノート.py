# !/usr/bin/env python
# coding: utf-8

# ==============================
# ない場合
# ==============================
def example():
    while 1:
        print("(^o^) xかexitを入力してね")
        key = input()
        if key == "x"   : print("( ﾟo ﾟ) xが押されたよ")
        if key == "exit": print("(^~^) ループを出ます")

def example2():
    while 1:
        print("(^o^) xかexitを入力してね")
        key = input()
        if key == "x"   : print("えっくすがおされた")
        if key == "exit": print("るーぷをでる")


# ==============================
# ある場合 派生クラスのインスタンスを作って、InputKeyのメソッドを利用する
# ==============================
class InputKey:
    def foo(self, key):
        if key == "x"   : return self.inputX()
        if key == "exit": return self.inputE()
    def inputX(self): print("( ﾟo ﾟ) xが押されたよ")
    def inputE(self): print("(^~^) ループを出ます"); return 1

class Example(InputKey):
    def bar(self):
        while 1:
            print("(^o^) xかexitを入力してね")
            key = input()
            if self.foo(key): return 0
    def inputX(self): print("(-_-) xが押されました…")

ins1 = Example()
ins1.bar()


# ==============================
# あるけどインスタンスを作らない場合 メソッドを呼べはするが self.fooのインスタンスメソッドは使えない
# ==============================
class InputKey:
    def foo(self, key):
        if key == "x"   : return self.inputX()
        if key == "exit": return self.inputE()
    def inputX(self): print("( ﾟo ﾟ) xが押されたよ")
    def inputE(self): print("(^~^) ループを出ます"); return 1

class Example(InputKey):
    def bar():
        while 1:
            print("(^o^) xかexitを入力してね")
            key = input()
            if self.foo(key): return 0
    def inputX(self): print("(-_-) xが押されました…")

Example.bar()




