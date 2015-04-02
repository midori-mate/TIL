# coding: utf-8
# コメント
# 変数(データにつけるラベル)
# データ型
# 数値
# 真偽値 True False
#　None
# 関数・オブジェクト
# 要素が並んだもの
# - 文字列 : 文字が並んだもの
# - リスト : データが並んだもの
# - タブル : データが並んだもの(変更ができない)
# - セット : データが並んだもの(重複を許さない)
# - 辞書 : キーと値がペア

msg = "hey python how can i start?"
print msg

---2---

# 数値
# 整数、少数、複素数

# 演算子 + - * / // % **
print 10 * 5 # 50
print 10 // 3 # 3
print 10 % 3 # 1
print 2 ** 3 # 8

# 整数と小数の演算 -> 少数
print 5 + 2.0 # 7.0

# 整数同士の割り算
print 10 / 3	
print 10 / 3.0

---3---

# 文字列
# 日本語は u をつける u"よう元気かい"

# + *
print "hello " + "world"
print u"無駄!" * 10

# エスケープ \n 改行 \t タブ \\ バックスラッシュ自身 \' 'をそのまま表示
print "hello\n wo\trld\\ it\'s a pen" 

# """で囲うとそのまま表示される。
print """<html lang="ja"><body></body></html>"""

---4---

# 文字列 len 文字数を教えてくれる
# 検索 find 文字列のなかで、指定したものが何番目かどうか教えてくれる。1文字目が0としてカウントされることに注意。存在しない文字を find させると -1 を返す。
# 切り出し [] (数)番目の文字を切り出す。　[start:end]

s = "abcdefghi"
print len(s)
print s.find("c")
print s[2]
print s[2:5]
# : は ~ みたいに考えてよさそう
# end の方は含まないので、書かないと本当に最後まで、 6 だと 5 まで。
print s[2:]
print s[:2]
# -1 は一番最後の文字を示す。下の場合は「最後の文字を含まない」なので 2 番目から最後から 2 番目になる。
print s[2:-1]

---5---

# 数値と文字列の相互変換
# 数値 <> 文字列

# 文字列 -> 数値 int(整数) float(少数)
# 数値 -> 文字列 str 文字列なのに数字状態で + したらオカシイ。

# print 5 + "5" 他の言語はこれでいいけどpythonエラーが出る
print 5 + int("5") # 整数
print 5 + float("5") # 小数

age = 25
print "i am " + str(age) + " years old!"

---6---

# リスト(他言語では配列とか)
sales = [255, 100, 353, 400] # 文字列を入れてもオッケーよ。
# len + * []
print len(sales) # 4
print sales[2] # 353
sales[2] = 100 # 2のところを100に変更
print sales[2] #100
# in 存在チェック
print 100 in sales # True
# range リストを一気に作る
print range(10) # 0から9まで
print range(3, 10, 2) # 2個トバしで3から10まで。3 5 7 9
print range(3, 10, 1)

---7---

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

---8---

# タプル 基本的にはリストと同じだけど変更ができない
a = (2, 5, 8)
# len 要素数、 + * [] 変更ができないのは要素の中身
print len(a) # 3
print a * 3
# a[2] = 10 8を10に、とかは変更不可能
# タプルをリストにする
b = list(a)
print b
c = tuple(b)
print c

---9---

# セット(集合型と呼ぶ) - 重複を許さない

a = set([1, 2, 3, 4, 3, 2])
# 重複した 3, 2 は表示されない
print a
b = set([3, 4, 5])

# - 差集合
print a - b # a にあって b にない1,2が出る
# | 和集合 ぜんぶ
print a | b
# & 積集合 両方にあるもの
print a & b
# ^ どちらかにしかないもの
print a ^ b

---10---

# 辞書 key と value がペあになったもの。
# [2505, 523, 500] それぞれが誰の売上か知りたい
sales = {"midori":200, "weruda":300, "imoten":500} # {}で囲まれたものを key っていうっぽい。数字が value か。
print sales # 必ずしもそのままの順番で表示されはしない
print sales["midori"]
sales["weruda"] = 800
print sales # werudaの value が800になってる
# in 存在チェック
print "imoten" in sales # True
# keys, values, items
print sales.keys() # key の一覧
print sales.values() # value の一覧
print sales.items() # 中身の一覧

---11---

# 文字列にデータを組み込もう
a = 10
b = 1.234234
c = "midori" # 文字列
d = {"weruda":200, "imoten":500}
print "age: %d" % a # %d は整数
print "age: %10d" % a # ケタ数
print "age: %010d" % a # ケタ数を0で表示
print "price: %f" % b # %f は少数
print "price: %.2f" % b # 小数点以下二桁まで表示
print "name: %s" % c # %s は文字列
print "sales: %(weruda)d" % d # werudaの value を sales の次に出す
print "%d and %f" % (a, b)

---12---

# 出た if 文だ
# 比較演算子 > < >= <= == 等しいときは = じゃなくて == !=
# 論理演算子 and or not
score = 70
if score > 60:
	print "ok!"
	print "OK!"
if score > 60 and score < 80:
	print "good!"

score = 45
if score > 60:
	print "ok!"
elif score > 40: # else 文よりうしろにおいたらエラーが出ました
	print "soso..." 
else: # それ以外
	print "ng!"

# if else 文のちょっと変わった書き方
print "okay!" if score > 60 else "no!"

---13---

# for　文によるループ処理
sales = [13, 3525, 31, 238]
for sale in sales: # sales から一個とりだして sale にいれて下の処理をしろって意味
	print sale # それぞれが表示される

sales = [1, 2, 4, 6]
sum = 0
for sale in sales:
	sum += sale # sum = sum + sale のこと
else: # ループが終わったら
	print sum

# ただ単純に0-9まで出したい
for i in range(10):
	print i
# continue break
for j in range(10):
	if j == 3:
		break # ここに continue 打つと3だけ抜かして9まで。
	print j

---14---

# 辞書型のデータで for ループ
users = {"ten":200, "wada":300, "will":500}
# 全部表示させたい
for key, value in users.iteritems(): # iteration は反復
	print "key: %s value: %d" % (key, value)
# key だけ表示したい
for key in users.iterkeys():
	print key
for value in users.itervalues():
	print value

---15---

# while 文でループ
n = 0
while n < 10:
	print n
	# n = n + 1
	n += 1
else:
	print "end."

# continue とか break も使えます
m = 0
while m < 5:
	if m == 3:
		m += 1 # ここに入れないと無限ループに入る。 ctrl + C で強制ストップできる。
		continue # もし m が3なら、+1してコンティニュー。
	print m
	m += 1
else:
	print "end."

---16---

# 関数　複数の処理をまとめて
def hello():
	print "hello"
hello()

# 引数
def fuck_you(name, a = 3):
	print "fuck you %s!" % name * a # * を使うと繰り返し
fuck_you("Tom", 2)
fuck_you("Steve") # def の方に数字がかいてあれば、こっちに書かない場合その数値が適用される。

# 返り値 関数に値を返してもらいたい
def asshole(name, a = 3): # コロンを忘れちゃダメ! 忘れると下の色文字が白くなります
	return "asshole %s!" % name * a
s = asshole("Steve") # 関数に格納できる
print s

# 変数のスコープ 有効範囲みたいなもん
name = "midori"
def ce_faci():
	name = "weruda"
print name
# 部分プログラム内の関数は外では関係ない

# pass
def ce_faci2():
	pass # 何も処理しないという意味

---17---

# リスト <> 関数 map リストの要素に関数を適応させる命令 map
def double(x): 
	return x * x # 二乗したものを返す
print map(double, [2, 5, 8])

# 無名関数 上のものを一行で書きたい場合。
print map(lambda x:x * x, [2, 5, 8])

---18---

# オブジェクト(変数と関数をまとめて管理したい)
# 用語 概念的なものだけど
# クラス: オブジェクトの設計図
# インスタンス: クラスを実体化したもの
class User(object): # ユーザークラスってのを作ります
	def __init__(self, name): # インスタンス化されるときに呼ばれる関数
		self.name = name # selfはユーザーオブジェクト自身
	def greet(self): # ふつうの関数
		print "my name is %s!" % self.name

bob = User("Bob") # インスタンスを作る
tom = User("Tom") 
print bob.name
bob.greet()
tom.greet()
# HAHAHA 突然わかんなくなったぜ。

# クラスの継承
class SuperUser(User):
	def shout(self):
		print "%s is SUPER!" % self.name
tom = SuperUser("Tom")
tom.greet()
tom.shout()
# クラスを継承してオブジェクトを作っていく。いや、よくわからん。

---19---

# モジュールの使い方
# 公式 -> ドキュメンテーション -> Global Module なんちゃら
import math, random #モジュールを呼び出す 複数なら , で区切る
print math.ceil(5.2) #切り上げをしてくれるので6
for i in range(5):
	print random.random()

from datetime import date # おっきなモジュールdatetime、日付に関するものだけdate
print date.today()