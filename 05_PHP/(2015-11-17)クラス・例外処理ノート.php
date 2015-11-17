<?php

/* ================
参考
http://qiita.com/mpyw/items/41230bec5c02142ae691

2015.11.17. ::とか静的プロパティとかがよくわからん。とりあえずノートだけしとく。

================ */

############### new

class Robot {}
$a = new Robot;
$b = new Robot;
// Robotはロボットの設計図。設計図をもとにロボットを製造するには、new演算子を使う。

############### public

class {
    public $name;
}
$a = new Robot;
$a->name = "ロボ太郎";
$b = new Robot;
$b->name = "ロボ次郎";
// 名前のないのは可哀想なので名前を記録するプロパティを確保する。publicはどこからでもアクセス可能なことを意味する。
// ->はアロー演算子という。$a->$nameと書くと、$nameをプロパティの名前にするってだけになる。(あとでテスト)
// ロボ太郎とかつける前にはnullが入ってる。nullがイヤだったら public $name = ""; にしましょう。

############### private

class {
    private $name = "";
}
$a = new Robot;
$a->name = "ロボ太郎"; // error
$b = new Robot;
$b->name = "ロボ次郎"; // error
// 配列とか勝手に入れられちゃったらイヤなのでアクセス権をprivateにする! したらロボ太郎ロボ次郎もエラーになる!

############### setter

class {
    private $name = "";
    public function setName($name) {
        $this->name = (string)filter_var($name);
    }
}
$a = new Robot;
$a->setName("ロボ太郎");
$b = new Robot;
$b->setName("ロボ次郎");
echo $a->name; // error
echo $b->name; // error
// 外部から名前を受け取り、文字列なら設定するメソッドを追加。メソッドは外部からアクセス可能じゃないと意味ないからpublicに。
// $thisはインスタンス自身を指す。$a->setName("ロボ太郎");とコールしたら、setNameメソッド内で$thisは$aを指す。
// まだエラーが出る。privateにしたら、書き込みだけでなく読み取りのメソッドも必要。

############### getter

class {
    private $name = "";
    public function setName($name) {
        $this->name = (string)filter_var($name);
    }
    public function getName() {
        return $this->name;
    }
}
$a = new Robot;
$a->setName("ロボ太郎");
$b = new Robot;
$b->setName("ロボ次郎");
echo $a->getName();
echo $b->getName();
// Getter/Setterパターンというオブジェクト指向の根幹

############### __construct

class Robot {
    private $name = "";
    public function __construct($name) {
        $this->setName($name);
    }
    public function setName($name) {
        $this->name = (string)filter_var($name);
    }
    public function getName() {
        return $this->name;
    }
}
$a = new Robot("ロボ太郎");
$b = new Robot("ロボ次郎");
echo $a->getName();
echo $b->getName();
// __constructという名前でコンストラクタメソッドを作ると、インスタンス生成時に自動的にコールされる。こゆ特別なのをマジックメソッドという。

############### stdClass

class stdClass {}
$a = new stdClass;
$a->name = "ロボ太郎";
echo $a->name;
// 未定義のインスタンスプロパティを新たに作成できる。ちなみにpublicとなる。
// 配列とstdClassは相互にキャストが可能 $array = (array)$stdClass とか $stdClass = (object)$array;

############### 値渡し

$a = "value";
$b = $a;
// 普通に、$bに$aの値がコピーされる

$a = "value";
$b = &$a;
// $aと$bが同じ値を参照するようになる

$a = new stdClass;
$b = $a;
// $bに$aの値がコピーされる。オブジェクトはidという値によって管理されてる。#1みたいな感じ。

############### 静的プロパティ、静的メソッド、オブジェクト定数

class Sample {
    public static $property;
    # 静的プロパティ
    public static function method() {}
    # 静的メソッド
    const OBJECT_CONSTANT = null
    # オブジェクト定数(クラス定数でよくね?とか言われてるもの)
}
// クラス内で自らのインスタンスを生成する場合、newクラス名のかわりにnew selfが使える。

###############
/*
インスタンスプロパティ
    外部から $v->name
    IM内から $this->name
    静的M内から --
インスタンスメソッド
    外部から $v->name()
    IM内から $this->name()
    静的M内から --
静的プロパティ
    外部から クラス名::$name
    IM内から self::$name
    静的M内から self::$name
静的メソッド
    外部から クラス名::name()
    IM内から self::name()
    静的M内から self::name()
*/

############### factory method1

class Robot {
    private $name = "";
    private $color;
    public function __construct($name, $color) {
        $this->setName($name);
        $this->color = $color === "blue" ? "blue" : "red";
    }
    public function setName($name) {
        $this->name = (string)filter_var($name);
    }
    public function getName() {
        return $this->name;
    }
    public function getColor() {
        return $this->color;
    }
}
$a = new Robot("ロボ太郎");
$b = new Robot("ロボ次郎", "blue");
echo $a->getColor(); // red
echo $b->getColor(); // blue
// ロボットに色情報を追加する。条件は以下。
// 一度決めたら変更できない。色はredとblueだが、色の指定が間違ってた場合はredを適用。

$a->__construct("ロボ太郎", "blue");
echo $a->getColor();
// しかし、こうすると色が変わっちゃうじゃないか!!

############### factory method2

class Robot {
    private $name = "";
    private $color;
    public static function createRedRobot($name) {
        return new self($name, "red");
    }
    public static function createBlueRobot($name) {
        return new self($name, "blue");
    }
    private function __construct($name, $color) {
        $this->setName($name);
        $this->color = $color;
    }
    public function setName($name) {
        $this->name = (string)filter_var($name);
    }
    public function getName() {
        return $this->name;
    }
    public function getColor() {
        return $this->color;
    }
}
$a = Robot::createRedRobot("ロボ太郎");
echo $a->getColor(); // red
$a->__construct("ロボ太郎", "blue"); // error
echo $a->getColor(); // red
// コンストラクタはオブジェクトを生成したときに実行されるもの、かつ、publicだとクラス内でしかいじれない
// ゆえにクラス内のメソッドで色を指定したオブジェクトを生成し、その瞬間コンストラクタでプロパティを作ればいいってことか!

############### 継承

class B extends A {}
// Bから見てAは親。BにはAのプロパティやメソッドがすべて引き継がれる。
/*
継承されるか
    private される
    protected される
    public される
継承したクラスからアクセスできるか
    private むり
    protected できる
    public できる
クラス外からアクセスできるか
    private むり
    protected むり
    public できる

*/


