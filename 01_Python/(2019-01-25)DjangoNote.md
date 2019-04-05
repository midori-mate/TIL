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
        - static
            - app1/images/.gitkeep
            - app2/images/.gitkeep
            - css/.gitkeep
            - js/.gitkeep

Add templates folders
    ベストプラクティスに従って templates を配置。
        - templates
            - .gitkeep
            - app1/.gitkeep
            - app2/.gitkeep

Add app1,2
    ベストプラクティスに従って app1 app2 追加。
    python manage.py startapp app1
    python manage.py startapp app2

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

### vagrant デプロイ

heroku は色々大変なのでこちらで先に試す。

```
準備
    Vagrantfile と vagrant-provision を置く。

vagrant 起動
    $ vagrant up

django 起動
    $ vagrant ssh
    $ python3.6 /vagrant/manage.py runserver 0.0.0.0:8000

DEBUG=False のための準備
    MIDDLEWARE の SecurityMiddleware の下に
        'whitenoise.middleware.WhiteNoiseMiddleware',
        追加。
    settings.py の一番下に
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Manually added.
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Manually added.
        追加。
    $ python3.6 /vagrant/manage.py collectstatic
    staticファイルの中に、404があったときはエラーが出るから処理してね。
```

これで DEBUG=False 許容する。


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
tbl, created = Tbl.objects.update_or_create(
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


### テンプレート内で文字列を連結したりする

```
文字 'aaa'+variable+'bbb' を連結して変数 string に格納。
{% with 'aaaa'|add:variable|add:'bbb' as string %}
  作ったものをここで表示
  {{string}}
{% endwith %}
```

### heroku 環境変数操作

```
# みる
heroku config
heroku config:get NAME

# 設定
heroku config:set NAME=VALUE

# 削除
heroku config:unset NAME
```


### adminページで OperationalError エラー

具体的にはこういうエラーが出る。

```
attempt to write a readonly database 
unable to open database file
```

以下のパーミッションを開ける。

- sqlite ファイル自体。
- sqlite のあるディレクトリ(プロジェクト本体である場合が多いかな?)


### django-markdownx で画像アップできない問題

状況

- localhost での markdownx はうまくいく。(admin画面で書いてアップ)
- vagrant 内で apache を通してやると画像アップができない。

エラーログを見てみたらパーミッションエラーだった。

```
PermissionError: [Errno 13] Permission denied: '/vagrant/media/markdownx/ba4befe6-f087-4a81-a953-9581954b490e.png', referer: http://localhost:1992/admin/app1/md/1/change/
```

media/markdownx のパーミッションを開けたら解決。


### Vagrant,Apache,DEBUG=False ではめっちゃ読み込みが遅い

なんなんこれ。


### apache 環境、staticfiles が notfound 言われる。

状況

```
FileNotFoundError: [Errno 2] No such file or directory: '/vagrant/staticfiles/admin/css/widgets.css'
```

解法

- apache 環境で `STATIC_ROOT` は不要。

```
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```


### apache 環境、admin ページのCSSが404。

そりゃそうね、/static/ 下にないんだもの。

解法

- apache 環境では STATIC_ROOT をナシにしていたが、一度有効にする。
- collectstatic すれば /staticfiles/ 下に admin のファイルが現れる。
- それだけパクって /static/ へ移動。staticfiles は消してしまえ。


### ↑をやっても markdownx のcssがない。

ないやつ

- /static/markdownx/admin/css/markdownx.css
- /static/markdownx/js/markdownx.js 


### ↑をやってもエラー

```
Cannot set property 'innerHTML' of null
```

これは、 markdownx のcssを無理やり引き抜いたことで起こったっぽい。さらにいえば admin の引き抜き(collectstatic して出てきたやつを自前の static に移しちまおう)自体がおかしいってことかな? ちゃんと apache で admin 用の css を引き抜く方法を調べよう。

てかようは markdownx 用の static がないってだけ。適切な方法で admin 用の static は抜き出しましょう。

###### ひとつ見つけた。

「apache の Alias で /static/admin/ のURLで admin の static を直接参照させよう。」

```
# 例として書かれてたやつ。
Alias /static/admin/ "/usr/lib/python2.6/site-packages/django/contrib/admin/media"
```

あーなるほどってなった。つまりぼくの環境ではこうなるわけか。

```
# admin 用
Alias /static/admin/ "/Users/username/.pyenv/versions/3.6.3/envs/lab-3.6.3/lib/python3.6/site-packages/django/contrib/admin/static/admin"

# markdownx 用
Alias /static/markdownx/ "/Users/username/.pyenv/versions/3.6.3/envs/lab-3.6.3/lib/python3.6/site-packages/markdownx/static/markdownx"
```

ただしもうひとつのほうが正当そう。

###### もうひとつ見つけた。

ご存知 collectstatic を使って、collect 先に Alias を貼る。

```
# collect 先の例
STATIC_ROOT = "/var/www/static"

# Alias
Alias /static/ /var/www/static
```

だけどこれには疑問。admin はコピーされてたけど markdownx はコピーされてないじゃん。あれ? いまやってみたら staticfiles に現れた。まあよかった。


### ↑のあと DEBUG=False で実行したらcss表示されない

`--insecure` で実行したら表示された。

```
python manage.py runserver --insecure
```

insecure をつけると STATIC_ROOT のほうを見に行ってくれるようになるんかな?

Django の問題で状況を説明するときは

- どの環境(local, vagrant, apache, heroku)で
- どの実行方法(runserver, wsgi)で
- apache なら Alias の設定はどうなってて
- STATIC_ROOT はどこになってるか

らへんを明記しないとダメだなー。あと django1,2 でちょっと違うから注意。


### ↑の作業を終えたあと admin や markdownx のcssは表示されたが MEDIA にアップした画像が404

まあそりゃ apache なら Alias で media のアクセス先を指定できるけど、ローカルではそういうことしてないもんね。そう理解しつつググったら、あったあった。

- [How to serve media file when runserver --insecure?](https://stackoverflow.com/questions/28063089/how-to-serve-media-file-when-runserver-insecure)

ってまて、MEDIAファイルの設定はもう書いてあるよ! なんで?!

この質問はこういうふうに整理し言い換えたほうがいいか。

- 以下の条件下で /media/ のアクセスを任意のフォルダにするにはどうしたらいい?
    - DEBUG=False
    - Apache を使ってない
    - runserver --insecure で実行

うーん、これはできない、というかしないものなのかも。DEBUG=False にするならば runserver 以外のウェブサーバを使いましょうってことか。どうしても static だけでも確認したいときは collectstatic してから insecure しましょうってことかな?


### ふと思った

Django は「ここはよくわかんないなーまあでもやりたいメインのことじゃないし適当にしとくか」ってほかっておいたことがあとになって必ず襲ってくる感じ。
