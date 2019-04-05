
"""VatNote Value-added tax note 消費税ノート


大事なとこ

- 税抜合計に消費税をかけるのと、税込を合計するのでは、違うときがある。
- 小数点以下をいじらなければ同じ。
- 切り捨てて計算すると税抜合計のほうが高くなる。
    - 金額ではなく商品数に比例して、差は大きくなる。
- 四捨五入で計算しても差が出る。ただし切り捨てに比べると誤差レベル。

商品個数 差の平均
   2     0.4
   5     1.9
  10     4.3
  20     9.1
  30    14.0
  50    23.5
  70    33.1
  90    42.5
 100    47.7
 500   239.3
1000   479.6

"""

from random import randint
from decimal import Decimal
from math import floor


# 消費税
VAT = Decimal('1.08')

# 平均値
def GetAvr(itr):
    lis = list(itr)
    return sum(lis) / len(lis)

# 商品ランダム生成
def CreateRandomPrices(price_range, goods_num):
    nums = [ Decimal(str(randint(price_range[0],price_range[1]))) for i in range(goods_num) ]
    taxed_num = [ i * VAT for i in nums ]
    return nums, taxed_num

# 消費税計算を共通化。
def CalcVat(nums, taxed_num, func=None):
    if func is None:
        func = lambda _: _
    _1 = func(sum(nums) * VAT)
    _2 = sum(map(func, taxed_num))
    return (_1, _2, _1-_2)


# 1~1000円の商品を100個生成して、会計1回と会計100回での支払い金額差を算出。
nums, taxed_num = CreateRandomPrices((1,1000), 100)
print( '小数点以下いじらず計算:', CalcVat(nums, taxed_num) )
print( '小数点以下切り捨て計算:', CalcVat(nums, taxed_num, floor) )
print( '小数点以下四捨五入計算:', CalcVat(nums, taxed_num, round) )


# 商品個数ごとの誤差平均値を算出。
GOODS_NUMS = [2, 5, 10, 20, 30, 50, 70, 90, 100, 500, 1000]
for goods_num in GOODS_NUMS:
    # 500パターンほどランダムで商品生成して平均を出そう。
    results_floor = []
    results_round = []
    for i in range(500):
        nums, taxed_num = CreateRandomPrices((1,1000), goods_num)
        results_floor.append( Decimal(str(CalcVat(nums, taxed_num, floor)[2])) )
        results_round.append( Decimal(str(CalcVat(nums, taxed_num, round)[2])) )
    print( f'切り捨て  商品個数{goods_num}  平均価格差{GetAvr(results_floor)}' )
    print( f'四捨五入  商品個数{goods_num}  平均価格差{GetAvr(results_round)}' )
