# coding: utf-8

'''チョー便利 requestsモジュールノート RequestsNote
pip install requests
'''

import requests

# ==================
# 基本的な使い方
# ==================
# 単純なやつ
res = requests.get(url)
# セッション使うやつ
session = requests.session()
session.post(url, logindata)
# ヘッダだけくれ
res = requests.head(url)
# ヘッダ偽造
res = session.post(url, data=postdata, headers=headers)
# 取得
h = res.headers      # ヘッダ
e = res.encoding     # エンコーディング
t = res.text         # 本文
s = res.status_code  # ステータスコード

# sessionを確立してサイトにログインして暴れまわる術
url = 'なんかログインしてログインクッキーをもらうサイトのURL/login'
postdata = {
    'username': '...',
    'password': '...',
}
session = requests.session()
session.post(url, postdata)    # ログイン状態のセッションが完成
url = 'たとえばCSVダウンロードページのURL'
postdata = {
    'request': 'csv',
}
headers = {
    # ヘッダはこう送る
    'Accept'           :'application/json, text/javascript',
    'Accept-Encoding'  :'gzip, deflate',
    'Accept-Language'  :'ja,en-US;q=0.8,en;q=0.6',
    'BehaviorOverride' :'redirectAs404',
    'Cache-Control'    :'no-cache, no-store, must-revalidate',
    'ClientInfo'       :'os=Windows; osVer=7; proc=Win32; lcid=en-us; deviceType=1; country=n/a; clientName=skype.com; clientVer=908/1.42.0.98//skype.com',
    'Connection'       :'keep-alive',
    'ContextId'        :'tcid=146372019467711519',
    'Content-Type'     :'application/json',
    'Expires'          :'0',
    'Host'             :'client-s.gateway.messenger.live.com',
    'Origin'           :'https://web.skype.com',
    'Pragma'           :'no-cache',
    'Referer'          :'https://web.skype.com/ja/',
    'User-Agent'       :'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'RegistrationToken':'exampleexample',
}
res = session.post(url, data=postdata, headers=headers)
encoding = res.encoding                 # デフォルトではISO-8859-1になってるかもしれん。すっと文字化けするから下行で直す。
res.encoding = 'Shift_JIS'
res.encoding = res.apparent_encoding    # 本文を読んで文字コードを自動判別してくれるからこれでも。
# (おまけ)URLエンコード
import urllib.parse
example = urllib.parse.unquote(res.headers['Content-Disposition'])
# 本文の取得方法
text = res.text

''' cx_freezeとrequests
"C:\Python34\Lib\site-packages\requests\packages\urllib3\util\ssl_.py"
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
'''
import sys
from cx_Freeze import setup, Executable
import requests

exe = Executable(
    script = 'skypeBot.py',   # ファイル名
    icon   = 'python.ico',     # アイコン
    base   = None)             # "Console"といっしょ

setup(
    name        = 'MyPython',
    version     = '1.0',
    description = 'application',
    executables = [exe],
    options     = {"build_exe":{'include_files':[(requests.certs.where(), 'cacert.pem')]}},
    )
# python cx_freeze.py build で実行

