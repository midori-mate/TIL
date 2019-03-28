
"""VatNote Value-added tax note 消費税ノート


大事なとこ

- 税抜を合計して消費税をかけるのと、税込を合計するのでは、違うときがある。
- しっかり小数点以下も計算すれば、同じになる。
- 小数点以下切り捨てをすると、税抜を合計して税を乗せたほうが高くなる。
    - これは金額ではなく商品数に比例する。
    - ざっくりいって10個だと5、100個だと50、1000個だと500の誤差が出る。
- 四捨五入をすると、まちまち。だけど同じになることはない。
    - これは金額や商品数にはまったく関係なく、10くらいの誤差が出る感じ?

これを見てまず思うのは「レジに何回も並んだほうがお得じゃん」。
だけどネットの記事では「1円程度にセコセコするなんて…」という意見が多かった。
でも「いや1円程度の差じゃないよ?!」と思った。
だから金額と商品数でどんだけ変わるのか集計してみる。

商品個数   2 の平均値: 0.4372
商品個数   5 の平均値: 1.8387999999999998
商品個数  10 の平均値: 4.191199999999999
商品個数  20 の平均値: 8.8464
商品個数  30 の平均値: 13.482400000000002
商品個数  40 の平均値: 18.260399999999997
商品個数  50 の平均値: 22.7892
商品個数  60 の平均値: 27.470800000000004
商品個数  70 の平均値: 32.146
商品個数  80 の平均値: 36.9016
商品個数  90 の平均値: 41.4928
商品個数 100 の平均値: 46.254

1円程度の差じゃないよ!!
商品数5個をべつべつにお会計すれば2円も得するし、100個をべつべつにお会計したら46円もお得だよ!
す い ま せ ん 常 識 の 範 囲 内 で は 1円 程 度 の 差 で す ね !!!

金額範囲 (1, 9)       の平均値: 18.069166666666664
金額範囲 (10, 99)     の平均値: 22.424166666666665
金額範囲 (100, 999)   の平均値: 21.790000000000003
金額範囲 (1000, 4999) の平均値: 21.819
金額範囲 (5000, 9999) の平均値: 21.77716666666667

金額範囲はどの範囲でも差がないことがわかる。
"""

from random import randint
from decimal import Decimal
from math import floor

# 消費税
VAT = Decimal('1.08')

# 数値をランダムに用意。参考までに表示。
NUMS       = [Decimal(str(randint(1,1000))) for i in range(100)]
TAXED_NUMS = [num*VAT for num in NUMS]
# print(NUMS      )
# print(TAXED_NUMS)

### 小数点以下を無視しない ###
総計に消費税 = sum(NUMS) * VAT
個別に消費税 = sum(TAXED_NUMS)
print(総計に消費税)
print(個別に消費税)

### 切り捨てる ###
総計に消費税かけて切り捨て = floor(総計に消費税)
個別に消費税かけて切り捨ててから合計 = sum(map(floor, TAXED_NUMS))
print(総計に消費税かけて切り捨て          )  # こっちのほうが高くなる
print(個別に消費税かけて切り捨ててから合計)  #
print(総計に消費税かけて切り捨て-個別に消費税かけて切り捨ててから合計)  # 差額

### 四捨五入 ###
総計に消費税かけて四捨五入             = round( 総計に消費税 )          # 四捨五入の場合、まちまち。
個別に消費税かけて四捨五入してから合計 = sum( map(round, TAXED_NUMS) )  # 
print(総計に消費税かけて四捨五入            )
print(個別に消費税かけて四捨五入してから合計)
print(総計に消費税かけて四捨五入-個別に消費税かけて四捨五入してから合計)  # 差額


#
# 以下、金額と商品数でどんだけ変わるのかの集計すくりぷと。
# numpy スタイルの docstring をちょっと試してみたよ。
#


def GetAvr(lis):
    """
    平均値を出します。

    Parameters
    ----------
    lis : list
        リスト。

    Returns
    -------
    results : Decimal
        計算結果
    """
    return sum(lis) / len(lis)


def GetTwoPatternsFloor(price_range, goods_num):
    """
    商品をランダムに生成して2パターンの消費税計算をします。

    Parameters
    ----------
    num_range : tuple
        生成する商品金額の範囲。
    goods_num : int
        生成する商品の個数。

    Returns
    -------
    results : tuple
        ( 税抜を合計して消費税をかけたもの, 税込を合計したもの, 差額 )
    """
    VAT = Decimal('1.08')
    nums = [ Decimal(str(randint(price_range[0],price_range[1]))) for i in range(goods_num) ]
    taxed_num = [ i * VAT for i in nums ]
    _1 = floor(sum(nums) * VAT)
    _2 = sum(map(floor, taxed_num))
    return (_1, _2, _1-_2)


results_goods_num   = { i:[] for i in [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] }
results_price_range = { t:[] for t in [(1,9), (10,99), (100,999), (1000,4999), (5000,9999)] }

for goods_num in results_goods_num.keys():
    for price_range in results_price_range.keys():
        # 何回もやって平均を出す。
        results = [ GetTwoPatternsFloor(price_range, goods_num)[2] for i in range(500) ]
        avr = GetAvr(results)
        # あとで金額範囲、商品個数ごとの平均値を出す。
        results_goods_num[goods_num].append( avr )
        results_price_range[price_range].append( avr )

for goods_num,results in results_goods_num.items():
    print( f'商品個数 {goods_num} の平均値: {GetAvr(results)}' )
for price_range,results in results_price_range.items():
    print( f'金額範囲 {price_range} の平均値: {GetAvr(results)}' )
