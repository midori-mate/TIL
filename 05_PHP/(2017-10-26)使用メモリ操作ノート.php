<?php

echo '最初の段階 ' . memory_get_usage(true) . PHP_EOL;

# メモリ上限の変更。25Mにすると下記エラーが起こるので興味があったら変更してみてね。
#     Fatal error: Allowed memory size of 26214400 bytes exhausted
#     10k件の二次元配列を作ると50Mくらいになるからオーバーする。
ini_set('memory_limit', '256M');

define('LIMIT', 100000);
$a = array();
for ($i=0; $i < LIMIT; $i++) {
    $a[] = array(
        't_den_no' => 'S1000000',
    );
}

echo LIMIT . '件の配列作った直後 ' . memory_get_usage(true) . PHP_EOL;

echo '現在php.iniで割り当てられてるメモリはphpinfoのmemory_limitを見てね。' . PHP_EOL;
