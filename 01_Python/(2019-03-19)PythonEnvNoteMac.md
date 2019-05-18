Python Environment Note For Mac PythonEnvNoteMac
===

pyenv, pyenv-virtualenv のノートだよ。


## いつもこのノートを開くときみたいコマンドはこれ

```bash
# 今なんだっけ?
pyenv versions

# 他の環境に変えよっと。
pyenv global VERSION

# 新しい環境ほしいな。
pyenv install --list
pyenv install VERSION
pyenv virtualenv VERSION NEW_NAME

# 新しい環境作ったらこれ、ね。
pip install --upgrade pip
```


## 何ができる?

- python, anaconda 含むいろんなバージョンのｐｙてょんをターミナル上でインストール、切り替えができる。
- 切り替えたら python コマンドで実行できる。
- だから Sublime では何もいじらなくていい。


## 前提

- xcode
- homebrew


## pyenv, pyenv-virtualenv をインストール

```bash
brew install pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```


## .bash_profile に追記

```
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

オマケ .bash_profile の更新コマンド。

```
source ~/.bash_profile
```


## pyenv コマンド

```
pyenv install --list               インストールできるもの一覧。
pyenv install VERSION              インストールする。
pyenv virtualenv VERSION NEW_NAME  VERSIONのさらに下の区分を作成。
pyenv versions                     いまインストールしてあるもの一覧。
pyenv global VERSION               バージョン切り替え(全体)。
pyenv local VERSION                バージョン切り替え(カレントディレクトリ)。
pyenv uninstall NAME               環境を削除。
```


## venv で環境変えるとターミナルのプロンプトに環境名が出て目障り問題

[https://blog.shibayu36.org/entry/2017/04/01/145758](https://blog.shibayu36.org/entry/2017/04/01/145758)
