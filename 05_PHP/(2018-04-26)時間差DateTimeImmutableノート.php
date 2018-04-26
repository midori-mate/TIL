<?php

# 時間差ノート。

# 期限まで1時間だよ!
$now        = '2018-04-26 12:00:00';
$expiration = '2018-05-27 13:00:00';

# DateTimeImmutable 化します。
$now        = new DateTimeImmutable($now);
$expiration = new DateTimeImmutable($expiration);

# 現在に比べて期限がどれだけ先かを求めます。
$margin = $now->diff($expiration);

print_r($margin);
# DateInterval Object
# (
#     [y] => 0
#     [m] => 0
#     [d] => 0
#     [h] => 1  時間差1時間!
#     [i] => 0
#     [s] => 0
#     [f] => 0
#     [weekday] => 0
#     [weekday_behavior] => 0
#     [first_last_day_of] => 0
#     [invert] => 0  # これが1だと、diff対象が過去(期限超過)ということになる。
#     [days] => 0
#     [special_type] => 0
#     [special_amount] => 0
#     [have_weekday_relative] => 0
#     [have_special_relative] => 0
# )

# フォーマット方法。
echo PHP_EOL . $margin->format('時間差: %h %i %s') . PHP_EOL;
echo PHP_EOL . $margin->format('時間差プラマイつき: %R%h %R%i %R%s') . PHP_EOL;

# 日を全部時間に変換したい場合。
$hours = $margin->days * 24 + $margin->h;
echo PHP_EOL . $margin->format("日を時間に変換した場合: %R$hours %R%i %R%s") . PHP_EOL;
