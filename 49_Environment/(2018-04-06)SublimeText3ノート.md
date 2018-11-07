# SublimeText3ノート

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

#### CSV整形

CSVを選択し、 `Ctrl+k Shift+\`

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

#### markdown内のTableを整形

`Table Editor: Enable for current syntax`  
`Table Editor: Set table syntax 'Simple' for current view`

をやった上で、表のなかで tab 押せば整形できるらしいけどキーバインドが競合してできない。キーバインドはとにかく面倒くさいから今はやらない。
