# http://www.geocities.jp/m_hiroi/light/index.html#python_abc
# ここの情報ノート

# --- 関数 ---
	def square(x):
		return x * x
	print square(10) # 100

# --- ローカル変数、グローバル変数 ---
	# square() の仮引数 x は関数実行中のみ有効 = ローカル変数(local variable)
	# 関数の外で定義した x は global variable
	# ローカル変数が有効な範囲をスコープという。
	def foo(x):
		print x
		print y # Sunaba と違ってグローバル変数を関数内で使ってもいい

# --- リストも渡せる ---
	def sum_list(a):
		total = 0
		for b in a:
			total += b
		return total
	print sum_list([1, 2, 3]) # 6

# --- デフォルト引数 ---
	def foo(a, b = 10, c = 'c'):
		print a, b, c
	foo(1) # 1, 10, c が出る

# --- キーワード引数 ---
	def foo(a, b = 10, c = 'c'):
		print a, b, c
	foo(1, c = 'しい', b = 2)
	# 順番があべこべでもOK
	def bar(a, b = 10, **c):
		print a, b, c
	bar(1, b = 20, d = 20, e = 40) # {'d': 20, 'e': 40}ってのが出てくる

# --- ディクショナリを展開して関数に渡す ---
	dic1 = {'a': 10, 'b': 20}
	def foo(a = 1, b = 2):
		print a, b
	print foo(**dic1) # 10, 20 が出てくる

# --- リストを展開して関数に渡す ---
	list1 = [1, 2]
	def foo(a, b):
		print a, b
	foo(*list1) # 1, 2

# --- 可変個の引数 ---
	def baz(a, *b):
		print a, b
	baz(1) # 1 ()
	baz(1, 2) # 1 (2,)
	baz(1, 2, 3) # 1 (2, 3)
	# タプルにぶち込んでくれる。でもコレ何に使うんだ
	def baz1(*a):
		print a
	baz1(1, 2, 3) # 全部まとめてタプルにぶちこむ

# --- 例題、データの探索 ---
	list0 = [0, 1, 2, 3]
	def find(a, data):
		for x in data:
			if x == a:
				print str(a) + ' あったよ'
				break
		else: print 'なかったよ '
	find(4, list0)
	# 位置を返す場合
	def position(a, data):
		for i, x, in enumerate(data):
			if x == a: return i
		return - 1
	# 個数を返す
	def count_item(a, data):
		c = 0
		for x in data:
			if x == a: c += 1
		return c

# --- 二分探索 ---
	# binary searching
	# 線形探索は要素数に比例してヤバいので log2N に比例する時間でデータを探す log ってなんだっけ★
	# まず小さい順に sort して、半分にわけて検索していく
	def bsearch(x, list):
		low = 0
		high = len(list) - 1
		# 探索区間を low から high とする。リストの最初から、リストの長さ - 1 
		while low <= high:
			middle = (low + high) / 2
			# middle は区間の中央値
			if x == list[middle]:
				return True
			# middle の値が x と一致したら True
			elif x > list[middle]:
				low = middle + 1
			# middle の値より x が小さかったら探索区間の low を middle の一個上に。
			else:
				high = middle - 1
			# その逆
		return False

# --- ソート ---
	# sort メソッドもあるけど手作業でこんな感じ
	def insert_sort(list):
		size = len(list) # リストの長さを変数 size にセット
		i = 1
		while i < size:
			tmp = list[i] # リストの要素を1から順繰りに tmp に入れてく
			j = i - 1 # j は i が1のとき0番目
			while j >= 0 and tmp < list[j]: # もし1番目が0番目より小さかったら…(入れ替えないといけない)
				list[j + 1] = list[j] # 1番目を0番目にする
				j -= 1
			list[j + 1] = tmp
			i += 1

# --- 値呼びと参照呼び(関数の呼び出し方) ---
	# call by value と call by reference
	# call: 1. 仮引数を用意 2. データを引数に代入 3. 関数実行後、引数を廃棄

# --- モジュール ---
	# プログラムの書かれているソースファイルがひとつのモジュールになる。 .py を除いたファイル名がモジュール名。
	# foo.py
	a = 10
	def test(): print 'module foo' # これは関数の内容
	# bar.py
	a = 100
	def test(): print 'module bar'
	# 利用するときは import 文を使う。上のファイルがカレントディレクトリにあるなら、
	import foo, bar # foo, bar をインポート。
	# このときモジュール内のプログラムを実行。つまり a に数字を代入して関数 test() を定義する。
	a = 1000 # a に 1000 代入
	def test(): print 'test' # 関数 test() を定義。 a = 1000 もこれもメインモジュールに登録される
	# メインモジュール内の変数や関数は変数名や関数名だけでアクセスできるので、 a なら 1000, test() なら test
	a # 1000
	# 他のモジュールに定義された変数関数にアクセスするには、名前の前にモジュール名とドットをつける
	# foo.a ならモジュール foo の変数 a にアクセスするので
	foo.a # 値は10
	bar.a # 同じく100
	test() # メインモジュールの関数 test() にアクセス
	test
	foo.test() # モジュール foo の test() にアクセス
	module foo
	bar.test() # モジュール bar の test() にアクセス
	module bar

# --- from 文 ---
	# from {モジュール名} import {名前}, ...
	# 名前の衝突がない場合はこれを使うとモジュール名を付けなくていいのでラク
	from foo import a, test
	a # 10
	test() # module foo
	# メインモジュールに a も test() もないので foo. をつけなくていい
	# import * にするとモジュール内のすべての名前を使える! ただし _ で始まる名前は除く
	from bar import *
	a # 100
	test() # module bar
	# 同じ名前の関数を再定義してもエラーにはならない
	from foo import *
	from bar import *
	test() # module bar のほうが出る

# --- ファイル出入力 ---
	# Python はファイルオブジェクトを介してファイルにアクセスする
	# キーボードからの入力を「標準入力」、画面への出力を「標準出力」という
	# これに対応するファイルオブジェクトはモジュール sys の変数に格納されてる
	# stdin: 標準入力 stdout: 出力 stderr: 標準エラー出力
	# 標準入力からデータを受け取る関数 imput() raw_input()
	>>> input()
	'foo' # 'foo' と出る
	>>> input('number > ')
	number > # が予め出る
	# input() は標準入力からデータを1行読み、結果を返す。引数に文字列を渡すとプロンプトとして表示
	>>> raw_input()
	foo # 'foo'
	>>> raw_input('number > ')
	number > # が予め出る
	# raw_input() は1行読み、それを文字列にして返す
	>>> for x in [1, 2, 3]:
	print x, # 1 2 3 と出る
	# 末尾に , をいれると改行されない
	>>> for x in [1, 2, 3]:
	print x, x * x # 1 1 {改行} 2 4 {改行} 3 9 と出る
	# 合計値を求めるプログラム
	total = 0
	while True:
		a = input()
		if a < 0: break
		total += a
	print 'total =', total
	# キーボードから数値入力。 -1入力で合計値
	# 列ごとの合計値を求める場合
	total = [0]
	while True:
		a = raw_input()
		if a == '': break
		for x, y in enumerate(a.split()):
			if x < len(total):
				total[x] = total[x] + int(y)
			else:
				total.append(int(y))
	print 'total =',
	for x in total: print x,
	# リスト total に列ごとの合計値を求める。 raw_input() で1行読んで変数 a にセット。
	# データの終了は空文字列''で判断。 a が空文字列なら break 。
	# 次にスペースやタブを区切り文字として、 a.split() で文字列を分離。
	# split() は文字列のメソッドで、分離した文字列をリストに格納して返す
	a = '1 2 3'
	a.split() # ['1', '2', '3']

# --- for 文とファイルオブジェクト ---
	# ファイルをコレクションのように順番に読み込みたい
	import sys # stdin を使うため sys をインポート
	total = [0]
	n = 0
	for a in sys.stdin:
		for x, y in enumerate(a.split()):
			if x <= n:
				total[x] = total[x] + int(y)
			else:
				total.append(int(y))
				n += 1
	print 'total =',
	for x in total: print x,
	# ファイルをリダイレクトする場合は正常に動作するがキーボードから入力するとうまい動作しない
	# はァ? なら別にどうでもいいか

# --- 標準出入力を使わずにファイルにアクセスする ---
	# 1. アクセスするファイルをオープンする。
	# アクセスするファイルを指定して、一対一に対応するファイルオブジェクトを生成する
	# 2. 出入力関数(メソッド)を使ってファイルを読み書きする。
	# ファイルをオープンするには open() とじるには close()
	open(filename, access_mode)
	# アクセスモードの種類 r(read) w(write) a(append追加)
	# ファイル出入力のメソッド
	read(size) # バイトを読み込んで文字列で返す。 size 省略するとファイル全体をよむ
	readline() # 1行読んで文字列で返す
	readlines() # 全部の行を読んでリストに格納して返す
	write(s) # 文字列 s をファイルに書き込む
	writelines(x) # リスト x に格納された文字列をファイルに書き込む
	out_f = open('test.dat', 'w') # test.dat をライトモードで開いて0-9を書き込む
	for x in range(10):
		out_f.write(str(x) + '\n') # str(x) は引数 x を文字列に変換する。 \n は改行
	out_f.close()
	in_f = open('test.dat') # test.dat のデータを読み込む。アクセスモードを省略すると r になる
	for x in in_f: # for でファイルから1行ずつ読み、 print する
		print x, # 0 1 2 3 4 5 6 7 8 9
	in_f.close()

# --- コマンドライン引数の取得 ---
	# モジュール sys の変数 argv にコマンドラインで与えられた引数が格納されてる
	import sys
	print sys.argv
	# これで argv が表示される
	import sys
	total = [0]
	in_f = open(sys.argv[1]) # ファイルをオープンし、ファイルオブジェクトを変数 in_f にセット
	for a in in_f: # ファイルから1行読み、列ごとに数値の合計値を求める
		for x, y in enumerate(a.split()):
			if x < len(total):
				total[x] = total[x] + int(y)
			else:
				total.append(int(y))
	in_f.close() # ファイルをクローズ
	print 'total =',
	for x in total: print x, # 列ごとの合計値を表示

# --- 文字列のフォーマット操作 ---
	# print はデータをそのまま出力
	# 整形して出力したい場合は文字列のフォーマット操作を使う
	書式文字列 % (data1, data2, ...)
	# 書式文字列は文字列として扱われるが、途中に % が現れると、その後ろの文字を変換指示子として理解する
	%d # 10進数
	%o # 8進数
	%x # 16進数
	>>> '%d %o %x' % (100, 100, 100)
	'100 144 64'
	# 変換指示子とデータの個数があわないとエラー。 % を出したいなら %%
	# % と変換指示子の間にオプションを入れられる
	# マップキー、フラグ、最小フィールド幅、精度、変換修飾子
	>>> '[%d]' % 10
	'[10]'
	>>> '[%4d]' % 10
	'[  10]'
	>>> '[%04d]' % 10 # フィールド幅を0で埋めたい場合、フラグに0指定
	'[0010]'
	>>> '[%-4d]' % 10 # 左詰めにしたいならフラグに - 指定
	'[10  ]'
	# 変換指示子 r はデータを関数 repr() で文字列に変換して表示
	# 変換指示子 s だと \n を読む 
	>>> a = 'hey, man\n'
	>>> print '%s %r' % (a, a)
	hey, man
	'hey, man\n'
	>>> print '[%20s] [%20r]' % (a, a) # フィールド幅の指定もできる

