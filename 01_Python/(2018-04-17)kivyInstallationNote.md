
# kivy インストールノート

## コンソール

```bash
$ pip install --upgrade pip    # pip の更新
$ pip install cython pygame    # 下のも合わせて依存モジュール
$ pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer
$ pip install kivy             # これは依存モジュール入れ終わってからやらないとダメ。
$ pip uninstall kivy           # もし kivy install 後に依存モジュール入れたならこれで入れ直すこと。
```

## テスト用スクリプト

これ実行して画面が出たら、インストール成功!

```python
import kivy

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text='Hello world')

MyApp().run()
```

## kviewer(kvファイルリアルタイムプレビュア) の準備

kviewer.py の一部を書き換える。

ぼくの環境では `/Users/user/.pyenv/versions/3.6.0/lib/python3.6/site-packages/kivy/tools/kviewer.py` だったよ。


```python
except Exception as e:
    Window.add_widget(Label(text=e.message if e.message else str(e)))
# この部分を↓のに書き換え。
```

```python
# 3.6 だと message が存在しないためエラー落ちする。回避のため書き換え。
except Exception as e:
    Window.add_widget(Label(text=(
        e.message if getattr(e, r'message', None) else str(e)
    )))
```

実行はこのコマンド。

```bash
$ python -m kivy.tools.kviewer ./***.kv  # ./をつけないとダメみたい。
```

## Sublime Text3 パッケージ

```
Kivy Language
```
