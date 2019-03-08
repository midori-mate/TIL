
/// <summary>
/// C# DateTimeNote c#datetimenote
/// </summary>
class Program
{
    // デバッグ実行でコンソールが消えちゃうときはCtrl+F5で実行するといいよ。

    static void Main(string[] args)
    {

        // DateTime でやりたいことなんてだいたい決まってんだよ!

        // 今の時間は?
        Print( DateTime.Now );  // 2019/03/08 15:09:06

        // 自分で作る。
        Print( new DateTime(2000, 2, 7, 23, 59, 59) );

        // 文字列フォーマット。
        Print( DateTime.Now.ToLongDateString()  );  // 2019年3月8日
        Print( DateTime.Now.ToLongTimeString()  );  // 15:10:47
        Print( DateTime.Now.ToShortDateString() );  // 2019/03/08
        Print( DateTime.Now.ToShortTimeString() );  // 15:10
        Print( DateTime.Now.ToString("よく使う普通のやつ yyyy-MM-dd HH:mm:ss"     ) );  // 2019-03-08 16:01:28
        Print( DateTime.Now.ToString("ゼロで埋めない版 yyyy-M-d H:m:s"            ) );  // 2019-3-8 16:1:28
        Print( DateTime.Now.ToString("月を文字で MMM, MMMM 曜日を文字で ddd, dddd") );  // 3, 3月  金, 金曜日
        Print( DateTime.Now.ToString("午前、午後 tt"                              ) );  // 午後

        // ロケールをつけると。
        System.Globalization.CultureInfo[] cultures =
            (new string[] { "ja-JP", "en-US", "en-GB", "fr-FR", "de-DE", "ru-RU" })
            .AsEnumerable()
            .Select(_ => new System.Globalization.CultureInfo(_))
            .ToArray();
        foreach (System.Globalization.CultureInfo culture in cultures)
        {
            Print( DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss" , culture) );  // ふっと思ったんだけど別に
            Print( DateTime.Now.ToString("yyyy-M-d H:m:s"      , culture) );  // 時差を合わせてくれるわけじゃないから気をつけて。
            Print( DateTime.Now.ToString("MMM, MMMM  ddd, dddd", culture) );  // Mar, March  Fri, Friday  mars, mars  ven., vendredi
            Print( DateTime.Now.ToString("tt"                  , culture) );  // PM
        }

        // 単体で取り出す。全部 int だよ。
        Print( DateTime.Now.Year   );  // 2019
        Print( DateTime.Now.Month  );  // 3
        Print( DateTime.Now.Day    );  // 8
        Print( DateTime.Now.Hour   );  // 16
        Print( DateTime.Now.Minute );  // 6
        Print( DateTime.Now.Second );  // 42

        // 時間を動かす。
        Print( DateTime.Now                );  // 2019/03/08 16:08:26
        Print( DateTime.Now.AddDays(-1)    );  // 2019/03/07 16:08:26
        Print( DateTime.Now.AddMonths(-1)  );  // 2019/02/08 16:08:26
        Print( DateTime.Now.AddSeconds(-1) );  // 2019/03/08 16:08:25

        // 月初、月末。
        DateTime d = DateTime.Now;
        d = d.AddDays(-d.Day + 1);
        Print( new DateTime(d.Year, d.Month, d.Day            ) );  // 2019/03/01 0:00:00
        d = d.AddMonths(1).AddDays(-d.Day);
        Print( new DateTime(d.Year, d.Month, d.Day, 23, 59, 59) );  // 2019/03/31 23:59:59
    }

    static void Print(object obj)
    {
        Console.WriteLine(obj);
    }
}
