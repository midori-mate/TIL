# SublimeText3ノート

## 80ドル

- 設定、パッケージ、ビルドシステムを Chrome のように常時同期できるようになったら。
- windows10 で日本語入力の小窓がインラインになったら。
- windows10 タスクバー右クリックで新しいウィンドウを開けるようになったら。
- windows10 現在開いているファイルをエクスプローラで開けるようになったら。

## ショートカット

基本的なとこはいいとして最近発見したグッドなショトカを書く。

|               ShortCut               |                       Meaning                        |
|--------------------------------------|------------------------------------------------------|
| Opt + Ctrl                           | 上下矢印といっしょに押して画面スクロール             |
| Shift + Ctrl                         | 上下矢印といっしょに複数カーソル                     |
| Command + Ctrl                       | 上下矢印といっしょに行を移動させる                   |
| F12                                  | 関数ジャンプ(同ファイル内か、開いているプロジェクト) |
| Opt + - (てかこれは変えてる)         | カーソル位置を前の場所へ                             |
| Opt + Shift + - (てかこれは変えてる) | カーソル位置を前の場所へ                             |


## 場合別 tips

### 01. C#のビルド

C#.sublime-build

```json
{
    // This build system will build your cs file to exe file and will run it
    "file_regex": "^(...*?)[(]([0-9]*),([0-9]*)[)]",
    // By default csc is not in your PATH, so add it to your path
    // or uncomment "path" and check that it has correct value
    "path": "C:/Windows/Microsoft.NET/Framework/v4.0.30319/",
    "shell": true, // Without this sublime has hard times to parse "&" in out command line
    "selector": "source.cs",

    "windows":
    {
        "cmd": ["del", "${file/\\.cs/\\.exe/}", "2>NUL", "&", "csc", "/nologo", "/out:${file/\\.cs/\\.exe/}", "$file"],
        "encoding": "cp932",
    },

    "variants":
    [
        {
            "name": "Run",
            "windows":
            {
                "cmd": ["del", "${file/\\.cs/\\.exe/}", "2>NUL", "&", "csc", "/nologo", "/out:${file/\\.cs/\\.exe/}", "$file", "&", "${file/\\.cs/\\.exe/}"],
                "encoding": "cp932",
            },
        }
    ]
}
```

### 02. OmniMarkupPreviewer でブラウザプレビューしようとしたら404になる問題

基本設定 > Package Settings > OmniMarkupPreviewer > Settings > User

```json
{
    "renderer_options-MarkdownRenderer": {
        "extensions": ["tables", "fenced_code", "codehilite"]
    }
}
```

### 03. Mac キーバインディングの設定

・ キーバインドファイルをここにコピー。

    Packages/Default/Default (OSX).sublime-keymap

・ 検索欄の「次へ」ショートカットをCtrl+Enterにする。

    // Find panel key bindings
    // Replace panel key bindings
    // Incremental find panel key bindings
    以上のショートカットを enter から ctrl+enter にする。

・ Ctrl+kでカタカナ変換ができるようにする。

    ctrl+k のところをコメントアウト。

・ 置換は Command+opt+f だけど他のとかぶるから変更する。

```json
// { "keys": ["super+alt+f"], "command": "show_panel", "args": {"panel": "replace", "reverse": false} },
{ "keys": ["ctrl+h"], "command": "show_panel", "args": {"panel": "replace", "reverse": false} },
```

### 04. coffee script のシンタックスハイライト

Better CoffeScript をパッケージインストール。ファイルの種類を Better CoffeeScript に合わせる。

### 05. Table Editor パッケージ

CSVを見るためにわざわざ Excel とかいうクソ重ソフトを開いてないか?  Sublimeちゃんでいけるで。

`install > Table Editor`

#### まず

こいつはかなり keymap が他とかぶるから変更したほうがいい。

1. `Sublime Text 3/Packages/Table Editor/Default (OSX).sublime-keymap` 作成。
    - Windows の場合は `Default (Windows).sublime-keymap` ね。
2. 中身は `Preference > Package Settings > Table Editor > Key Bindings - Default` の内容。
    - うまくいかんかったらここにデフォルトのキーマップがおいてある。
        - [https://github.com/vkocubinsky/SublimeTableEditor](https://github.com/vkocubinsky/SublimeTableEditor)

```
# 変更ガイド

# md の table
table_editor_next_field     : 次のセルに移動。デフォルトは tab で動作しない。 super+right とかよさげ。
table_editor_previous_field : 前のセルに移動。 super+left とかよさげ。
table_editor_next_row       : 次の行に移動。とにかく enter から ctrl+enter とかに変える。

# csv の整形
table_editor_csv_to_table   : デフォルトは ctrl+k,| なんだがそれはカタカナ変換だ!!!!! 他のキーに変える。
```

#### CSV整形

コマンドパレットでこれ打ってから

```
Table Editor: Enable for current syntax
```

CSVを選択し `table_editor_csv_to_table` に設定してるショートカット。

```
# これが
a,b,c
1111111111111,1111111111,22222
3sdfasd,asfsdaf,fsafa
```

```
# こうなる
| a             | b          | c     |
| 1111111111111 | 1111111111 | 22222 |
| 3sdfasd       | asfsdaf    | fsafa |
```

#### markdown 内の Table を整形

コマンドパレットでこれ打ってから

```
Table Editor: Enable for current syntax
Table Editor: Set table syntax 'Simple' for current view
```

こういうのを用意して

```
|||
|-
```

この中のどっかで `table_editor_next_field`, `table_editor_previous_field`, `table_editor_next_row` に設定したショートカットを打つ。テーブルの上を Excel のように移動できるぞ。

### 06. つーかショートカットがかぶるのマジ面倒くさいんだけど

かぶること自体は防げないが、かぶったあと「何がかぶってんのか」をサクッと見れるパッケージがこれ。

#### FindKeyConflicts

コマンドパレットから `All Conflicts` で一覧が見れる。

### 07. シンタックス・セットのショートカット

コマンドパレットから `Set Syntax` であとはわかるだろう。
