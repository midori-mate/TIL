<?php

# 日付ノート。

# 昨日、今日、明日
print_r([
    'yesterday' => date('Y-m-d H:i:s', strtotime('-1 day')),
    'today'     => date('Y-m-d'),
    'tomorrow'  => date('Y-m-d', strtotime('+1 day')),
]);

# タイムスタンプ
print_r([
    'yesterday'  => strtotime(date('Y-m-d', strtotime('-1 day'))),
    'today'      => strtotime(date('Y-m-d')),
    '2016/09/01' => strtotime(date('Y-m-d', strtotime('2016/09/01'))),
]);

# xml形式の日付
print_r([
    'today' => date('D, d M Y H:i:s O', strtotime(date('Y-m-d'))),
]);

# 一日分の秒数(86400)
echo 1474902000 - 1474815600;


# わざあり!!!!!!!!!!!!!!!!!!!!!!!
# nヶ月前
function perfectLastMonth($n)
{
    return strtotime(date('Y-m-1') . "-$n month");
}
# それを日付形式に。
echo date('Y年m月', perfectLastMonth());


# わざあり!!!!!!!!!!!!!!!!!!!!!!!
# 今月からn年n月までの配列作成。
function ymList($to)
{
    $i = 0;
    $to = strtotime($to);
    while (true) {
        $cursor = strtotime(date('Y-m-1') . "-$i month");
        $a[date('Y-m', $cursor)] = date('Y年m月', $cursor);
        if ($cursor <= $to) {
            break;
        }
        $i++;
    }
}
print_r(ymList('2018-01-01'));

