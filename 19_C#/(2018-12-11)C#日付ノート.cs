
// 
// C# 日付ノート
// 

// いま
Console.WriteLine(DateTime.Now);  // 2018/12/11 18:24:31

// ひと月前
Console.WriteLine(DateTime.Now.AddMonths(-1));  // 2018/11/11 18:24:31

// あるDateTimeの月の初日0時
DateTime d = DateTime.Now;
d = d.AddDays(-d.Day + 1);
Console.WriteLine(new DateTime(d.Year, d.Month, d.Day, 0, 0, 0));  // 2018/11/01 0:00:00

// あるDateTimeの月の末日23時59分
DateTime d = DateTime.Now;
d = d.AddMonths(1).AddDays(-d.Day);
Console.WriteLine(new DateTime(d.Year, d.Month, d.Day, 23, 59, 59));  // 2018/11/30 23:59:59
