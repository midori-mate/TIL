<?php

/* -------------------
fopen ファイルを開く
    引数は (ファイル名, モード) モードは r読み込み w書き込み a追記
-------------------　*/

/* ------------------- 読み込む系
file_get_contets ファイルの全内容を読み込んで返す
readfile ファイルの全内容をそのままブラウザに出力
file ファイルの全内容を一行ごとの配列にして返す
fgets ファイルの内容を一行ごと読み込み返す。fopen()と組み合わせて使う
fgetc ファイルの内容を一文字ごと読み込み返す。fopen()と組み合わせて使う
fread ファイルの内容を指定した長さだけ読み込み返す。fopen()と組み合わせて使う
fgetcsv CSVファイルの内容を一行ごと読み込み、各列ごとの配列にして返す。fopen()と組み合わせて使う
fgetss ファイルの内容を一行ごと読み込み、HTMLタグを取り除いて返す。fopen()と組み合わせて使う
------------------- */

$filename = "C:\\xampp\\htdocs\\php\\samplefile.txt";
print(file_get_contents($filename));

/* ------------------- 書き込む系
file_put_contents 指定した内容をファイルに書き込む
fputcsv 指定した配列をCSVに整形して書き込む
fwrite(fputs) 指定した内容をファイルに書き込む。fopen()と組み合わせて使う
------------------- */

$filename = "samplefile.txt";
$string = "あいうえおaiueo天上天下";
$fp = fopen($filename, "w");
fwrite($fp, $string);
fclose($fp);
