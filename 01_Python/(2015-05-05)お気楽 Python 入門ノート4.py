# http://www.geocities.jp/m_hiroi/light/index.html#python_abc
# ここの情報ノート

# --- モジュール ---
	import sys, string

# --- 文字列の検索メソッド find, index, count ---
	S.find(sub) # 部分文字列 sub の位置を返す。見つからなければ - 1
	S.index(sub) # sub の位置を返す。見つからなければ ValueError
	S.count(sub) # sub の出現回数を返す
	# どのメソッドも引数に start, end を指定できる

# --- 文字の除去 strip ---
	S.strip() # 先頭と末尾の文字を除去
	S.rstrip() # 末尾の文字
	S.lstrip() # 先頭の文字
	# 例
	>>> a = ' hello, world \n'
	>>> a.strip()
	'hello, world' # 引数を省略すると改行文字の前のスペースも削除する

# --- 文字列の分解と結合 split, join ---
	S.split() # 文字列に含まれる単語をリストに格納
	join(list) # リストに格納されている文字列を連結
	>>> a = 'foo bar baz'
	>>> print a.split()
	['foo', 'bar', 'baz']
	>>> print string.join(a.split(), '\t')
	'foo\tbar\tbaz'
	# 英単語の数を数える関数
	def word_count():
		c = 0
		for x in sys.stdin: # 標準入力 sys.stdin から一行ずつ読み込む
			c += len(x.split())
		print c

# --- 文字列の置換 replace, maketrans, translate, lower, upper ---
	>>> a.replace('foo', 'FOO', 2) # 文字列 a の foo をふたつ FOO に変える
	>>> b = string.maketrans('xyz', 'XYZ') # 変換テーブルを作成
	>>> c = 'a b c x y z'
	>>> c.translate(b) # 'a b c X Y Z'
	a.lower() # 全部小文字にする
	a.upper() # 全部大文字にする

# --- 正規表現 ---
	| # 前後の正規表現どちらかと一致
	* # 直前の正規表現の0回以上の繰り返しに一致
	+ # 1回以上の繰り返しに一致
	? # 0,1回一致
	{m,n} # m 回以上 n 回以下の繰り返し
	*? # 0回以上の繰り返しに最短一致
	+? # 1回以上の繰り返しに最短一致
	?? # 0,1回最短一致
	{m,n}? # m 回以上 n 回以下の繰り返し 最短一致
	[] # カッコ内の文字のどれかと一致
	[^] # カッコ内の文字でない場合に一致
	. # 任意の一文字に一致
	^ # 行頭と一致
	$ # 行末と一致
	() # 正規表現をグループにまとめる

# --- 正規表現の使い方 match, search ---
	# Python で正規表現を利用する場合はモジュール re をインポート
	match(pattern, string [, flag])
	search(pattern, string [, flag])
	# pattern が正規表現で、 flag が正規表現の動作指定
	# マッチングに成功した場合はマッチオブジェクト Match Object を返す。失敗したら None
	group() # 正規表現と一致した文字列を返す」
	start() # 一致した文字列の開始位置を返す
	end() # 一致した文字列の終了位置を返す
	span() # 一致した文字列の位置をタプルで返す
	# --- 例 ---
	>>> import re
	>>> a = re.search(r'\d+', 'abcd0123efgh')
	>>> a.group()
	'0123'
	>>> a.start(), a.end()
	(4, 8)
	>>> a.span()
	(4, 8)
	>>> b = re.match(r'\d+', 'abcd0123efgh')
	>>> print b
	None


