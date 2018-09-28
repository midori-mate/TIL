//: Playground - noun: a place where people can play

// swift4 Dateノート
// PlayGroundに貼って実行するとわかりやすいよ!


// これがないとDateもFormatterも使えん。
import UIKit


// 現在。DateはGMTで表示される。日本時間にしたいときは……
let nowDate:Date = Date()
print(nowDate, "<- これはGMTで表示されてるはず。")


// ……Formatterでタイムゾーンを指定する。
func createDateFormatter() -> DateFormatter {
    let formatter = DateFormatter()
    formatter.timeZone = TimeZone.current
    print(formatter.timeZone)
    formatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
    return formatter
}
let formatter = createDateFormatter()


// Dateを文字列に変換。このときタイムゾーンが適用される。
let nowString:String = formatter.string(from: nowDate)
print(nowString, "<- これはちゃんと日本時間が表示されてるはず。")


// 時間をずらす。たとえば1時間後。
let plusHourDate:Date = Date(timeInterval: 60*60, since: nowDate)
print(plusHourDate, "<- これもDateなのでGMTのはず。")


// yyyy-mm-dd から Date を取得する。
func getDateFromString(string:String) -> Date {
    
    // yyyy-mm-dd を分解。まあこれはただの文字列操作。文字列のスライスねーのだるい……
    var s:String = string
    let year = Int(s.prefix(4))!
    s = s.replacingOccurrences(of: s.prefix(5), with: "")
    let month = Int(s.prefix(2))!
    s = s.replacingOccurrences(of: s.prefix(3), with: "")
    let day = Int(s)!
    
    // こうやって日付を取得。入力した情報は日本時間として解釈されているみたい。
    // DateはGMTになってるからprintしたら前日になってるとかある。混乱するわ…
    // これをDateFormatterで文字列にすれば入力した日付になってる。
    return Calendar.current.date(from: DateComponents(year:year, month:month, day:day))!
    // DateComponents(
    //                calendar: Calendar?, timeZone: TimeZone?, era: Int?,
    //                year: Int?, month: Int?, day: Int?, hour: Int?, minute: Int?, second: Int?, nanosecond: Int?,
    //                weekday: Int?, weekdayOrdinal: Int?, quarter: Int?, weekOfMonth: Int?, weekOfYear: Int?, yearForWeekOfYear: Int?)
}
let d:Date = getDateFromString(string: "2018-09-01")
print(d, "<- 2018-08-31 って表示されて「は?」ってなる")
print(createDateFormatter().string(from: d), "<- formatterを通すとちゃんと2018-09-01になっとるやろ。")
