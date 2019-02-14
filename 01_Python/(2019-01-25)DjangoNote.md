DjangoNote
===


## 作成から heroku デプロイまで。

[DjangoFloare](https://gitlab.com/midori-mate/djangofloare)に以下のとおりの手順でコミットしてある。


### 作成

```
下準備
    mkdir DjangoFloare
    cd DjangoFloare/
    gitignore 追加
    https://github.com/jpadilla/django-project-template/blob/master/.gitignore

Initialize Django
    django-admin startproject config .
    こうするとイチイチフォルダ名を config にしなくていい。

Add static folders
    ベストプラクティスに従って static を配置。

Add templates folders
    ベストプラクティスに従って templates を配置。

Add app1,2
    python manage.py startapp app1
    python manage.py startapp app2
    ベストプラクティスに従って app1 app2 追加。

Deal with static, templates
    settings.py に static と templates を扱う設定を追加。

Add apps to setting
    settings.py に app1,app2 を追加。

Create models
    models.py にモデルを追加。画像も追加したいけどシンプルにしたいからまたあとで。
    python manage.py makemigrations
    python manage.py migrate

Add models to admin
    admin.py にモデルを追加。admin ページから見れるようになる。

スーパーユーザ作っとく
    python manage.py createsuperuser

ここらで runserver してみる。
    python manage.py runserver
    localhost:8000

admin にいくつか登録してみる
    localhost:8000/admin/

Create top page
    トップページ作成。

Create floare page
    個別ページ作成。

Set timezone
    忘れてたタイムゾーン。

何のトガったところもない django ができあがった。heroku へ入る。
```

### heroku デプロイ

```
Create heroku files
    echo 'web: gunicorn config.wsgi --log-file -' > Procfile
    pip install gunicorn django-heroku
    pip freeze > requirements.txt
    echo 'python-3.6.3' > runtime.txt
    settings 修正
        https://www.miniwebtool.com/django-secret-key-generator/

heroku ci
    heroku login
    heroku create django-floare
    git push heroku master
    heroku ps:scale web=1
    heroku run python manage.py migrate
    heroku run python manage.py createsuperuser
    heroku open

問題: heroku push heroku master でエラー。
    failed to push some refs to 'https://git.heroku.com/django-floare.git'
    これを実行。
        heroku config:set DISABLE_COLLECTSTATIC=1
    OK

問題: 開くとエラー。
    relation "app1_floare" does not exist
    は? migrate したじゃん。ls してみたら sqlite3 がないからマジで heroku では posgre が疲れてるんかなー。
    ずっと半信半疑だった、「migrations ファイルは git add するもんなのか問題」にカタがついたみたいだ。絶対 add すること。
    そして heroku ci の中に makemigrations はいらない。ローカルで作って、リモートで migrate する。

片付け
    heroku apps:destroy --app django-floare
```


## 基礎

### INSERT

```python
# ひとつ
Tbl(field1='...', field2='...').save()

# 複数 save いらねーのよ
Tbl.objects.bulk_create([
    Tbl(field1='...', field2='...'),
    Tbl(field1='...', field2='...'),
])
```

### UPDATE

```python
t = Tbl.objects.filter(field1='...').first()
t.field2 = '...'
t.save()
```

### GETSERT

取得、さもなくばINSERT。こんなんあるんだ一度もやろうと思ったことないけど。

```python
tbl, created = Tbl.objects.get_or_create(
    field1='...',      # これで検索かける。
    defaults={
        field2:'...',  # これをINSERTする。field1は書かなくていいよ。
    },
)
```

### UPSERT

これは欲しいだろー。

```python
tbl, created = Tbl.objects.get_or_create(
    field1='...',      # これで検索かける。
    defaults={
        field2:'...',  # これでUPDATEかける。
    },
)
```


## 場合別

### POSTを飛ばすと CSRF verification failed. エラーが出る。

原因

- setting.py で CsrfViewMiddleware を追加してるのに csrf_token が form に追加されてないとこうなる。

解法

- 解法: フォームの中に `{% csrf_token %}` を追加すればよい。


### DEBUG = False にすると static が読み込まれない。

原因

- `True`=(開発中) のときだけ django の機能 `django.contrib.staticfiles` を使ってサーバ経由で静的ファイルを表示してるから。
- `False`=(本番) のときはApache等のWebサーバを利用する。
    - 本番環境では**runserver コマンドは利用しない。**マジで?!
    - そして `collectstatic` を使ってWebサーバが見れるとこに static を移動させてくれるそうだ。

だがこのへんのことは今はサクサク進めたいからやらん。本当に必要になったとき調べ直す。  
ひとまず `DEBUG=True` で進める。404テストをしたいときだけ `False` にする。

- [Django での static files の扱い方まとめ](http://hideharaaws.hatenablog.com/entry/2014/12/12/230825)


### 404 ページを作りたいんだが。

テンプレートディレクトリに `404.html` を追加する。  
`DEBUG=False` のときだけ表示される。


### 画像を格納するDBがほしい。

ImageField の使い方

- [Django の ImageField](https://qiita.com/kojionilk/items/da20c732642ee7377a78)

(サイズバリエーション自動作成)ImageKit を使うやつ

- [DjangoでImageFieldからサムネイルをImageKitで自動生成する](https://qiita.com/felyce/items/57421ea191ab89175e9e)

(サイズバリエーション自動作成)StdImageField を使うやつ

- [Django2で画像を指定サイズで保存する](https://qiita.com/peijipe/items/68292ded4fd3e31a8bfe)


### DatetimeField を取得するとき None になるんだが。

原因

- このとき手動でDBに `yyyy-mm-dd` なんつー文字列を入れてた。

解法

- sqlite では `%Y-%m-%d %H:%M:%S.000000` のフォーマットで登録すること。
- 参考: `datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.000000')`


### テンプレート内でディクショナリとかリストのインデックスに変数が使えない。

```html
{% for i,l in enumerate_lis %}
    {{lis.i}}
    {{dic.i}}  どっちも何も表示されない!! まじくそ。最初からこれくらいサポートしておけ。
{% endfor %}
```

解法

```python
# まずテンプレートタグを作成する。
# manager/templatetags/template_utils.py
from django import template
from django.template.defaulttags import register

@register.filter
def ref_lis(lis, arg):
    return lis[int(arg)]

@register.filter
def ref_dic(dic, arg):
    if arg not in dic:
        raise KeyError(f'Dictionary doesn\'t have key: {arg}')
    return dic[arg]
```

```python
# settings に追記する。
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
            ],
            # これを追記するよ。
            'libraries': {
                'lookup': 'manager.templatetags.template_utils',
            },
        },
    },
]
```

```html
<!-- 使いたいテンプレートのてっぺんで読み込む。 -->
{% load template_utils %}

<!-- こう使う。 -->
{% for i,l in enumerate_lis %}
    {{lis|ref_lis:i}}
    {{dic|ref_dic:i}}
{% endfor %}
```
