Python Environment Note For Windows PythonEnvNoteWindows
===

virtualenvwrapper のノートだよ。


## いつもこのノートを開くときみたいコマンドはこれ

```bash
# いまある環境のリスト。
workon

# 環境を使う。
workon VERSIONNAME
```


## 何ができる?

- cmd上でバージョンを切り替えられる。
- Mac の pyenv, virtualenv みたいにぱそこ全体のバージョンを切り替えられるわけではない。


## 前提

- 欲しいバージョンのPythonは予めインストールしておく。
- [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

例

- `C:\Python37\python.exe`
- `C:\Python34\python.exe`


## 導入

これはPowerShellだとダメ。(workonコマンドはバッチなのでcmdじゃないと動かん。)

```
> pip install virtualenvwrapper-win                         # よく検索に出てくるvirtualenvのもっと便利版。

> python -V
Python 3.7.2                                                # 現在デフォルトのPythonは3.7

> mkvirtualenv 環境名 --python="C:\Python34\python.exe"     # 環境名のとこはMacのvirtualenv的なノリでつける。

> workon 3.4.4

(3.4.4)> python -V                                          # バージョン切り替え完了。
Python 3.4.4

(3.4.4)> deactivate                                         # 終了。
```


## おまけ py コマンドを使う方法

- 複数バージョンは自分でインストーラを落としてインストール。(Mac ならターミナル上で全部できる。)
- 厳密な意味で切り替えができるわけじゃない。`py -3.6 sample.py` `py -3.7 sample.py` みたいにイチイチバージョン指定が必要。
- よって Sublime では切り替えとか面倒くさい。


#### 別バージョンをインストールする

[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

- パスを通さないようにすること。
- パスを通していないためこの段階で `python -V` してもエラーになる。

#### バージョンを指定して実行

```
py -*.* sample.py      *.* の python で sample.py を実行する場合。
py sample.py           バージョンを指定しない場合入ってる最新のバージョンで実行になる。
py -*.* -V             バージョン確認。
```

最初見たときは「py っていうコマンドのバージョンを切り替えられるのかな?」って思ったんだけどできねえ。毎回バージョンを指定する必要がある。クソ。
