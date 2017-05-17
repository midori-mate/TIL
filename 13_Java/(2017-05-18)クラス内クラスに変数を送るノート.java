// クラス内クラスに変数を送るノート
// 下クラスJvのインスタンス変数aは、Jvクラス内クラスFooから直接呼び出すことができない。
// だから以下のような手順で送る。
//     1. Jv.mainでJvインスタンスを生成
//     2. そのインスタンスからaを引きずりだす
//     3. Fooインスタンスを生成しコンストラクタにaを送る
//     4. Fooインスタンスでaを呼び出せる

package org.mate;

public class Jv {
    private String a = "AAA";
    public static void main(String[] args) throws Exception {
        // 1. Jvインスタンス生成
        Jv jv = new Jv();
        // 2と3. そのインスタンスからaを引きずり出してFooインスタンスに送る
        Foo instance = new Foo(jv.a);
        instance.bar();
    }
    public static class Foo {
        private String str;
        public Foo(String a) {
            this.str = a;
        }
        public void bar() {
            // Fooインスタンスでaを使える
            System.out.println(str);
        }
    }


}

