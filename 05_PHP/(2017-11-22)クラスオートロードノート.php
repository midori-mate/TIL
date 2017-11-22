<?php

# クラスオートロードノート。


# クラスオートロード 「そんなクラスねーよ」というタイミングで$funcが実行される設定
$func = function($a) {

    # クラスオートロード関数の中で「そんなクラスねーよ」が起きたらフツーにnotfoundでFatalErrorになるよ。
    new FooBar();

    require_once $a . '.php';
};
spl_autoload_register($func);


# PHPが終わったとき実行される設定。エラーで落ちようが実行される。
$shutdown_func = function() {
    echo 'おわったぞおおおおおおおおおおおおお！' . PHP_EOL;
};
register_shutdown_function($shutdown_func);


# 「Fooなんてクラスねーよ」クラスオートロード実行される。
new Foo();
# 「Barなんてクラスねーよ」同上。
new Bar();
# Bazはファイルもないからクラスオートロード内でエラー落ち。その際にregister_shutdown_funtionで指定したことが起こる。
new Baz();
