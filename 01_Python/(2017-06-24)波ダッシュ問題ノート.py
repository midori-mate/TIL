#!/usr/bin/env python
# coding: utf-8

'''波ダッシュ問題ノート
マジびっくりなことに、'〜'と'～'は違う。
'''


print('---------- まえがき ----------')


wavedash = '〜'  # SJISにはこっちしかない。 波ダッシュ 'WAVE DASH' b'\xe3\x80\x9c'
fullwidthtilde = '～'  # 全角チルダ 'FULLWIDTH TILDE' b'\xef\xbd\x9e'
print(wavedash == fullwidthtilde)  # Falseになりやがる

# バイトに変換すると違うことがわかる。
print('WAVE DASH: ' + str(wavedash.encode('utf8')))
print('FULLWIDTH TILDE: ' + str(fullwidthtilde.encode('utf8')))


print('---------- 判別関数 ----------')


def is_WAVEDASH(char):
    return char.encode('utf8') == b'\xe3\x80\x9c'


print(is_WAVEDASH(wavedash))
print(is_WAVEDASH(fullwidthtilde))


def is_FULLWIDTHTILDE(char):
    return char.encode('utf8') == b'\xef\xbd\x9e'


print(is_FULLWIDTHTILDE(wavedash))
print(is_FULLWIDTHTILDE(fullwidthtilde))


print('---------- 変換関数 ----------')


# これらを統一する関数。stringに波ダッシュがあったら全角チルダに変換する。
def convert_WAVEDASH_to_FULLWIDTHTILDE(string, reverse=False):
    wavedash = (b'\xe3\x80\x9c').decode('utf-8')
    fullwidthtilde = (b'\xef\xbd\x9e').decode('utf-8')
    if not reverse:
        return string.replace(wavedash, fullwidthtilde)
    else:
        return string.replace(fullwidthtilde, wavedash)


print(is_FULLWIDTHTILDE(convert_WAVEDASH_to_FULLWIDTHTILDE(wavedash)))
print(convert_WAVEDASH_to_FULLWIDTHTILDE(wavedash).encode('utf8'))

print(is_WAVEDASH(convert_WAVEDASH_to_FULLWIDTHTILDE(fullwidthtilde, reverse=True)))
print(convert_WAVEDASH_to_FULLWIDTHTILDE(fullwidthtilde, reverse=True).encode('utf8'))
