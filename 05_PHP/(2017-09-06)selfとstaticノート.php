<?php


/**
 * selfとstaticノート
 *
 * ・static関数の呼び方
 * ・self::は「self」が書かれてるクラス自身を指す(静的に決まる)
 * ・static::はコールされたクラスを指す(実行時に動的に決まる)
 */

class Foo
{
    public static function stasta()
    {
        return '散々';
    }

    public static function sta()
    {
        return self::stasta();
    }

    public static function stan()
    {
        return static::stasta();
    }
}


class Bar extends Foo
{
    public static function stasta()
    {
        return 'かたつむり';
    }
}


print(Bar::sta());   // selfだから、Fooのstasta()内容が呼ばれる。
print("\n");
print(Bar::stan());  // staticだから、Barのstasta()内容が呼ばれる。
