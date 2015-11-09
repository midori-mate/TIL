<?php
header("Content-Type: text/html; charset=utf-8");

/* -----------
print <<< EOF
ヒアドキュメント <<<EOFからEOF;の箇所までを文字列としてまとめて表示する。EOFっていうのは別の文字列でもOKAY
end of file

ヒラカワさんと見つけたこと
EOF;にはスペースとかあっちゃダメだし、くわえて、;の次には改行がないといけない!
改行があっちゃだめ、はこれまで何度かあったけれど、改行がないとだめ!は初めてだ。
----------- */

# 検索フォームをHTML出力する
print <<< EOF
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;  
charset=EUC-JP" />
<title>ユーザー定義型関数</title>
</head>
<body>
検索文字を入力してください。<br>
文字列に「saity」という文字が入っているか検索するよ<br>
<form action="php.php" method="post">
<input type="text" name="val" value=""><br>
<input type="submit" value="検索開始">
</form>
</body>
</html>
EOF;

# 検索の値チェック
# isset部分がサイトには入ってなかった。こうやってトラップ仕掛けるのマジやめろや!
if (isset($_POST["val"]) && $_POST["val"] != "") {
    # 検索する関数を呼び出す
    $message = search_word($_POST["val"]);
    print "<hr>";
    print $message;
}

# ここからがユーザー定義型関数

# 文字列から saity という文字列を検索してメッセージを出力する関数
# こっちもサイトではpostがposになってたりする。マジやめろや!!
function search_word($word) {
    $findme = 'saity';
    $post = mb_strpos($word, $findme);

    # 見つからなかったときは
    if ($post === False) {
        return "「" . $findme . "」の文字列は「" . $word . "」の中にはないよ。";

    # 見つかったときは
    } else {
        return "「" . $findme . "」の文字列は「" . $word . "」の中にあるよ。";
    }
}
