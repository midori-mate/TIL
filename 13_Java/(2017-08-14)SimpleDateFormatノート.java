
// SimpleDateFormatの使い方を毎回ググってるからノートにするよ。

// ■ 1. 今の時間を"2017-06-01 11:22:33"みたいな文字列で欲しいんだけど〜
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
String wanted = sdf.format(new Date());

// ■ 2. 文字列からDateがほしいんだけど〜
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
Date wanted = sdf.parse("2000-01-01");

// ■ 3. 7日後が文字列でほしいんだけど〜
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
Calendar cal = Calendar.getInstance();
cal.setTime(new Date());
cal.add(Calendar.DATE, 7); // 月なら.MONTH 年なら.YEAR
String wanted = sdf.format(cal.getTime());



// つまり
//     Date   --format--> String
//     String --parse-->  Date

