<?php

$data = array(
    "array"     => array("a", "b", "c")
    );

/* ********************
serialize()
******************** */
$data = serialize($data);
# "a:1:{s:5:"array";a:3:{i:0;s:1:"a";i:1;s:1:"b";i:2;s:1:"c";}}"
# 型、大きさ、値を保持して文字列にする。
$data = unserialize($data);
# 配列に戻す。

/* ********************
var_export()
******************** */
$data = var_export($data, true);
/*
"array (
  'array' => 
  array (
    0 => 'a',
    1 => 'b',
    2 => 'c',
  ),
)"
そのまんま文字列にする。変数に代入するときは第二引数をtrueにする。
*/
$data = eval("return $data;");
# 戻すときはeval()。

/* ********************
json_encode()
******************** */
$data = json_encode($data);
# "{"array":["a","b","c"]}"
# JSON形式の文字列に変換。
$data = json_decode($data, true);
# 配列に戻す。trueを指定しないと、戻り値がstdClassになっちまう。


var_dump($data);


