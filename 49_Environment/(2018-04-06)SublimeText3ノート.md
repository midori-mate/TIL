SublimeText3Note SublimeNote SublimeTextNote
===

## 80ドル

- 設定、パッケージ、ビルドシステムを Chrome のように常時同期できるようになったら。 -> sync settings で OK!
- windows10 で日本語入力の小窓がインラインになったら。 -> 2019-03-14 OK!
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
| Opt(Alt) + - (てかこれは変えてる)         | カーソル位置を前の場所へ                             |
| Opt(Alt) + Shift + - (てかこれは変えてる) | カーソル位置を前の場所へ                             |


## 場合別 tips

#### 01. C#のビルド

C#.sublime-build

```javascript
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

#### 02. OmniMarkupPreviewer でブラウザプレビューしようとしたら404になる問題

基本設定 > Package Settings > OmniMarkupPreviewer > Settings > User

```json
{
    "renderer_options-MarkdownRenderer": {
        "extensions": ["tables", "fenced_code", "codehilite"]
    }
}
```

#### 03. Mac キーバインディングの設定

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

```javascript
// { "keys": ["super+alt+f"], "command": "show_panel", "args": {"panel": "replace", "reverse": false} },
{ "keys": ["ctrl+h"], "command": "show_panel", "args": {"panel": "replace", "reverse": false} },
```

#### 04. coffee script のシンタックスハイライト

Better CoffeScript をパッケージインストール。ファイルの種類を Better CoffeeScript に合わせる。

#### 05. Table Editor パッケージ

便利だけれど keymap がかなり被るから設定しとけ。

```bash
# keymap のユーザ設定ファイルを作成。
# NOTE: User フォルダ内の Default-TableEditor (OSX).sublime-keymap の ln をユーザ設定ファイルとする。
$ mkdir -p "/Users/midori/Library/Application Support/Sublime Text 3/Packages/Table Editor"
$ ln -s "/Users/midori/Library/Application Support/Sublime Text 3/Packages/User/Default-TableEditor (OSX).sublime-keymap" "/Users/midori/Library/Application Support/Sublime Text 3/Packages/Table Editor/Default (OSX).sublime-keymap"
```

使う key だけ設定。

|            command             |      keys      |
|--------------------------------|----------------|
| table_editor_next_field        | super+right    |
| table_editor_previous_field    | super+left     |
| table_editor_next_row          | ctrl+enter     |
| table_editor_csv_to_table      | ctrl+s         |
| その他 ctrl+s が入っているやつ | コメントアウト |

#### 06. つーかショートカットがかぶるのマジ面倒くさいんだけど

かぶること自体は防げないが、かぶったあと「何がかぶってんのか」をサクッと見れるパッケージがこれ。

#### FindKeyConflicts

コマンドパレットから `All Conflicts` で一覧が見れる。

#### 07. シンタックス・セットのショートカット

コマンドパレットから `Set Syntax` であとはわかるだろう。

#### 08. 謎現象、ショートカットが効かない

「ライセンス買え」が出ているせいかもしれない。今回は `Ctrl+K,Ctrl+U` が効かなかった。

#### 09. GoToAnything パッケージ

左サイドバーに置いているファイルの中からファイル名で検索。 

|     ShortCut     | Meaning  |
|------------------|----------|
| Ctrl,Command + p | File     |
| Ctrl,Command + r | Function |
| Ctrl,Command + ; | Variable |

#### 10. Win のフォントはどうする?

[Myrica](https://nelog.jp/myrica)

なんか `Ricty` はバッククォートがカス。等幅じゃないしさー。

#### マルチカーソルのWin,Mac差が面倒なのでこの際統一

こうする。

- Win: Ctrl+Alt
- Mac: Command+Ctrl

Mac のほうはもともと `swap_line_up` `swap_line_down` があったのでそれは無効化した。(行移動)

#### HTML の整形

HTMLPrettify

#### Ctrl + k のカタカナが死んでる

これは適切なユーザキーバインドの設定で解決した。 **Default (OSX).sublime-keymap** は Default のフォルダに置かないとダメ。もしかしたら sync settings で同期されるのは User フォルダだけかもなので、シンボリックリンクを張る。

```bash
ln -s "path/to/Packages/User/Default (OSX).sublime-keymap" "path/to/Packages/Default/Default (OSX).sublime-keymap"
```

#### Sync Settings

https://packagecontrol.io/packages/Sync%20Settings

