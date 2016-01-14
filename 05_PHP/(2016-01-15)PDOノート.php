<?php

/* ********************
SQLiteとの接続  
PDOオブジェクトを作るところが違うだけかな?
******************** */
try {
    $pdo = new PDO("sqlite:{DB名}"); // ここにはパスを書く
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // エラーの代わりに例外を投げる
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC); // 毎回FETCH_ASSOCを書かなくていい!

    // プレースホルダ使わない場合
    $sql = "SELECT * FROM table;";
    $rows = $pdo->query($sql)->fetchALL();

    // プレースホルダ使う場合
    $sql = "SELECT * FROM table WHERE id=?;";
    $select = $pdo->prepare($sql);
    $a = 1;
    $select->bindParam(1, $a, PDO::PARAM_INT); // bindParamの第二引数は変数のみ。bindValueはどっちでもいい
    $select->execute();
    $row = $select->fetch();

} catch(PDOException $e) {
    # なんか適当に
}


/* ===============
DBとphpをつなぐノート
使用テーブルはmate.member_list
カラムはid, name, address, favourite_color

$dsnは"mysql:dbname=**;host=localhost;charset=utf8"
mysqlではlocalhostと127.0.0.1で接続方法が変わる(Unixのみ?)
my.cnfにskip-networking(TCPポート無効化)を設定しているとlocalhostじゃないと接続できん

=============== */

try {
    $pdo = new PDO(
        "mysql:dbname=mate; host=127.0.0.1; charset=utf8; port=3306",
        "user",
        "pass",
        array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)
        );
    $rows = $pdo->query("SELECT * FROM mate.member_list")->fetchALL(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    $error = $e->getMessage();
}
foreach ($rows as $row) {
    $last = count($row) - 1;
    foreach ($row as $key => $value) {
        print("$key=>$value ");
    }
    print("\n");
}
print_r($rows);

###################### fetch() fetchALL() PDO::FETCH_ASSOC の意味調べ
# fetch()は1レコードの「カラムと値」「配列のキーと値」を出してくれる。
# PDO::FETCH_ASSOCは「カラムと値」だけを出してくれる。
# fetchALL()は全レコードを連想配列にして出してくれる。
# 実際の返り値は以下を見てね。

$pdo = new PDO(
    "mysql:dbname=mate; host=localhost; charset=utf8; port=3306",
    "user",
    "pass",
    array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)
    );
$rows = $pdo->query("SELECT * FROM executive_list;")->fetch();
print_r($rows);
/*
Array
(
    [id] => 1
    [0] => 1
    [position] => leader
    [1] => leader
    [name] => Someone
    [2] => Someone
)
*/
$rows = $pdo->query("SELECT * FROM executive_list;")->fetch(PDO::FETCH_ASSOC);
print_r($rows);
/*
Array
(
    [id] => 1
    [position] => leader
    [name] => Someone
)
*/
$rows = $pdo->query("SELECT * FROM executive_list;")->fetchALL();
print_r($rows);
/*
Array
(
    [0] => Array
        (
            [id] => 1
            [0] => 1
            [position] => leader
            [1] => leader
            [name] => Someone
            [2] => Someone
        )
    [1] => Array
        (
            [id] => 2
            [0] => 2
            [position] => sub leader
            [1] => sub leader
            [name] => Hikaru
            [2] => Hikaru
        )
)
*/
$rows = $pdo->query("SELECT * FROM executive_list;")->fetchALL(PDO::FETCH_ASSOC);
print_r($rows);
/*
Array
(
    [0] => Array
        (
            [id] => 1
            [position] => leader
            [name] => Someone
        )
    [1] => Array
        (
            [id] => 2
            [position] => sub leader
            [name] => Hikaru
        )
)
*/

###################### queryじゃなくてprepare使ってSELECTする
$stmt = $pdo->prepare("SELECT * FROM {tablename} WHERE id=:id");
$stmt->bindValue(":id", 1, PDO::PARAM_INT);
$stmt->execute();
if ($rows = $stmt->fetch()) {
    $name = $rows["name"];
    $age = $rows["age"];
}

###################### INSERT
$name = "Yurika";
$age = "28";
$stmt = $pdo->prepare("INSERT INTO {tablename} (id,name,age) VALUES ('',:name,:age)");
$stmt->bindParam(":name", $name, PDO::PARAM_STR);
$stmt->bindValue(":age", $age, PDO::PARAM_STR);
$stmt->execute();

###################### bindParam, bindValue
# Paramはbindからexecuteまでの間に変数の中身が変わったらそっちが使われる(評価が実行時)
# Valueはbindした時点のものが使われる(bind時点で評価)

###################### UPDATE
$a = $pdo->prepare("UPDATE {table} SET name=:name WHERE id=:id");
$a->bindParam(":name", $name, PDO::PARAM_STR);
$a->bindValue(":id", $id, PDO::PARAM_INT);
$a->execute();

###################### DELETE
# record削除
$b = $pdo->prepare("DELETE FROM {table} WHERE id=:delete_id");
$b->bindValue(":delete_id", $id, PDO::PARAM_INT);
$b->execute();
# table削除 tableの場合executeじゃなくてexec
$pdo->exec("DROP TABLE IF EXISTS {table}");

###################### COUNT
$b = $pdo->prepare("SELECT * FROM {table} WHERE age=:age");
$b->bindValue(":age", $age, PDO::PARAM_INT);
$b->execute();
$count = $b->rowCount();

###################### SUM
# 条件Yに当てはまるa1の合計を出す場合
$c = $pdo->prepare("SELECT SUM(a1) as a1 FROM {table} WHERE y=:y");
$c->bindParam(":y", $y, PDO::PARAM_STR);
$c->execute();
if ($row = $c->fetch()) {
    $total = $row["a1"];
}
# 複数のとき
$c = $pdo->prepare("SELECT SUM (a1+a2+a3) as grandtotal FROM {table} WHERE y=:y");
$c->bindParam(":y", $y, PDO::PARAM_STR);
$c->execute();
if ($row = $c->fetch()) {
    $total = $row["grandtotal"];
}