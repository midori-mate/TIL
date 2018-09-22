//: Playground - noun: a place where people can play

// swift4 ソートノート
// PlayGroundに貼って実行するとわかりやすいよ!


import Foundation


// リスト。
var dates:[String] = [
    "2018-08-01",
    "2018-09-03",
    "2018-08-02",
    "2018-09-02",
    "2018-08-03",
    "2018-09-01",
]
// 昇順(default)
dates.sort()
dump(dates)
// 降順
dates.sort(by: {$0 > $1})
dump(dates)


// ディクショナリをキーでソート。
// ただし返ってくるものはもうディクショナリじゃなくてタプルの配列。
var dates2:[String:[String]] = [
    "2018-08-01": ["foo"],
    "2018-09-03": ["foo"],
    "2018-08-02": ["foo"],
    "2018-09-02": ["foo"],
    "2018-08-03": ["foo"],
    "2018-09-01": ["foo"],
]
// 昇順
dump(dates2.sorted() { $0.0 < $1.0 })
// 降順
dump(dates2.sorted() { $0.0 > $1.0 })
// for したときちゃんと順番になっている。
for (key, value) in dates2.sorted(by: { $0.0 < $1.0 }) {
    print(key, value)
}
// sorted したものを return するときは -> [String:[String]] じゃダメ。
func foo() -> [(key: String, value: [String])] {
    return  ["1": ["foo", "bar"]].sorted(by: {$0.0 > $1.0})
}
// タプルの配列だから、取り出すときはこう。 python とちょっと違うね。
print(dic[0].key)
