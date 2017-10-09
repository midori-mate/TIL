#!/usr/bin/env python
# coding: utf-8

'''raiseノート
javaでthrowを扱う作業をにない、よ〜うやくpythonのraiseが何をやってたのか理解できた。
(関数で呼ばれるとかした)下の階層で、能動的に作ったExceptionを上の階層にぶん投げて処理をそこで終えるのがraise。
javaではthrow(ぶん投げる)だけど、pythonではraise(ぶち上げる)わけだね。

処理を終えるんだったら
    print('第三階層でエラーが発生しました。')
    exit()
でいいじゃんって気がするけど、raiseするとスタックトレースが見れるのがグッドってわけ。
'''


# 第四階層
def baz():
    # 上の階層barにExceptionを能動的に浮かび上げ(raise)る。
    raise MidoriException('第四階層でエラーが発生しました。')


# 第三階層
def bar():
    # 浮かび上がってきたExceptionは勝手に上の階層fooに浮かび上がる。
    baz()


# 第二階層
def foo():
    # 同じく、勝手に上の階層(pythonさんの領域)に浮かび上がる。
    bar()


# これはfooと同じことが起こる。つまり普段、エラーが起きてるときは、その場で勝手にraiseが起きてると思ってよさげ。
def foo2():
    try:
        bar()
    except Exception as e:
        raise e


# 自分オリジナルの例外を作ってみる
class MidoriException(Exception):
    def __init__(self, error_message='緑エラーだよ。'):
        self.error_message = error_message

    def __str__(self):
        return self.error_message


foo()
