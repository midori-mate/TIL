DjangoNote
===


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
