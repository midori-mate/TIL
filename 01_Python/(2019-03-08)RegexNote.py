
"""Regex Note 正規表現ノート regexnote 

全部おぼえんのはムリやけー実際に使ったやつをメモってく感じで……。
"""

import re


# 置換しちまう。
print( re.sub(r'AB.*?BC', 'AC', 'AAAAABBBBBCCCCC') )  # AAAAACCCCC

# 抜き出す。
print( re.findall(r'AB.*?BC|Ab.*bC', 'ABBBBBCAbbbbbC') )  # ['ABBBBBC', 'AbbbbbC']

# HTMLタグ系の正規表現。
r'<span>*/span>|<SPAN .*?/SPAN>'
r'<td[\s\S]*?/td>|<TD[\s\S]*?/TD>'  # 改行を含めたいとき。
