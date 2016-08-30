<?php

/*
クラス変数を動的に生成するノート

phpではpythonみたいにクラスのグローバルスコープで処理をすることができないので、
「クラス外でクラス変数を操作するクラスメソッドを呼ぶ」
という方法をとる。
*/

Foo::createA();

class Foo
{
    /**
     * これは「クラス変数を動的に生成」と直接関係はないが、
     * 「もうすでに生成されてるよ」のフラグ管理をするinitialize処理。
     */
    public static $notInitialized = true;
    public static $a;
    public static function createA()
    {
        if (!self::$notInitialized) {
            return;
        }
        self::$a = 'aaa';
    }

}

echo Foo::$a;


