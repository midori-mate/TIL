HerokuNote
===

わりと頻繁にコマンドを調べちゃうから、ノートとしてまとめておく。

## 必要ファイル

- runtime.txt(Pythonのバージョンを記載)
- requirements.txt(依存するライブラリの記載)
- Procfile(プログラムの実行方法を定義)

コマンド。

```bash
# runtime.txt
python -V
# Python 3.7.4
echo python-3.7.4 > runtime.txt

# requirements.txt
pip freeze > requirements.txt

# Procfile - Django の場合
echo web: gunicorn config.wsgi --log-file - > Procfile
# Procfile - Flask の場合
echo web: gunicorn ここに python で実行するファイル名:app --log-file - > Procfile
```

## Heroku コマンド

```bash
# 作成
heroku create アプリ名

# 環境変数
heroku config:set SLACK_WEBHOOK_URL="https://hooks.slack.com/services/***"

# 削除
heroku apps:destroy --app アプリ名
```
