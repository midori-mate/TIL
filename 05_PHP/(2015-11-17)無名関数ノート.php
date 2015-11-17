<?php

/* =====================
無名関数
===================== */
$foo = 1;
$a =　function($bar) {
    GLOBAL $foo;
    return function() use($foo, $bar) { return $foo + $bar; }; # (A)
};

# データ型を教えてくれる この場合はClosureだよって言う
var_dump($a(1));

# (A)の計算結果を知りたかったら、いちど引数をとった関数をおろしてから
$b = $a(1);
print($b());
# $aと$bは関数が変数にはいってる 関数として実行したいなら()つけないとダメ!

############### useはどう役に立つか
$foo = "GLOBAL";
function a() {
    $foo = "A";
    return b();
}
function b() {
    global $foo;
    return $foo;
}
echo a(); // GLOBAL
// 通常の関数ではglobalキーワードを使ってグローバル変数にアクセスするしかない

$foo = "GLOBAL"; # グローバル変数fooにGLOBAL代入
$a = function () {
    $foo = "A"; # ローカル変数fooにA代入
    $b = function () use ($foo) { # 一階層下のfooをuseするのでb内でのfooはAとなる
        return $foo;
    };
    return $b();
};
echo $a(); // A






