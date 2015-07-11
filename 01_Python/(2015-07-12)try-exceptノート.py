# coding: utf-8

# --- とりあえず try-except 構文の基本 ---
print('処理開始')
try:
    print('try開始')
    a = 10 / 0 # エラーを発生させるための0除算
    print('try終了')
except:
    print('エラー終了')
print('処理終了')
# ああ、エラーが発生した時点で except の方に飛ぶのか。


# --- Exception クラスを指定(?) ---
print('処理開始')
try:
    print('try開始')
    a = 10 / 0 # エラーを発生させるための0除算
    print('try終了')
except Exception as e:
    print('=== エラー内容 ===')
    print('type:' + str(type(e)))
    print('args:' + str(e.args))
    print('message:' + e.message)
    print('e自身:' + str(e))
print('処理終了')
# なんかテキストとは違うエラーが出てよくわかんないんだけど、とりま type:<class 'ZeroDivisionError'> とかいう文が出る。


# --- 存在しないファイルを開く ---
print('処理開始')
try:
    print('try開始')
    f = open('not_exist_file', 'r') # 存在しないファイルを開く
    print('try終了')
except Exception as e:
    print('=== エラー内容 ===')
    print('type:' + str(type(e)))
    print('args:' + str(e.args))
    print('message:' + e.message)
    print('e自身:' + str(e))
print('処理終了')
# とりま type:<class 'FileNotFoundError'> とかいう文が出る


# --- 発生した処理によって処理を分岐(表示メッセージを変更) ---
print('処理開始')
try:
    print('try開始')
    a = 10 / 0
    # f = open('not_exist_file', 'r')
    print('try終了')
except ZeroDivisionError:
    print('テメェ0で除算しやがったな?')
except IOError:
    print('無ェファイルを開こうとすんな。')
print('処理終了')
# キレイに「0で除算しやがったな?」が出る。
# これクソ便利じゃねーかｗｗ


# --- なおエラーの種類は()で括ってもよい ---
print('処理開始')
try:
    print('try開始')
    a = 10 / 0
    # f = open('not_exist_file', 'r')
    print('try終了')
except (ZeroDivisionError, IOError):
    print('テメェ0除算か、無ェファイルを開こうとしやがったな?')
print('処理終了')
# キレイに表示されるよ。


# --- else finally ---
print('処理開始')
try:
    print('try開始')
    a = 10 / 0
    print('try終了')
except (ZeroDivisionError, IOError):
    print('テメェ0除算したな')
else:
    print('else に来たよ')
finally:
    print('finally に来たよ')
print('処理終了')
# else には行かない。つまり
# else: エラーが起こらなかったら実行, finally: どっちにしろ実行。


# --- 予期しないエラーの発生 ---
print('処理開始')
try:
    print('try開始')
    a = int('string') # 予期しないエラー発生
    print('try終了')
except ZeroDivisionError:
    print('テメェ0除算したな')
else:
    print('else に来たよ')
finally:
    print('finally に来たよ')
print('処理終了')
# finally だけが実行され、スタックトレースが出る。


# --- まとめ ---
print('処理開始')
try:
    print('try開始')
    a = int('string') # エラー発生
    print('try終了')
except Exception as e:
    print('type:' + str(type(e)))
print('処理終了')
# こんな風にしとけばエラーの内容、 except になんて書けばいいのかわかっていいね!






