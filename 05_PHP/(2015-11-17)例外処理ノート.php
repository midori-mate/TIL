<?php

############### 例外1 不格好な例外処理

function div($a, $b) {
    if ($a > 0 && $b == 0) {
        return INF;
    }
    if ($a < 0) && $b == 0 {
        return -INF;
    }
    if ($a == 0 && $b == 0) {
        trigger_error("ゼロ除算とか無理だってはっきりわかんだね", E_USER_WARNING);
        return false;
    }
    return $a / $b;
}
echo "計算スタート\n";
$answer = div(1, 0);
if ($answer === false) {
    die("そんなことをしてはいけない(戒め) \n");
}
printf("div(1, 0) = %s\n", $answer);
$answer = div(-1, 0);
if ($answer === false) {
    die("そんなことをしてはいけない(戒め) \n");
}
printf("div(-1, 0) = %s\n", $answer);
$answer = div(0, 0);
if ($answer === false) {
    die("そんなことをしてはいけない(戒め) \n");
}
printf("div(0, 0) = %s\n", $answer;
echo "計算エンド\n";
/* 実行結果
計算スタート
div(1, 0) = INF
div(-1, 0) = -INF
Warning:  ゼロ除算とか無理だってはっきりわかんだね in ... on line ...
そんなことはしてはいけない(戒め)

記述が冗長だしエラメもそのまま表示されてカッコワルイ。
*/

############### 例外2 tryを使った例外処理

function div($a, $b) {
    if ($a > 0 && $b == 0) {
        return INF;
    }
    if ($a < 0 && $b == 0) {
        return -INF;
    }
    if ($a == 0 && $b == 0) {
        throw new Exception("ゼロ除算とか無理だってはっきりわかんだね");
    }
    return $a / $b;
}

try {
    echo "計算スタート\n";
    printf("div(1, 0) = %s\n", div(1, 0));
    printf("div(-1, 0) = %s\n", div(-1, 0));
    printf("div(0, 0) = %s\n", div(0, 0));
    echo "計算エンド\n"
} catch (Exception $e) {
    echo $e->getMessage() . "\n";
    echo "そんなことをしてはいけない(戒め) \n";
}
/* 実行結果
計算スタート
div(1, 0) = INF
div(-1, 0) = -INF
ゼロ除算とか無理だってはっきりわかんだね
そんなことはしてはいけない(戒め)
*/

############### 例外3 Exceptionクラス

class Exception {
    private $message;
    private $code;
    public function __construct($message = "", $code = 0) {
        $this->message = $message;
        $this->code = $code;
    }
    public function getMessage() {
        return $this->message;
    }
    public function getCode() {
        return $this->code;
    }
}

try {
    # 1. この中でthrowされた例外は
} catch (Exception $e) { # 2. ここで$eに代入されて
    # 3. ここへ強制的に移動する
}
// 例外処理においては、それまで実行途中であった完結していない処理はなかったことになる

############### 例外4 

// 文字列にキャストしてみてfalseだとしても強引に""に変換する、という処理を
public function setName($name) {
    $this->name = (string)filter_var($name);
}
// 文字列にキャスト不可能な型が渡されたら例外をスローする、に変更する
public function setName($name) {
    $name = filter_var($name);
    if ($name === false) {
        throw new InvalidArgumentException("ホモ特有の使い方はNG");
    }
    $this->name = $name;
}


