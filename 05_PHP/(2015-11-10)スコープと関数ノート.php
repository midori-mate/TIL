<?php

/* ===================

スコープと関数のメモ
    グローバル変数 -> グローバルでしか使えないが、$GLOBALS[""]を使えばローカルでも使える
    ローカル変数 -> ローカルでしか使えん

=================== */
header("Content-Type: text/html; charset=utf-8");
$a = "a";
$b = "b";
function foo($b) {
    $c = "c";
    print($GLOBALS["a"] . $b . $c);
}
foo($b);
print($a . $b . $c);
exit;

/* ===================
関数1内の関数2でグローバル変数と関数1のローカル変数を使うことはできるのかな問題
    できない。
    PHPでは関数内関数は意味がない(関数1の外からでも関数1内の関数2を呼べる)
    だから関数1内の変数はふつーによその関数として扱われる
=================== */

$foo = 1;
$func1 =
function($bar) {
    # グローバル変数はこんなふうにローカルで使うこともできる
    GLOBAL $foo;
    return function() use($foo, $bar) { return $foo + $bar; };
    $baz = 2;
    function bb() {
    }
};

