
"""ProgressBarNote TqdmNote

$ pip install tqdm

・ https://github.com/tqdm/tqdm

tqdm はアラビア語の progress らしいよ。
"""


import time
import tqdm


# 基本
# 100%|███████████████████████████████▉| 456/456
for i in tqdm.trange(456):
    time.sleep(0.01)


# オプションマシマシ。
# OptionMashiMashi:  91%|########################################################5     | 456/500
for i in tqdm.trange(
        456,
        total=500,                # この場合 456/500 でゲージが止まるよ。
        ascii=True,               # バーが # になるよ。
        desc='OptionMashiMashi',  # 説明。
        leave=True,               # False にすると処理が終わったときバーが消えるよ。
        ):
    time.sleep(0.01)


# 手動でバーを進める。
# 100%|███████████████████████████████████████████████████████████████████████████| 10000/10000
with tqdm.tqdm(total=5000) as pbar:
    for i in range(5000):
        time.sleep(0.0001)
        pbar.update(1)


# ネストの場合……。
# なんか windows10 だとキャリッジリターンが効いてない感じだった。
for i in tqdm.trange(4, desc='1st loop'):
    for j in tqdm.trange(5, desc='2nd loop'):
        for k in tqdm.trange(50, desc='3nd loop', leave=False):
            time.sleep(0.01)
