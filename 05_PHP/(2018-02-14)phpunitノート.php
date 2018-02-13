<?php

# phpunitノート

# ■ 準備 Windows版
    /** phpunit インストール
     *
     * 1.下記にアクセスしたら.pharがダウンロードされる。
     *     https://phar.phpunit.de/phpunit.phar
     * 
     * 2.それをパスが通っているところに置く
     *     もしくは保存したいディレクトリでコマンドラインを開いて
     *     $ wget https://phar.phpunit.de/phpunit.phar
     * 
     * 3.ファイル名を変更
     *     [phpunit.phar] から [phpunit] に
     * 
     * 4.確認
     *     cmdで
     *     $ phpunit --version
     *     [PHPUnit 3.7.21 by Sebastian Bergmann.]
     *     と表示されれば成功
     * 
     * [発生した問題]
     * <問題>
     *     4.
     *     PHP Warning:  PHP Startup: Unable to load dynamic library 'C:\xampp\php\ext\php_mysql.dll' - 指定されたモジュールが見つかりません。
     *      in Unknown on line 0
     *     って出てきた。
     *     これは phpunit が勝手にこの中に侵入していって、php_mysql.dllってファイルが必要だからとりに行ったら、無かったよってこと。
     *     phpunitの中で使うモジュールみたいやね
     *         ちなみにdllファイルはモジュール。モジュールは単体としても機能する部品のこと。
     *         開いてみると数字の羅列だったのでなんじゃこりゃと思ったが、phpのプログラムを数字だけで書いてあるらしい。
     *         つまり、なんらかの機能を持ったphpファイルを数字にしてあるやつっていう認識でいい(はず)
     * <解決法>
     *     「php_mysql.dll ダウンロード」 でググって、php_mysql.dll を落としてきて、ここのディレクトリの中に入れれば解決する。
     *     Explorer > PC右クリック > プロパティ > システムの詳細設定 > 環境変数 > Path
     *     でphpのpathを[C:\Program Files (x86)\PHP\v5.6]から[C:\Xammp\php]にしてPHPを7にした。
     *     のにも関わらず、まだエラーが治らない！
     *     php.iniでphp_mysql.dllをコメントアウトして無効にしたったwwこれで正常起動完了。
     *     なにかこれによるエラーが出たらそん時っしょ！！
     * 
     * <問題>
     *     phpuni.bat と phpuni を同じフォルダに置かんとダメみたいだった。
     *     一回古いやつを消したかったので phpuni.bat を消したら死んだ。
     *     それをゴミ箱から復活させて、phpuni だけ最新の奴を落として、 phpuni_6.5.5.phar をphpuniっていう名前にして保存したら成功した。
     *     まあできたしいっか...
     * 
     * あとはパスの通っているところに[phpunit]を置けば使える。
     * (require_onceとかやってないのに使えたのはなんでなんだろう)
     */

    /** coverage 準備
     * [手順1]
     * 拡張モジュール "xdebug" のインストール。
     *     現在使っているphpのあるフォルダの中のextの中にdllファイルを入れて、php.iniの設定を追加した。
     *     下記に従ってやったらあっさりできた。
     * 
     *     <windowsでの設定の仕方>
     *     https://qiita.com/daikiojm/items/84449d33a63b5dfbe9ae
     * 
     * [手順2]
     * ホワイトリストの設定-1-
     *     まず、テストファイルのあるディレクトリに phpunit.xml を作成する。
     * 
     * [手順3]
     * ホワイトリストの設定-2-
     *     phpunit.xmlの内容を以下のように書いてホワイトリストの設定をする。(後述)
     *
     * [手順4]
     * テストファイルのあるディレクトリに出来上がったhtmlファイルを保存する用の空ディレクトリ[dir]を作る。
     */

# ■ 準備 Mac版
    /** phpunit インストール
     * 最初に書いておくけど pear.phpunit.de はもう廃止されてるから、これを使うって言ってる情報は全部使えない。
     *
     * ■ まずcomposerを入れる
     *     $ brew tap homebrew/homebrew-php
     *     $ brew install PHP71
     *     $ brew install homebrew/php/composer
     *
     * ■ phpunitのバージョンを確認する
     *     https://phpunit.de/manual/current/ja/installation.html
     *     今回はPHPUnit6.5にする
     *
     * ■ phpunitをインストール
     *     $ composer global require "phpunit/phpunit=6.5.*"
     *     $ export PATH=$PATH:~/.composer/vendor/bin/
     *         これは .bash_profile にも書く。
     *     $ phpunit --version
     */

    /** coverage 準備
     * ■ xdebugインストール
     *     https://xdebug.org/wizard.php
     *         $ php -i の結果を貼り付けると必要なtgzを教えてくれるんでそれをDL。
     *         その後のことも全部ここで教えてくれる。 Instructionsのところ。
     *     $ php -m
     *         で完了確認。
     */

# ■ coverage のための phpunit.xml
    /**
    ________________________________________________________________________________
    <?xml version="1.0" encoding="UTF-8"?>
    <phpunit backupGlobals="false"
             backupStaticAttributes="false"
             colors="true"
             convertErrorsToExceptions="true"
             convertNoticesToExceptions="true"
             convertWarningsToExceptions="true"
             processIsolation="false"
             stopOnFailure="false"
             syntaxCheck="false">
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="CACHE_DRIVER" value="array"/>
        <env name="SESSION_DRIVER" value="array"/>
        <env name="QUEUE_DRIVER" value="sync"/>
    </php>
    <filter>
        <!-- coverageの対象にするディレクトリを書きます。 -->
        <whitelist>
            <directory>.</directory>
        </whitelist>
    </filter>
    </phpunit>
    ________________________________________________________________________________
 */

# ■ まず書くもの。
    use PHPUnit\Framework\TestCase;
    require_once 'Klass.php';  # テストするファイル。

# ■ 実例1 たくさんの入力値、期待値パターンでテストする。
    class KlassTest extends TestCase
    {
        /**
         * @dataProvider provider_foo
         */
        public function test_foo($x,$y,$expected)
        {
            $this->assertEquals($expected, Klass::foo($x,$y));
        }
        public function provider_foo()
        {
            return [
                'one one' => [1, 1, 2],
                'one two' => [1, 2, 3],
                'two ten' => [2, 10, 12]
            ];
        }
    }

# ■ 実例2 Exception含むdataProvider
    class KlassTest extends TestCase
    {
        /**
         * @dataProvider provider_bar
         */
        public function test_bar($x, $expectException, $expected)
        {
            # 通常の返り値期待。
            if (!$expectException) {
                $res = Klass::bar($x);
                $this->assertEquals($expected, $res);  # ここのexpectedには実数が入ってる。
                return;
            }

            # 例外が飛んでくるのを期待。
            try
            {
                Klass::bar($x);
            }
            catch(Exception $e)
            {
                $this->assertTrue($e instanceof $expected);  # ここのexpectedには例外クラスが入ってる。
                return;
            }
            $this->fail("引数 $x のときは例外でなくちゃダメ。");
        }
        public function provider_bar()
        {
            return [
                [true, true, 'InvalidArgumentException'],
                [false, false, 1],
                [1, true, 'InvalidArgumentException'],
                [0, false, 1],
            ];
        }
    }

# ■ 実例3 モック
    class KlassTest extends TestCase
    {
        # かなり限定されたやり方しか分からなかった...
        #   追記:privateとstaticメソッドのモック化はかなりめんどくさいらしい。Phakeというフレームワークが推奨されてた。

        # [手順1] テストしたいメソッド(A)を public function にする
        # [手順2] その中でモックにしたいメソッド(B)を public function で用意しておく(中身は空で良い)
        # [手順3] A内でBのスコープを this-> にする (インスタンスを使用するため)

        public function testqux()
        {
            # 指定したクラスを、指定したメソッドのみモック化して、インスタンス化できる。(スタブという)
            $stub = $this->getMockBuilder(Klass::class) # クラス指定。Klassにクラス名を入れる。
                         ->setMethods(['quux']) # モックにしたいメソッド指定。
                         ->getMock();

            # スタブの設定。空で用意してあるメソッドに代用したい値を設定する。(モック作成)
            $stub->expects($this->once()) # メソッドが一度だけコールされる。
                 ->method('quux') # コールされるメソッドはquux()。
                 ->willReturn('foo'); # その値を'foo'で代用する。

            # テストするメソッドを指定。上記で設定したモックを使用してメソッドが実行される。
            $testMethod = $stub->qux();

            $this->assertEquals('foo', $testMethod);
        }
    }
