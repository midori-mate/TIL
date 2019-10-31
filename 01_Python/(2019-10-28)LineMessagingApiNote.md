LineMessagingApiNote
===

どこもかしこもわかりづらいサイトばっかりだった。ちゃんとまとめる。


## LINE Developers でチャネルを作成

この作業をしているとき「Line Developers」と「Line Official Account Manager」がややこしい。どちらにも「チャネル」に相当するものがあるから。今回使うのは Developers のほう。

- Line Developers: [https://developers.line.biz/](https://developers.line.biz/)
- Line Official Account Manager: [https://manager.line.biz/](https://manager.line.biz/)

そして「チャネル」「プロバイダ」あたりの用語もややこしい。チャネルはプロバイダの子要素にあたる。ひとつのプロバイダに対し複数のチャネルを作成できる。チャネルが LINE の対話相手になる。

![](media/line01.jpg)

![](media/line02.jpg)

![](media/line03.jpg)

![](media/line04.jpg)

![](media/line05.jpg)

![](media/line06.jpg)

![](media/line07.jpg)

![](media/line08.jpg)

![](media/line09.jpg)

![](media/line10.jpg)


## Python スクリプト作成

ぼくの場合、 pipenv を使うのでこんなふうに環境を準備。

```bash
pipenv install flask line-bot-sdk gunicorn
pipenv shell
```

Python スクリプトは my_flask_script.py って名前にしてみた。ベースのコードは [line-bot-sdk のドキュメント](https://github.com/line/line-bot-sdk-python#synopsis)から取得し、そこへ手を加えた。

```python
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# 環境変数取得のため。
import os

# ログを出力するため。
import logging
import sys

app = Flask(__name__)

# ログを標準出力へ。heroku logs --tail で確認するため。
# app.logger.info で出力するため、レベルは INFO にする。
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

# 大事な情報は環境変数から取得。
CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']
CHANNEL_SECRET = os.environ['CHANNEL_SECRET']

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route('/')
def top_page():
    return 'Here is root page.'


@app.route('/callback', methods=['POST'])
def callback_post():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def reply_message(event):
    # reply のテスト。
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='こちらこーるばっく処理からお送りします:'+event.message.text))


if __name__ == '__main__':
    app.run()
```


## Heroku 用ファイル作成

```bash
# runtime.txt: Python のバージョンを記載。
echo python-3.7.4 > runtime.txt

# requirements.txt: 依存ライブラリの記載。
pip freeze > requirements.txt

# Procfile: プログラムの実行方法を記載。
echo web: gunicorn my_flask_script:app --log-file - > Procfile
```

Procfile は `web: python my_flask_script.py` ではなぜだか動かなかった。


## Heroku へアップ

```bash
# Git リポジトリ作成。
git init
# 個人的な趣味で、最初に空っぽのコミットを作成。
git commit --allow-empty -m "Initial Commit"
# 全ファイルをコミット。
git add --all
git commit -m "Add all files"

# 今回のアプリ名は line-messaging-py-py-py にしてみる。
heroku create line-messaging-py-py-py

# 環境変数を設定。
heroku config:set CHANNEL_ACCESS_TOKEN="チャネル基本設定のページからアクセストークン（ロングターム）をコピーしてくる" --app line-messaging-py-py-py
heroku config:set CHANNEL_SECRET="チャネル基本設定のページから Channel Secret をコピーしてくる" --app line-messaging-py-py-py

# Heroku のリポジトリへアップ。
git push heroku master

# 途中でなにか失敗したら一度消す。
heroku apps:destroy --app line-messaging-py-py-py
```

トップページのメソッドも作ってあるので開いてみる。

![](media/line11.jpg)


## URL をチャネルへ登録

チャネル基本設定のページで Webhook URL を登録し、 Webhook送信 を有効にする。上の Python スクリプトで、 callback を受け付ける URL は `/callback` にしたので、今回の Webhook URL は `https://line-messaging-py-py-py.herokuapp.com/callback` になる。

![](media/line12.jpg)


## 使う

チャネル基本設定のページの下の方に QR コードがあるので、そこからこのチャネルを友達登録する。

![](media/line13.jpg)

![](media/line14.jpg)

![](media/line15.jpg)

Python で書いたコールバック処理を通過してメッセージが返されたことがわかる。いまはチャネルの設定がデフォルトなので色々自動返信されちゃっているけれど、それはのちのち編集したらいい。


## event と userId の内容

my_flask_script.py では、 `app.logger.info` によって、このスクリプトへ送られてきた情報を出力している。 `heroku logs --tail` で確認できる。

```json
{
    "events": [
        {
            "type": "message",
            "replyToken": "********************************",
            "source": {
                "userId": "*********************************",
                "type": "user"
            },
            "timestamp": 1572247838104,
            "message": {
                "type": "text",
                "id": "**************",
                "text": "foo bar baz"
            }
        }
    ],
    "destination": "*********************************"
}
```

この中の `userId` はあとで push_message に使いたいので、控えておく。コード内で取得したい場合、以下のように取得する。

```python
event.source.user_id
```


## push_message を使う

上で書いた Python スクリプトだけでは、返事しかできない。そうではなく、サーバ側から能動的にメッセージを送れるようにしたいところ。もちろんこれは Heroku にアップする必要はなく、ローカルから試せる。

```python
from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = '上で使った CHANNEL_ACCESS_TOKEN と同じ'
USER_ID = '上で控えた userId の値'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

line_bot_api.push_message(
    USER_ID,
    TextSendMessage(text='ぷっしゅめっせーじです。やあ!'))
```

![](media/line16.jpg)

このとおり、ユーザごとにユニークである `user_id` を保存しておきさえすればサーバ側からいつでもメッセージを送付することができることがわかる。


---
