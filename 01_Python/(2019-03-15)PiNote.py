
"""PiNote 円周率ノート

Python で求めるのは2通りある。
"""

# math.pi で出る。
import math
print(math.pi)

# よくわからんけど pi は以下の法則で算出できるんだって。
# pi = 4( 1/1 - 1/3 + 1/5 - 1/7 + 1/9 ... )
#    = +4/1 -4/3 + 4/5 -4/7 +4/9 ...
# ↑これを書けばいい。
pi   = 0
sign = +1
for base in range(1, 100, 2):  # +4/1 から -4/99 まで。この数値を上げていくと精度が増す。
    pi += sign * 4 / base
    sign *= -1
print(pi)
