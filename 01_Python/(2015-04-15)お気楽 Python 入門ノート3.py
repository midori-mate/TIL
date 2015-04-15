# http://www.geocities.jp/m_hiroi/light/index.html#python_abc
# ここの情報ノート

# --- 再帰呼び出し recursive call, 再起定義 recursive difinition ---
	# 階乗の定義
	0! = 1
	n! = n * (n - 1)!
	# 階乗の関数
	def fact(n):
		if n == 0: return 1
		return n * fact(n - 1)
	# fact() の定義で fact() 自身を呼び出している。これが再起呼び出し
	# 5回目の再帰呼び出しで引数が0になるので、そこで return 1 が実行されて呼び出しがとまる
	# つまりは関数のなかでその関数使えるってこと

# --- ユークリッドの互除法 Euclidean Algorithm ---
	# 負でない整数 a, b(a > b) で、 a % b = r とする
	# このとき a, b の最大公約数は b, r の最大公約数に等しい
	# 証明: a, b の割り算はこう a = q * b + r ---(1)
	# a, b の最大公約数を m とすると、 a = m * a', b = m * b' となる
	# すると (1) = m * a' = q * m * b' + r ---(2)
	# 左辺が m で割り切れるので、右辺も m で割り切れる。つまり r は m で割り切れる。ゆえに m は b, r の公約数。
	# b, r の最大公約数を m' とすると m <= m' ---(3)
	# b = m' * b'', r = m' * r' として(1)に代入すると a = q * m' * b'' + m' * r' ---(4)
	# 右辺が m' で割り切れるので、左辺の a も m' で割り切れる。ゆえに m' は a, b の公約数。
	# m' は b, r の最大公約数なので m' <= m ---(5)
	# (3), (5) より m = m'
	# 最大公約数をもとめる関数
	def gcd(a, b): # greatest common divisor
		if b == 0: return a # b が0なら a を返す
		return gcd(b, a % b) # そうでなければ b と a % b の最大公約数を求める
	# gcd(a, b) = a, b の最大公約数は gcd(b, a % b) = b, r の最大公約数に等しいってこと
	# 最小公倍数をもとめる関数
	def lcm(a, b): # least common multiple
		return a * b / gcd(a, b)

# --- 末尾再帰と繰り返し tail recursion ---
	def fact(n):
		if n == 0: return 1
		return n * fact(n - 1)
	# これを末尾再帰にすると
	def fact(n, a = 1):
		if n == 0: return a
		return fact(n - 1, n * a)
	# gcd(a, b) を繰り返しにすると
	def gcd(a, b):
		while b > 0:
			a, b = b, a % b
		return a
	# 繰り返しのほうが速度やメモリの消費量の面で有利。

# --- クイックソート ---
	# 前にやった挿入ソートは要素数の二乗に比例する遅いソート。再起定義を使って高速なソートアルゴリズムを作る
	# 適当な要素を枢軸 pivot とし、左から枢軸以上の要素を探し、右から枢軸以下の要素を探す。
	# 見つけたらお互いの要素を交換する。探索位置が交差したら分割終了
	def quick_sort(buffer, low, high): # ソートするリスト, 区間の下限値, 区間の上限値
	# リスト buffer の low から high までの区間をソートする
		pivot = buffer[(low + high) / 2] # 区間の中央にあるデータを枢軸とする
		i = low
		j = high
		while True:
			while pivot > buffer[i]: i += 1 
			# 枢軸より小さい間は探索位置を進める = 左から枢軸以上の要素を探す
			while pivot < buffer[j]: j -= 1
			# 右から探す
			if i >= j: break
			# 探索位置 i, j が交差したら終了
			# そうでなければ要素を交換する
			tmp = buffer[i]
			buffer[i] = buffer[j]
			buffer[j] = tmp
			# 交換したあと i, j を更新
			i += 1
			j -= 1
		if low < i - 1: quick_sort(buffer, low, i - 1)
		# 要素が二個以上ある場合、再帰呼び出しを行う
		if high > j + 1: quick_sort(buffer, j + 1, high)

# --- バックトラック法と再起定義 ---
	# 可能性のあるパターンをすべて生成して、条件を満たしているかチェックする
	# 失敗したら元に戻って別の選択肢を選ぶという方法

# --- 順列 permutation ---
	# n 個の順列の総数は n!
	perm = [] # 順列を格納するリスト
	def make_perm(n, m = 0):
		if n == m: print perm
		else:
			for x in range(1, n + 1):
				if x in perm: continue
				perm.append(x)
				make_perm(n, m + 1)
				perm.pop()

# --- バックトラックで8クイーン ---
	# 斜め利き筋のチェック
	def check(n): # n がクイーンの個数
		for y in range(1, n): # ローカル変数 y が列
			if conflict(board[y], y): return False
		return True
	# check() は y 列のクイーンが0からy - 1列までのクイーンと衝突していないか conflict() を呼び出してチェックする
	def conflick(x, y):
		for y1 in range(0, y):
			x1 = board[y1]
			if x1 - y1 == x - y or x1 + y1 == x + y:
				return True
		return False
	# クイーンの解放
	def queen(n, y = 0):
		global count
		if n == y:
			if check(n):
				print board
				count += 1
		else:
			for x in range(0, n):
				if x in board: continue
				board.append(x)
				queen(n, y + 1)
				board.pop()
	# クイーンの高速化
	def queen1(n, y = 0):
		global count
		if n == y:
			print board
			count += 1
		else:
			for x in range(0, n):
				if x in board or conflict(x, y): continue
				board.append(x)
				queen1(n, y + 1)
				board.pop()
	# for ループの中で衝突のチェックを行うことで無駄な順列を生成しないようにする = 枝刈り

# --- 高階関数 ---
	# 関数を引数として受け取る関数のこと
	# マッピング(引数の関数 func() にリストの要素を渡して呼び出し、結果をリストに格納して返す関数)
	def mapcar(func, list):
		new_list = []
		for x in list:
			new_list.append(func(x))
		return new_list
	>>> def square(x): return x * x
	>>> mapcar(square, [1, 2, 3])
	[1, 4, 9]
	# この機能は map() も持ってる

# --- filter() reduce() ---
	# filter() リストの要素に func() を適用し、 func() が真を返す要素をリストに格納して返す
	# 関数が真を返す要素を削除する関数 remove_if()
	def remove_if(func, ls):
		new_list = []
		for x in ls:
			if not func(x): new_list.append(x)
		return new_list
	# reduce() は func(x) が偽ならば x に加える

# --- ラムダ形式 lambda form ---
	# 高階関数を使うようになると square() のような小さな関数を定義するのがメンドくなる
	# ラムダ形式は名前の無い関数を生成するもの
	>>> func = lambda x, y: x + y
	>>> func(1, 2)
	3
	# キーワード lambda で始まり、そのあと引数を指定し、コロンの後ろに実行する式を定義
	# リストの要素を二乗する処理は、次のように実現できる
	>>> mapcar(lambda x: x * x, [1, 2, 3])
	[1, 4, 9]
	# ラムダ形式は高階関数と組み合わせると便利

# --- レキシカルスコープ lexical scope ---
	>>> def foo(): print x
	>>> x = 10
	>>> foo()
	10
	# この場合もちろん x はグローバル変数の値。ではこれは?
	>>> def foo1():
		x = 100
		foo()
	>>> foo1()
	10
	# この場合もグローバル変数。 foo1() で定義したローカル変数 x は foo() からアクセスできない
	# foo1() で定義したローカル変数は foo1() の中でのみ有効
	# レキシカル(文脈上)の有効範囲

# --- ラムダ形式とローカル変数 ---
	# リストの要素を n 倍する
	def times_element(n, ls):
		return map(lambda x: x * n, ls)
	# ラムダ形式の仮引数は x だけだが、 n は time_element の引数 n をアクセスする
	# リストに格納された文字列のなかで a から始まる文字列を削除する関数
	def remove_string(a, ls):
		return filter(lambda x: c != x[0], ls)

# --- 関数のネスト ---
	# 関数の中で別の関数を定義できる。関数のネスト(入れ子)
	# ネストの関数は局所的な関数なので、定義された関数の中でのみ有効
	# 関数を引数として渡す場合簡単な処理ならラムダ形式だけど、ラムダ形式は式を一つしか定義できない
	# times_element() リストの要素を n 倍する関数をネスト使って書き直す
	def times_element(n, ls):
		def timesN(x):
			return n * x
		return map(timesN, ls)
	# ただしネスト内から外側の関数のローカル変数は書き換えられん

# --- クロージャ closure ---
	# 関数を生成する関数。評価する関数と参照可能なローカル変数をまとめたもの
	# 引数を n 倍する関数を生成する関数
	>>> def foo(n): return lambda x: n * x # foo() は引数を n 倍する関数を生成
	>>> foo10 = foo(10) # foo10 に foo(10) の返り値をセット
	>>> foo10(100) # すると foo10 は引数を10倍する関数になる
	1000
	>>> foo5 = foo(5)
	>>> foo5(11)
	55
	# 参照可能なローカル変数は foo() の引数 n 。
	# そしてクロージャを実行するときは保存されているローカル変数を参照することができる
	# foo(10) を実行して無名関数を生成するとき、定義されているローカル変数は n で、その値は10
	# その値がクロージャに保存されているので foo5 の関数は引数を5倍した結果を返す
	# カリー化関数
	def mapcar(func):
		def _mapcar(ls):
			result = []
			for x in ls:
				result.append(func(x))
			return result
		return _mapcar
	# mapcar() を1引数の関数に直したもの。



