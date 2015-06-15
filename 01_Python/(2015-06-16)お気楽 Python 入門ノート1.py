# http://www.geocities.jp/m_hiroi/light/index.html#python_abc
# ここの情報ノート

# --- 数 ---
	a = 100
	print a
	# 変数に値をセットすること = 代入
	x = y = z = 0 # 複数の変数に同時代入できる
	# 算出演算子
	x / y # 商
	x % y # 剰余
	x ** y # x の y 乗

# --- 文字列 ---
	'\n' # 改行
	'\t' # タブ 無効にしたかったら文字列の前に r をつける
	str.count(sub[, start[, end]]) # str 内の sub の個数を検索して数えてくれる

# print 5 + "5" 他の言語はこれでいいけどpythonエラーが出る
	print 5 + int("5") # 整数
	print 5 + float("5") # 小数
	age = 25
	print "i am " + str(age) + " years old!"

# --- リスト ---
	list1 = [1, 'a', 3 + 1]
	list2 = [] # 空リスト
	list1[- 1] # リストの要素にアクセスするには [] を使う
	list3 = [[1, 2], [3, 4]] # 多次元配列も可能
	list3[0][1] # この結果は2になる

# --- リストに適用できる操作 ---
	# L にはリストの名前を入れてね
	L.append(x) # 最後尾に追加
	L.index(x) # x を探して位置をくれる
	L.insert(i, x) # i 番目に x 追加
	L.pop() # 最後尾を削除
	L.remove(x) # x を削除
	del L[i] # i 番目を削除
	L[start:end] = List # 代入
	# list1[2:2] = [10, 20] ってやると [0, 1, 2] が [0, 1, 10, 20, 2] になる
	# 空リストを代入すると要素を削除できる
	# これらの操作はリストを直接書き換えるので破壊的操作という。かっけえ。破壊的操作
	# L.append(x) この構造は object.method(arguments) 
	# すべてのデータはオブジェクトとして扱う。メソッドはオブジェクトを操作する関数のこと。
	# これがオブジェクト指向機能かな?

# リストで使える命令 sort, reverse, split, join
	sales = [50, 100, 80, 45]
	# sort / reverse
	sales.sort() # 小さい順に並び替え
	print sales
	sales.reverse() # 逆向きに並び替え
	print sales

# 文字列とリスト
	d = "2015/3/29"
	print d.split("/") # この文字で分ける
	a = ["a", "b", "c"]
	print "-".join(a) # この文字で文字列に

# --- タプル ---
	# 変更がきかないリスト
	tuple1 = (1, 2, 3)
	tuple2 = 'a', 'b' # () つけなくてもタプルになる
	a[0] # [] でアクセス
	x, y, z = a # タプルを使って同時代入。 x = y = z = 0 よりスマートかも
	# 間違い! これはできない。みっつに代入するにはこう
	a = 1, 2, 3 # これは [] 使ってリストでも大丈夫
	x, y, z = a
	a = 1, # これは要素いっこのタプルになる

# --- シーケンス ---
	# データを一列に並べたデータ構造のこと
	s = 'abc' # これもシーケンスなので [] でアクセスできる
	s[0] # みたいな感じ。もちろん 'a' のこと
	# 以下はスライス操作。スライスってのはシーケンスの部分列を取り出す操作
	s[start:end] # start から end - 1 まで。なんで - 1 やねん
	s[start:] # 最後尾まで
	s[:end] # 先頭から end - 1 まで。
	s[:] # 全部
	len(s) # 要素数。 length のこと

# --- ディクショナリ ---
	# 連想配列のこと。wtf is it
	# リストは整数値を使って要素を指定し、ディクショナリはキーを使って指定
	d = {'foo': 10, 'bar': 20}
	d['foo'] # 10
	# ずっと「なんでここでリスト?」とか思ってたけど、これはリストってかアクセスの手段なんだね。
	# 関数とメソッド
	dict() # ディクショナリ生成。 d = dict([('foo', 1)]) みたいに書けばいい
	del D[key] # キーと値を削除
	len(D) # 要素数
	D.clear() # ディクショナリを空に
	D.keys() # キーをリストにしてくれる。取り出しの順番はクレイジー
	D.values() # 値をリストにしてくれる。クレイジー
	D.items() # 連想リストにしてくれる。連想リストって [('foo', 10), ('bar', 20)] こういうの。クレイジー
	D1.update(D2) # D1 に D2 追加
	D["A"] = 'B' #要素追加

# コレクション: 複数の要素を格納するデータ型。リスト、タプル、文字列、ディクショナリ
# セットもコレクションだが、上の連中と違って順番や重複がない

# --- セット ---
	# 複数の要素を格納するデータ型のこと。
	set() # セット生成。 ([1, 2, 3]) ってやること。 a = set([1, 2, 3])
	frozenset() # タプルみたいなセット(変更不可)
	len(S) # 要素数
	S.add(x) # 追加
	S.remove(x) # 削除
	S.clear() # 空に
	S.update(xs) # コレクション xs の要素を追加
	# 他のメソッド
	s1.issubset(s2) # s1 が s2 の部分集合なら True
	s1.issuperset(s2) # s1 が s2 の部分集合なら True
	s1.intersection(s2) # s1 と s2 の積
	s1.union(s2) # s1 と s2 の和
	s1.difference(s2) # s1 - s2
	s1.symmetic_difference(s2) # s1 と s2 の両方にひとつだけ表れる要素

# --- if 文 ---
	# 条件部が真のとき実行されるブロックが then 節、偽のときが else 節
	if test_a:
		処理 A
	else:
		if test_b:
			処理 B
		else:
			処理 C
	# 上の入れ子構造と、下の入れ子構造は一緒
	if test_a:
		処理 A
	elif test_b: # elif はいくらでも繋げられる
		処理 B
	else:
		処理 C
	# elif じゃなくて全部 if でよくね?

# --- 比較演算子、論理演算子 ---
	x < y < z # みたいに書けるけど、C言語はダメなんだって
	not x # 真偽反転
	x and y # x と y 両方真なら真
	x or y # どっちか真なら真

# --- コレクション用の演算子 ---
	5 in [1, 2, 5] # True
	5 not in [1, 2, 5] # False
	'foo' in {'foo': 1, 'bar': 2} # True

# --- while と for で繰り返し
	# while はまあええやろ。 for は要素があるかぎり繰り返す
	a = [1, 2, 3]
	for x in a:
		print x # 結果は 1 2 3。ディクショナリの場合、取り出す順番はわからん
	for a, b in [[1, 2], [3, 4], [5, 6]]:
		print a * b # タプルで複数指定もOK

# --- break と continue 使って繰り返しの制御 ---
	while a:
		処理 A
		if b: continue # b が真だったら、この行で while a に戻る
		処理 B
		if c: break # b が偽だったらこの行にきて、 c が真ならループをブチ抜いて処理 E が行われる
		処理 C
	else:
		処理 D
	処理 E
	# 例をもういっこ
	while 1:
		print 'a'
		if 1: break
		print 'b'
	else:
		print 'c'
	print 'd'
	# この場合 print されるのは a, d

# --- 関数 range でリストを作る ---
	range(end)
	range(start, end)
	range(start, end, step)
	# while を使うと
	n = 0
	while n < 10:
		print 'fuck you shit up brains motherfucker'
		n += 1
	# 4行になっちゃうけど、 for と range を使うと?
	for i in range(10):
		print 'fuck ry'
	# 2行…だと?
	# 1 から 1000 までを加算するプログラムはこう
	total = 0
	for i in range(1001):
		total += i
	print total

# --- for 使ってリストの内包表現 ---
	a = [1, 2, 3]
	print [x * x for x in a] # a の要素をそれぞれ累乗したもの
	print [(x, x * x) for x in a] # (2, 4) とか作る
	print [x * x for x in a if x % 2 == 0] # 累乗したものの中で偶数のやつを出す

# --- for 使った関数とメソッド ---
	# これと
	for n, m in enumerate(['a', 'b', 'c']):
		print n, m
	# これがいっしょ
	n = 0
	for m in ['a', 'b', 'c']:
		print n, m
		n += 1
	# とにかく for 文ってのは4行を2行にしてくれるんですな
	# iteritems() はディクショナリのメソッド。キーと値を取り出す。 interation は反復。
	d = {'foo': 1, 'bar': 2}
	for key, value in d.iteritems():
		print key, value
	# D.items() のメソッドは [('foo', 10), ('bar', 20)] ってのを返す。
	# zip() は各リストの要素をタプルに詰め込み、リストに格納する
	zip(['a', 'b'], [1, 2]) # [('a', 1), ('b', 2)]
	for x, y in zip([1, 2], [10, 20]):
		print x + y # 11, 22

# --- 例題、素数を求める ---
	list = [2] # まず 2
	for x in range(3, 100, 2): # 3 から 99 までの奇数を片っ端から x に入れる
		for y in list: # list 内の素数を片っ端から y に入れる
			if x % y == 0: break # x が y で割り切れたら素数じゃないのでこの for ループ(yのやつ)を終了
		else: list.append(x) 
			# 最初 else 文のインデントを + 1 してたがソレだと
			# x を指定 -> y(これまでの素数) が0にならないたびに x をリストに追加しやがる。
	print list


