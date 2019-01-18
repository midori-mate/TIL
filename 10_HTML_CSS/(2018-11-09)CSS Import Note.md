CSS Import Note
===

理想的なCSSの読み込み方をめざすぞ。

## 候補

- CSS の import で読む
```css
/* CSS側 */
@import url('common.css');
@import url('button.css');
@import url('header.css');
@import url('footer.css');
```

- HTML の link で読む
```html
<!-- HTML側 -->
<link rel='stylesheet' href='css/common.css' type='text/css' />
<link rel='stylesheet' href='css/button.css' type='text/css' />
<link rel='stylesheet' href='css/header.css' type='text/css' />
<link rel='stylesheet' href='css/footer.css' type='text/css' />
```

- SCSS で読む(何それって疑問はもっともなので後述)
```css
/* CSS側 */
@import "common";
@import "button";
@import "header";
@import "footer";
```

## 計測

| 候補        | サイズ      | 時間      |
| ----------- | --------- | --------- |
| CSS import  | でかい      | おせえ     |
| HTML link   | ちょっとでかい | そこそこ速い |
| SCSS import | 小さい      | 速い      |

## つまり

SCSS 最強。

## で何それ

### 概要

```
普通のCSSファイル -- (コンパイル) --> SCSSファイル
コンパイルされたファイルだからサイズが小さくて読み込みが速いのはもっともだね!
```

### つくりかた

- まず Ruby が必要
    - [RubyInstaller](https://rubyinstaller.org/downloads/)
    - 左ペインの `WITH DEVKIT` のやつでいい。
    - インストールするときに **Rubyの実行ファイルへ環境PATHを設定する** チェックするように。
    - 英語だったら **Add Ruby executable to your PATH**
- 次に Sass ソフトが必要。
    1. cmd 開く。
    2. `gem install sass` 打つ。
    3. インストール完了。

