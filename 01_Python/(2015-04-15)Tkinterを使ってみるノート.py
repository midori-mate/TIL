# coding: utf-8
# 参考: http://qiita.com/nnahito/items/ad1428a30738b3d93762

# --- 基本形式 ---
	import sys
	import Tkinter
	root = Tkinter.Tk()
	root.title(u'title') # タイトルバー
	root.geometry('400x300') # ウィンドウサイズ
	root.mainloop()
	# 400 * 300 px のウィンドウが出来る。
	# ソフトウェアの実行内容は Tkinter.Tk() と root.mainloop() のあいだに記述

# --- Label ---
	static1 = Tkinter.Label(text = u'test')	# 変数に格納
	static1.pack() # ウィジェットに格納
	# 任意の場所に配置したい場合は、
	static1.place(x = 3, y = 3) # って感じ
	# オプションの追加は、
	(text = u'test', foreground = 'color', background = 'color') # こんな感じ

# --- Entry ---
	editbox = Tkinter.Entry(width = 50)
	editbox.insert(Tkinter.END,'mojiretsu') # 最初から文字を入力しておく場合
	editbox.pack()

# --- Entry の中身を取得削除 ---
	# .get() を使う
	value = editbox.get() # 変数 value に entry の中身が入る
	# .delete(0, Tkinter.END) を使う

# --- Button ---
	button = Tkinter.Button(text = u'smt', width = 50)
	button.pack() # あるいは button.place(x = foo, y = bar)

# --- Button を押すと何か処理を ---
	def DeleteEntryValue(event):
		editbox.delete(0, Tkinter.END)
	button = Tkinter.Button(text = u'delete')
	button.bind('<Button - 1>', DeleteEntryValue)
	# <Button - 1>(左クリック)されると関数を呼び出す
	button.pack()

