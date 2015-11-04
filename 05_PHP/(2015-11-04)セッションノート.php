<?php  
/* ===================
セッションの働きを理解するやつ
更新するたびに数字が増えるよ
=================== */

# 文字化けを防ぐ呪文 これはレスポンスヘッダにUTF-8を入れてねっていうお願い
header("Content-Type: text/html; charset=utf-8");

session_start();

if (isset($_SESSION["counter"])) {
    $_SESSION["counter"]++;
    print($_SESSION["counter"] . "回目の読み込みだよー");
}
else {
    $_SESSION["counter"] = 0;
    print("最初の読み込みだよー");
}