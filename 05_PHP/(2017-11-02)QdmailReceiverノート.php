<?php

/*
QdmailReceiverノート
    http://hal456.net/qdmail_rec/top

SMTP
    「SMTP」とは「Simple Mail Transfer Protocol（シンプル・メール・トランスファー・プロトコル）」の略で、あえて訳せば「簡単なメールの送信の手順」というところだろうか。
POP
    「POP」は「Post Office Protocol（ポスト・オフィス・プロトコル）」の略で、まさしく「郵便局の手順」だ。

問題:QdPop: Comunicate Error
    yahooのほうはこれでうまくいったから、設定が間違ってるくさい。
        'protocol' =>'pop3',
        'host'     =>'pop.mail.yahoo.co.jp',
        'user'     =>'username',
        'pass'     =>'password',
    サイコのほうはこれ。
        'protocol' =>'pop3',
        'host'     =>'mail.test.co.jp',
        'user'     =>'username@test.co.jp',
        'pass'     =>'password',
*/



# PHP Deprecated と Strict Standards がライブラリ内で起こるので非表示に。
error_reporting(E_ALL & ~E_DEPRECATED & ~E_STRICT);

require_once('0.1.4.alpha/qdmail_receiver.php');

$params = [
    'protocol' =>'pop3',
    'host'     =>'mail.test.co.jp',
    'user'     =>'username@test.co.jp',
    'pass'     =>'password',
];

$paramsYahoo = [
    'protocol' =>'pop3',
    'host'     =>'pop.mail.yahoo.co.jp',
    'user'     =>'username',
    'pass'     =>'password',
];

# POPサーバとの接続を作ります。
$receiver = QdmailReceiver::start('pop', $params);

# サーバにあるメール件数を取得します。
echo $receiver->count() . PHP_EOL;

# いま読んでるメールの番号(POPセッション毎に1から付け直し)を取得します。
echo $receiver->pointer() . PHP_EOL;

# そのメールのUID(POPサーバー内では一意に保たれる)を取得します。
echo $receiver->getUid() . PHP_EOL;

# メールの差出人です。
    echo 'From: '
echo $receiver->header(['from', 'name']) . PHP_EOL;
echo $receiver->header(['from', 'mail']) . PHP_EOL;

# 差出人を一括取得します。
print_r($receiver->header(['from'])) . PHP_EOL;

# 件名を一括取得します。
print_r($receiver->header(['subject'])) . PHP_EOL;

# メール本文を取得します。
echo $receiver->bodyAutoSelect() . PHP_EOL;

# メール本文をテキストで取得します。htmlメールの場合代替テキスト。代替テキストがない場合nullです。
echo $receiver->text() . PHP_EOL;

# 添付ファイルを取得します。
print_r($receiver->attach());

# 添付ファイルを保存するコードです。
foreach($receiver->attach() as $att){
    $fp = fopen($att['filename_safe'], 'w');
    fputs($fp,$att['value']);
    fclose($fp);
}

# 次のメールへ移動します。
$receiver->next();

# 移動したことを確認します。
echo $receiver->pointer() . PHP_EOL;
echo $receiver->header(['subject', 'name']) . PHP_EOL;

print_r($receiver->listHeader()) . PHP_EOL;

// for($i = 1 ; $i <= $receiver->count() ; $i++){

//     echo "Mail number: ".$receiver->pointer()."\r\n";
//     echo htmlspecialchars(
//         print_r(
//            $receiver->header( array('subject','name') , 'none' )
//         ,true)
//     ,ENT_NOQUOTES);

//     echo "\r\n";
//     $receiver->next();
// }

echo PHP_EOL;
