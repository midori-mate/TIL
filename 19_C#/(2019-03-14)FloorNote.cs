
/// <summary>
/// 小数点以下切り捨てノート 端数切り捨て FloorNote
/// 今回のハイライト : C#の小数点以下切り捨てはint化ではない。(?!)
/// </summary>


class Program
{
    // デバッグ実行でコンソールが消えちゃうときはCtrl+F5で実行するといいよ。

    static void Main(string[] args)
    {
        // 状況: 以下のようなパターンに対応したいね。
        //       円マークつきの文字列        \50000
        //       カンマつきの文字列          50,000
        //       小数点のついた数値の文字列  50000.00
        // やりたい: これらを全部 50000 にしてくれ。decimal ね!

        // パターンを全部合成したもの。
        string sample = @"\50,000.999";
        // ↓
        sample = sample.Replace(@"\", string.Empty);  // 1. 円を消す。
        decimal matomeDeci = GetDecimal(sample);      // 2. decimal化。
        matomeDeci = Math.Floor(matomeDeci);          // 3. 端数切り捨て。
        Print(matomeDeci);
    }

    /// <summary>
    /// object を decimal として取得します。カンマ区切りの文字列も許可します。
    /// </summary>
    /// <param name="value"></param>
    /// <returns></returns>
    static decimal GetDecimal(object value)
    {
        decimal test = 0;
        if (value == null || value is DBNull || !decimal.TryParse(value.ToString(),
                                                                  // decimal.TryParse はデフォルトで AllowThousands(カンマを許容してくれる)です。
                                                                  out test))
        {
            return 0;
        }
        return test;
    }

    static void Print(object obj)
    {
        Console.WriteLine(obj);
    }
}
