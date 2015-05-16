# coding: utf-8

foo = lambda a: a * 2
print foo(2)
def bar(a):
	return a ** 2
print bar(3)
# つまり lambda x: y で x が引数、 y が戻り値となる。

# map() と組み合わせる map(関数, リスト)
lis = [1, 3, 5]
ram = map(lambda a: a ** 2, lis)
print ram
bda = [a ** 2 for a in lis]
print bda
# 結果は同じ

# sorted() と組み合わせる
lis1 = [(1, 2), (3, 1), (5, 3)]
baz = sorted(lis1, key = lambda a: a[1])
print baz

# filter() と組み合わせる
class Album(object):
	def __init__(self, title, artist):
		self.title = title
		self.artist = artist
a1 = Album('A Hard Day\'s Night', 'The Beatles')
a2 = Album('The Rolling Stones', 'The Rolling Stones')
a3 = Album('Abbey Road', 'The Beatles')
albums = [a1, a2, a3]
albums_beatles = filter(lambda album: album.artist == 'The Beatles', albums)
for a in albums_beatles:
	print a.artist, '-', a.title

