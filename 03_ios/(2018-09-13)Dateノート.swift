//: Playground - noun: a place where people can play

// swift4 Dateノート
// PlayGroundに貼るとわかりやすいよ!


// これがないとDateもFormatterも使えん。
import UIKit

// 現在。DateはGMTで表示される。日本時間にしたいときは……
let nowDate:Date = Date()
print(nowDate, "<- これはGMTで表示されてるはず。")

// ……Formatterでタイムゾーンを指定する。
let formatter = DateFormatter()
formatter.timeZone = TimeZone.current
print(formatter.timeZone)
formatter.dateFormat = "yyyy-MM-dd HH:mm:ss"

// Dateを文字列に変換。このときタイムゾーンが適用される。
let nowString:String = formatter.string(from: nowDate)
print(nowString, "<- これはちゃんと日本時間が表示されてるはず。")


// 時間をずらす。たとえば1時間後。
let plusHourDate:Date = Date(timeInterval: 60*60, since: nowDate)
print(plusHourDate, "<- これもDateなのでGMTのはず。")


