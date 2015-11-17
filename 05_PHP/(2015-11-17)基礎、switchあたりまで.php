<?php

// $_GET はスーパーグローバル関数。連想配列で、URLで渡された変数名がキーと値になってる。
// is_numeric() は数字かどうかをチェックする関数。

// print($_GET["foo"]); と書いちゃいけない。かわりに print(htmlspecialchars($_GET["foo"])); と書く。
// これはセキュリティ上の問題

/*
// http://localhost/uranai.php?age=22
if (is_numeric($_GET["age"]) == true) {
    print("your age:");
    print(htmlspecialchars($_GET["age"]));
    print("years old");
} else {
    print("not number was typed.");
}
*/

// || は or

if (is_numeric($_GET["age"]) == false) {
    print("write \"number\"!!");
    exit();
}

$message[0] = "zero";
$message[1] = "one";
$message[2] = "two";

if ($_GET["age"] >= 30 || $_GET["age"] < 10) {
    $number = 0;
} elseif ($_GET["age"] >= 20) {
    $number = 2;
} else {
    $number = 1
}

print($message[$number]);

# ----------------------------------------------- for

print("roop starts\n");
for ($i = 0; $i < 10; $i++) {
    print($i . "roop\n");
}
print("roop ends up.\n");

// roop starts
// 0roop
// 1roop
// 2roop
// 3roop
// 4roop
// 5roop
// 6roop
// 7roop
// 8roop
// 9roop
// roop ends up.

# ---------------------------------------- foreach


// foreach (配列 as キー => 値)
$month_list = array(
    "1" => "January", "2" => "February",
    "3" => "March", "4" => "April");
foreach($month_list as $month_number => $month_name) {
    print($month_number . "月は" . $month_name . "です\n");
}

# -------------------------------------- while

$i = 0;
while($i < 10) {
    print($i . "kaime no roop\n");
    $i++;
}
print("roop ends up");

# -------------------------------------- switch case break

// switch構文では break つけないと次の case も実行されてしまうので break は必須・
$i = rand(1, 4);
switch ($i) {
    case 1:
    print("good weather");
    break;
    case 2:
    print("cloudy");
    break;
    case 3:
    print("fuckin rainy");
    break;
    default:
    print("don t know the wather");
    break;
}

$temp = 0;
switch ($temp++) {
    case 0:
        # smt
    case 1:
        break;
}
# このときswitch文で起きているのは
# tempが0なのでcase 0へ飛ばす -> tempをインクリメントする、というもの。なんか下行って上行ってる感じがして面白い
# なお ++$temp だとcase 1へ飛ぶ
