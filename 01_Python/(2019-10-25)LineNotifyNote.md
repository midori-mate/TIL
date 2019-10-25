LineNotifyNote
===

## 下準備

LINE アプリでの準備。

- LINE アプリ > ホーム > 左上の歯車 > アカウント
    - ログイン許可にチェック
    - パスワードを登録

LINE Notify トークンの発行。

- [LINE Notify](https://notify-bot.line.me/ja/)にログイン
- マイページ > トークンを発行する


## Python

```python
import requests

TOKEN = '上で発行した43桁のトークン'

requests.post(
    'https://notify-api.line.me/api/notify',
    headers={'Authorization': f'Bearer {TOKEN}'},
    data={'message': '事故が発生しました\nType: Warning\nLocation: Strada României'},
    files={'imageFile': open('./crush.jpg', 'rb')},
)
```


## PHP

```php
<?php

$TOKEN = '上で発行した43桁のトークン';

$payload = http_build_query(['message' => "事故が発生しました\nType: Warning\nLocation: Strada României"], '', '&');
$context = stream_context_create([
    'http' => [
        'method' => 'POST',
        'header' => "Authorization: Bearer $TOKEN\n"
                . "Content-Type: application/x-www-form-urlencoded\n"
                . 'Content-Length: ' . strlen($payload) . "\n",
        'content' => $payload,
    ]
]);
file_get_contents(
    'https://notify-api.line.me/api/notify',
    false,
    $context,
);
```
