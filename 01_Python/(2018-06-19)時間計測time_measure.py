#!/usr/bin/env python
# coding: utf-8

# 処理時間計測スクリプト。

import time

start = time.time()
# ================================
# 処理、ここから。



time.sleep(2)



# 処理、ここまで。
# ================================
margin = time.time() - start
print(f'結果: {margin}秒')
