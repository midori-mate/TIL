# coding: utf-8

from Tkinter import *
# module Tkinter をインポート

root = Tk() # メインウィンドウを作成
button = Button(root, text = 'Python/Tkinter')
# ボタンを創る。Tk では GUI 用の部品を widget と呼ぶ。
# Button() でウィジェットの button を生成
# 引数 text はボタンに表示されるテキスト
button.pack()
# ウィジェットの配置はジオメトリマネージャが行う。3種類あり、 pack() はそのうちひとつ。
root.mainloop()
# メソッドのイベントループ。

# --- Tkinter のウィジェット ---
	#生成は widget = widgetClass(parent, option = value, ...)
	Frame #ウィジェットを格納する枠組み
	Label #文字列やイメージ
	Message #複数行の文字列
	Button #これ
	Radiobutton #ラジオボタン
	Checkbutton #チェックボタン
	Listbox #リストボックス
	Scrollbar #スクロールバー
	Scale #スケール。おい、説明しろよ
	Entry #1行の文字列の入力と編集
	Menu　#メニュー
	Menubutton #そのまんますぎるから説明しねえ
	Bitmap
	Canvas
	Text #テキストの入力・編集
	LabelFrame #ラベル付フレーム
	Spinbox
	PanedWindow

# --- option ---
	foreground(fg) #文字や線の色
	background(bg)
	text #ウィジェット内テキスト
	textvariable #テキストを格納するオブジェクト
	image
	bitmap
	borderwidth(bd) #ウィジェットの枠の幅
	relief #ウィジェットの枠のスタイル
	height
	width
	anchor #ウィジェットや表示されるデータの位置を指定

# --- ボタンをひとつ表示するプログラム ---
	from Tkinter import *
	class App(Frame):
	# フレームウィジェットを表すクラス。 Frame を継承してアプリケーションを表すクラス App を生成。
	# App はフレームを継承しているので、 App() でオブジェクトを生成するとそこにウィジェットを配置できる。
		def init(self):
			button = Button(self, text = 'smt')
			button.pack()
		def __init__(self, master = None):
		# 特殊メソッド __init__() スーパークラス Frame の __init__() を呼び出して初期化に必要な処理。
		# ここでメインウィンドウ生成
			Frame.__init__(self, master)
			self.pack()
			self.init()
	app = App()
	app.mainloop()

# --- エントリー(一行の文字列) ---
	Entry() # よく使うオプションは textvariable
	# エントリーで入力されたデータは指定したオブジェクトに格納
	# show = '*' にすると入力された文字は * と表示される
	# 電卓プログラム
	from Tkinter import *
	root = Tk()
	root.option_add('*font', ('FixedSys', 14))
	buffer = StringVar()
	buffer.set('')
	def calc(event):
		if buffer.get():
			value = eval(buffer.get()) # 関数 eval() は与えられた文字列を python の式とする
			buffer.set(str(value))
	e = Entry(root, textvariable = buffer)
	e.pack()
	e.focus_set()
	e.bind('<Return>', calc)
	root.mainloop()

# --- ボタンとラベル ---
	# よく使われるオプション
	font
	underline
	padx # 水平方向の詰め物
	pady # 垂直方向の詰め物
	command # おした時に実行する関数を指定。 exit() を指定しておけばボタンを押したらアプリケーションを終了
	# 実例
	Button(root, text = 'smt', command = sys.exit)

# --- ジオメトリマネージャ。メソッド三種類 ---
	place() # ウィジェットを指定した座標に配置
	pack() # ウィンドウにウィジェットを詰め込む　ウィジェットの数・大きさによってウィンドウの大きさも変化
	grid() # ウィジェットを格子状に配置
	# 押したボタンの番号をラベルに表示するプログラム
	# まずラベルを定義
	from Tkinter import *
	root = Tk()
	buff = StringVar()
	buff.set('')
	label = Label(root, textvariable = buff) 
	# オプション textvariable にはクラス Variable のオブジェクトを指定
	label.pack()
