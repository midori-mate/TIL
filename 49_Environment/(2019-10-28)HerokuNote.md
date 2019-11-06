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

- `--log-file` はログを吐くというオプション。 `-` は stdout を指す。

### Procfile が理解できない

参考: [Procfile format](https://devcenter.heroku.com/articles/procfile#procfile-format)

- `<process type>: <command>` というフォーマットである。
- `gunicorn config.wsgi` とか `gunicorn file_name:app` の部分は gunicorn のコマンド。
- `--log-file` はログを吐くというオプション。 `-` は stdout を指す。

### gunicorn が理解できない

```bash
# Flask の場合。
gunicorn <ファイル名>:<コード内で Flask(...) を格納している変数名>

# Django の場合。
gunicorn <wsgi.py の入ってるディレクトリ名>.<wsgi.py のファイル名(wsgi)>
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
