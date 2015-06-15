# coding: utf-8
# coding: cp932
# coding: euc-jp

s = u'日本語'

# 文字コードの変換を行う。変換できない文字が見つかった場合の処理を明示。
s.encode('utf-8')
s.encode('utf-8', errors = 'strict')
s.encode('utf-8', errors = 'ignore')
s.encode('utf-8', errors = 'replace')

# 外部とやりとりするときに文字コードを変換して、内部では unicode を使う。
# 以下は utf-8 で入力、 cp932 で出力する例。
# src = open('src_filename', 'rb')
# dst = open('dst_filename', 'wb')
# for line in src:
#     uline = unicode(line, 'utf-8')
#     dst.write(uline.encode('cp932'))

# ASCII 以外の文字列はエスケープされた状態で表示される。
# なお python3 では文字列が python2 の unicode に相当するものになったのでそのまま表示される。
print [u'ふが']
a = [u'ふが']
print repr(a).decode('unicode-escape') # これ使えば ok?
print ['はげ']
print str(['はげ']).decode('string-escape')

# あるいは以下のを使ってもいい。
# for 文を使う
for i in a:
	print i
# str() を使う
print str(a).decode('unicode-escape')
