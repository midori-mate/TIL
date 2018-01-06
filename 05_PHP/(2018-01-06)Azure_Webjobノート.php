<?php

# Azure WebJob ノート
#     https://docs.microsoft.com/ja-jp/azure/app-service/web-sites-create-web-jobs
#     注意: Basic以上のプランじゃないと、常時接続のwebjobは作れません。

# ■ WebJobにスクリプトを登録する方法
#     Azureダッシュボード > {サービスページ}
#         Webジョブ > 追加 > 実行するスクリプトをzipにしてアップロード。
#         アップロードするとき、実行形式とかも選べるよ。手動実行なのか、定期実行なのか、とかね!

# ■ 定期実行にするときのCRON式
#     {second} {minute} {hour} {day} {month} {day of the week}
#     15 分ごと: 0 */15 * * * *
#     1 時間ごと (分の値が 0 のとき): 0 0 * * * *
#     午前 9 時から午後 5 時まで 1 時間ごと: 0 0 9-17 * * *
#     毎日午前 9 時 30 分: 0 30 9 * * *
#     平日の毎日午前 9 時 30 分: 0 30 9 * * 1-5

# ■ 登録したスクリプトのパス。
#     D:/local/Temp/Jobs/{triggered}/{testName}/{tempString}/***.php
# ■ ドキュメントルートのパス。
#     D:/home/site/wwwroot
# ■ だからWebJobスクリプトからwwwroot内のスクリプト呼びたかったらこうすればOK!
#     include 'D:/home/site/wwwroot/***.php';

# ■ ログとかの見かた
#     Webジョブのページからログを見れる。echoした内容もここに出ます。
#     実際のログファイルの場所は
#         wwwroot/data/jobs/の中。


/**
 *
 * 1. includeするwebjobスクリプト。(wwwroot内のファイルをincludeする場合ね!)
 *
 */

# webjob_include.php
$rootPath    = implode(DIRECTORY_SEPARATOR, ['D:', 'home', 'site', 'wwwroot']);
$includePath = implode(DIRECTORY_SEPARATOR, [$rootPath, 'webjobTarget', 'targetScript.php']);

if (!file_exists($includePath)) {
    throw new InvalidArgumentException("Invalid include path: $includePath");
}
include($includePath);

# wwwroot/webjobTarget/targetScript.php
date_default_timezone_set('Asia/Tokyo');
$dateNow = date('Ymd-H時i分s秒');
$outputFilePath = __DIR__ . DIRECTORY_SEPARATOR . 'webjob_put_date.txt';
file_put_contents($outputFilePath, $dateNow . PHP_EOL, FILE_APPEND | LOCK_EX);
echo $dateNow . 'って書かれたはずだけれど……。どう?';


/**
 *
 * ■ 2. webjobの中でライブラリ作ったりrequireしたりしたい。
 *     ファイル構成はこんな感じにする。
 *         main.php
 *         lib
 *             class.php
 *     同階層にふたつ並べちゃいけない。一度にトップディレクトリのひとつのphpファイルしか実行してくれないみたいだから。
 *     (class.phpとmain.phpだとclass.phpのほうが先に読まれてそれで終了しちゃう。)
 *
 */

# main.php
require_once 'lib/class.php';
echo Foo::func();

# lib/class.php
class Foo
{
    public static function func()
    {
        return 'func is called.';
    }
}
