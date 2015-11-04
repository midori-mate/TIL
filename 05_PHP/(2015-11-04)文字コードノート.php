<?php

# 文字化けを防ぐ呪文 これはレスポンスヘッダにUTF-8を入れてねっていうお願い
header("Content-Type: text/html; charset=utf-8");

# いま何の文字コードでやってるか教えてくれるやつ
print(mb_internal_encoding());

# mb_convert_kana関数が動かなかったら文字コードのせいっぽい。utf-8に変えよう
$a = mb_convert_kana("１", "a", "UTF-8");

print($a . "\n");


?>

<html>
<head>

<!-- これはレスポンスボディに UTF-8 でよろしく! っつーお願い -->
<meta http-equiv="Content-Type" 
            content="text/html; charset=UTF-8">
            
</head>
</html>
