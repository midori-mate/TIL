<?php

/* ==============
実験結果
headerで飛ぶと_POSTとかは残らんので、文字列で ?entry=*** とかやってスーパーグローバル変数を足せばいい!
============== */

header("Content-Type: text/html; charset=utf-8");

# ボタンが押された
if (isset($_GET["entry"])) {
    $a = $_GET["entry"];
    # それが数字だった
    if (is_numeric($a)) {
        header("Location: ph2.php?entry=$a");
        exit;
    } else {
        # 数字じゃなかった
        print("Number has to be written.");
    }
} else {
    # ボタンが押されてない
    $_GET["entry"] = "";
}

?>
<html>
<body>
<form action="ph.php" method="get">

<input type="text" name="entry"
    value="<?php print(htmlspecialchars($_GET["entry"], ENT_QUOTES)) ?>">

<input type="submit" name="regist" value="Register!">

</form>
</body>
</html>