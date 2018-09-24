//: Playground - noun: a place where people can play

// Optional ノート

import Foundation
import UIKit


class Man {
    func says(x: String) {
        print("swift頻繁な仕様変更やめろ \(x)")
    }
}

// ==========================
// 非Optional    nil不可    普通に参照可能
// ==========================
var a: Man = Man()
a.says(x: "a")


// ==========================
// Optional    nil可    参照するときunwrap必要
// ==========================
var b: Man? = Man()

// unwrapなしで参照はできない。
// b.says()    //Value of optional type 'Man?' must be unwrapped to refer to member 'says' of wrapped base type 'Man'

// 1  Forced unwrap    非Optional型に強制変更    nilだとエラーになる
b!.says(x: "b")

// 2  Optional changing    クラスオブジェクトの場合、メソッド、プロパティが呼び出せる    nilでもエラーにならない
b?.says(x: "b")
var b2: Man?
b2 = nil
b2?.says(x: "b")    // エラーにならない。でも nil とか表示してほしいよねPythonのNoneみたいに。

// 3 Optional binding    条件式のとこでやるやつ    nilのときは代入されず条件式もfalseになる
if let _b = b {
    _b.says(x: "b")
}

// 4 比較演算子    比較演算実行時に一時的にunwrapされる    nilのときは条件式もfalseになる
if b != nil {
    b?.says(x: "b")
}


// ==========================
// Implicitly unwrapped optional    参照するとき勝手にunwrapされるOpt
// ==========================
var c: Man! = Man()

// Implicitly unwrap    nilならエラーになる    勝手にunwrapされるので ! ? if だの使わなくていい。
c.says(x: "c")


// **************************
// 型チェックの方法
// **************************
print(type(of: variable))
