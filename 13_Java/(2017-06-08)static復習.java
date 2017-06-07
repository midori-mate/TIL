
// メンバ変数は俺に馴染みある言い方でいうとインスタンス変数。
// static変数は俺に馴染みある言い方でいうとクラス変数。

// Jvクラスの例で言うと count_Human はコンストラクタでインクリってるからインスタンス作るたびに加算される。

// 個人的にちょっとびっくりしたのが、クラス変数を「加算」なんてことができたところだ。
// pythonでもやってみよう。


public class Jv {

    // メンバ変数たち
    String name;
    int birthday;
    int manpukudo;

    // クラス変数
    static int count_Human = 0;


    // コンストラクタたち
    Jv(String name, int birthday, int manpukudo) {
        this.name = name;
        this.birthday = birthday;
        this.manpukudo = manpukudo;
        count_Human++;
    }
    Jv(String name, int birthday) {
        this(name, birthday, 50);
    }
    Jv(String name) {
        this(name, 0, 50);
    }
    Jv() {
        this("UNKNOWN", 0, 50);
    }

    // メンバメソッド
    void eat() {
        this.manpukudo += 60;
    }

}


public class Jv2 {

    public static void main(String[] args) {

        System.out.println(Jv.count_Human);    // 0

        Jv jv1 = new Jv();
        Jv jv2 = new Jv();

        System.out.println(Jv.count_Human);    // 2

    }

}


"

class Human:

    count_Human = 0

    def __init__(self, name='UNKNOWN', birthday=0, manpukudo=50):
        self.name = name
        self.birthday = birthday
        self.manpukudo = manpukudo
        Human.count_Human += 1


print(Human.count_Human)

human1 = Human()
human2 = Human()

print(Human.count_Human)

"

