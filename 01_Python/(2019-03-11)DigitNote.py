
"""桁切り抜きノート DigitNote

・ 整数の下n桁を切り抜く。
・ 整数の上n桁を切り抜く。
"""

import math


def split_last_digit(target, n):
    """下n桁。"""
    return target % (10**n)


def split_first_digit(target, n):
    """上n桁。"""
    # target の桁数。
    digitnum_of_target = get_number_of_digit(target)
    # targetの桁数 - 求められている桁数 = 切除する桁数(>=0)
    digitnum_unnecessary = (digitnum_of_target-n) if (digitnum_of_target-n)>=0 else 0
    return target // (10**digitnum_unnecessary)


def get_number_of_digit(num):
    """桁数を取得。"""
    num = -num if num < 0 else num
    return int(math.log10(num)) + 1


if __name__ == '__main__':
    # 下n桁。
    print( split_last_digit(123456789, 0) )   # 0
    print( split_last_digit(123456789, 5) )   # 56789
    print( split_last_digit(123456789, 15) )  # 123456789

    # 上n桁。
    print( split_first_digit(123456789, 0) )  # 0
    print( split_first_digit(123456789, 5) )  # 12345
    print( split_first_digit(123456789, 15) ) # 123456789

"""以下、参考
数学の原理
step1:  x = a*10^n, where n is integer and 1 =< a < 10
step2:  log10(x) = log10(a*10^n)
        Because log10(p*q) = log10(p)+log10(q) ,
        log10(x) = log10(a)+log10(10^n).
        Because the bases of log10(k) and k=10^m are the same,that is 10,
        log10(10^m) = m.
        Therefore, log10(x) = log10(a)+log10(10^n) = log10(a)+n.
        Here n+1 is the number of digits.
"""
def get_number_of_digits( num: float ) -> int:
    IsNegative = False
    if num < 0:
        num *= -1
        IsNegative = True
    n = int(math.log10(num))
    # a = math.log10(num) - n ## a is required here so it is commented in.
    return n+1 ## 1 is the number of digits of a so the result will be n+1

"""参考その2
友達が作ってくれた、小数点を含めた桁切り抜き関数。
"""
def get_transferred_number( num: float, digits: int ):
    IsNegative = False
    if num < 0: num *= -1; IsNegative = True
    n = int(math.log10(num))
    result = 0
    if type(num) == float:
        if digits > n+1:
            factor = 10**digits if num < 1 else 10**(digits-(n+1))
            result = int(num*factor)/factor
        else:
            result = num // 10**(digits-(n+1))
            if n+1 == digits: result = int(result)
    else:
        result = num // 10**(n+1-digits)
    if IsNegative: result *= -1
    return result

if __name__ == '__main__':
    cases = [
        12345678,     # 123
        123456789999, # 123
        -123456789,   # -123
        123.456,      # 123
        0.13255,      # 0.132
        12.3456,      # 12.3
    ]
    digits = 3
    for case in cases:
        print(get_transferred_number( case, digits ))
