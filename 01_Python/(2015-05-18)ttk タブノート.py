# coding: utf-8

import Tkinter as t
import ttk

root = t.Tk()
# タブの親
note = ttk.Notebook(root)

# entry = Tk.Entry() みたいなもん
# タブは frame なので Tk.Frame を使う
tab_a = t.Frame(note,height=100,width=100)
tab_b = t.Frame(note,height=100,width=100)
tab_c = t.Frame(note,height=100,width=100)

# あ、 pack() じゃなくて add() を使うってことか
note.add(tab_a, text="Tab_A")
note.add(tab_b, text="Tab_B")
note.add(tab_c, text="Tab_C")

note.pack()

root.mainloop()