#!/usr/bin/env python
# coding: utf-8

'''exe化ノート

cx_freezeのインストール
    $ pip install cx_freeze
    pipでだめだったら以下のURLからインストーラを。
        https://pypi.python.org/pypi?:action=display&name=cx_Freeze&version=4.3.4
        なんか昔の俺のメモによると、「なんかうまくいかなかったので32bit版を落としたらうまくいった」とあった。

'''


''' ■ 1. コンソールプログラムの場合

1. cx_freezeの実行スクリプトを用意して(下参照)、exe化したいpyの隣におく。
    俺は cx_freeze.py って名前にしてる。
2. $ python cx_freeze.py build
    これでbuildってフォルダの中にexeができる。

'''

# 実行スクリプト。一石二鳥ゲームをexe化したときのもの。
from cx_Freeze import setup, Executable
import begin_set

# いつもの前準備。
begin_set.exec_all(__file__)

exe = Executable(
    script='KillBirds.py',   # 対象スクリプトの名前。
    icon='pythongreen.ico',  # アイコン。
    base=None                # Noneは'Console'といっしょ。
)
setup(executables=[exe])


''' ■ 2. pygameプログラムの場合

1. 実行スクリプト用意。コンソールプログラムとの違いはbaseだけ。
2. $ python cx_freeze.py build
3. 完成物に静的ファイルは含まれてないから、画像とか音楽とかフォントは自分で追加。
4. oggファイルを使用してる場合は、以下3ファイルを追加。
    Python34/Lib/site-packages/pygame内
        libogg.dll
        libvorbis.dll
        libvorbisfile.dll

'''

# 実行スクリプト。DialogFrameをexe化したときのもの。
from cx_Freeze import setup, Executable
import begin_set

# いつもの前準備。
begin_set.exec_all(__file__)

exe = Executable(
    script='DialogFrame.py',  # 対象スクリプトの名前。
    icon='pythongreen.ico',   # アイコン。
    base='Win32GUI' if sys.platform == 'win32' else None
)
setup(executables=[exe])


''' ■ 3. requestsを使ってる場合

1. "C:\Python34\Lib\site-packages\requests\packages\urllib3\util\ssl_.py"
    の290行目あたりに以下の処理を加えないとダメ

    # cx_freezeのためにちょっと追加した部分
    # ca_certsに格納されてるパスにlibrary.zip\requests\っていうパスが入ってるとダメらしいから、それを消す
    # 参考    http://pc.atsuhiro-me.net/entry/2014/05/07/014236
    context = SSLContext(ssl_version)
    context.verify_mode = cert_reqs
    OP_NO_COMPRESSION = 0x20000
    context.options |= OP_NO_COMPRESSION
    ca_certs = ca_certs.replace('library.zip\\requests', '')
    # print('ca_certs: {0}'.format(ca_certs))

2. 実行スクリプト用意。
3. $ python cx_freeze.py build
'''

# 実行スクリプト。CocSkypeBotをexe化したときのもの。
from cx_Freeze import setup, Executable
import requests

exe = Executable(
    script = 'SkypeBot.py',      # ファイル名
    icon   = 'pythongreen.ico',  # アイコン
    base   = None)               # "Console"といっしょ

setup(
    executables = [exe],
    options = {
        "build_exe":
            {'include_files':
                [(requests.certs.where(), 'cacert.pem')]}},
    )
