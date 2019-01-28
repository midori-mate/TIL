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


