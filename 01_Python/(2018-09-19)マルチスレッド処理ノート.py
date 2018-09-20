
'''マルチスレッド処理ノート

■ マルチプロセス
メモリ領域を新たにつくる。

■ マルチスレッド
親プロセスの中にすべてのスレッドが存在していることになる。専用のメモリ領域は用意されない。
この状況で動作しても問題が発生しないことをスレッドセーフという。

(2018-09-19)ふたつの使い分けはまだよくわからん。
ただ ThreadPoolExecutor と ProcessPoolExecutor を書き換えればそれだけで変わるぞ。便利。

やりたいこと
    1. ふたつの関数を同時に実行したい。どっちも時間かかるから並列で動かしたいわけ。
    2. そのふたつが終わったときはじめて実行したい関数がある。

ついでに
    マルチスレッド処理が終わるのを待たない場合も。
'''

import time
import concurrent.futures

# 下のbarと同時に実行したい!
def foo(x):
    print(f'foo starts. {x}')
    time.sleep(3)
    print('foo ends up.')
    return 'foo return value'

# 上のfooと同時に実行したい!
def bar(x):
    print(f'bar starts. {x}')
    time.sleep(1)
    print('bar is running.')
    time.sleep(1)
    print('bar is running.')
    time.sleep(1)
    print('bar is running.')
    time.sleep(1)
    print('bar ends up.')
    return 'bar return value'

# どちらも終了したときに発生させたい!
def baz():
    print('both processes ended up.')


if __name__ == '__main__':

    # ためしにかかる時間をはかってみよう。
    print('=================')
    start = time.time()

    # max_workers で指定したものより多くのタスクを要求すると、タスクはキューに追加されて他のタスクの終了を待って順次実行される。
    # ええやん。
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:  # マルチスレッドにしたいならこれ。
    # with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:  # マルチプロセスにしたいならこれ。

        # executorにタスクをsubmitし、同数だけfutureオブジェクトを得る。
        # わざわざYEAHとかやってんのは引数の渡し方を示したいだけ。
        futures = [executor.submit(func, 'YEAH') for func in [bar, foo]]

        # 各futureの完了を待ち、結果を取得。
        # こっちは終わった順に拾う。だからfooのほうが先に返ってくる。
        for future in concurrent.futures.as_completed(futures):
            # 各関数の戻り値。
            print(future.result())

        # ↑のやつは「終わったやつから拾う」
        # こっちは呼び出し順に拾う。だからbarのほうが時間かかるのに先に返ってくる。
        # (done, notdone) = concurrent.futures.wait(futures)
        # for future in futures:
        #     print(future.result())

        # すべてのタスクの完了を待ち、あとしまつ。
        # as_completedを使ってるからこの時点ですべて終わってるはず。
        executor.shutdown()

    # 時間計測結果!
    margin = time.time() - start
    print(f'結果: {margin}秒')

    # fooもbarも終わったときはじめて実行させたいやつ。
    baz()


# ================================================
# マルチスレッド処理が終わるのを待たない場合も。
# ================================================

# 待たないのでこっちは時間が測れん。
print('=================')

# 引数max_workersのデフォルトは、現在のCPUの限界値。
executor = concurrent.futures.ThreadPoolExecutor()
# executor = concurrent.futures.ProcessPoolExecutor()
executor.submit(foo, '待たない場合!')
executor.submit(bar, '待たない場合!')
baz()
