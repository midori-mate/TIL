"""lambda の中で変数を使うときの罠

参考: https://stackoverflow.com/questions/938429/scope-of-lambda-functions-and-their-parameters
"""


# あ,い,う,え,お って表示される。
def function_a():
    functions = []
    functions.append(lambda: print('あ'))
    functions.append(lambda: print('い'))
    functions.append(lambda: print('う'))
    functions.append(lambda: print('え'))
    functions.append(lambda: print('お'))
    for func in functions:
        func()


# お,お,お,お,お って表示される。
def function_b():
    functions = []
    for hiragana in 'あいうえお':
        functions.append(lambda: print(hiragana))
        # lambda の中の hiragana は hiragana というグローバル変数の参照になっている。
        # for 内の hiragana のコピーにはなっていない。
        # つまり lambda: print(hiragana) は lambda: print('あ') にはなっておらず lambda: print(hiragana) のママなんだ。
        # for を抜けたあとにグローバル変数 hiragana を参照したら「お」になるだろ? そういうことが起こっている。
        #
        # そこで lambda hiragana=hiragana: print(hiragana) って書くと解決する。
        # こう書けば、 print(hiragana) の中の hiragana の参照先はグローバル変数の hiragana ではなく、 lambda の引数の hiragana になっている。
        # hiragana=hiragana の右側の hiragana は for hiragana のコピーだから lambda hiragana='あ': print(hiragana) になるってわけ。
    for func in functions:
        func()


function_a()
function_b()
