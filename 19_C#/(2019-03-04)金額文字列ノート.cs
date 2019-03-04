
// 
// 金額文字列ノート
//     \2,000 みたいなのをどうやって int や decimal にするの? ってやつ。
//

// =============================================================
// 円マークとカンマを消す基本的な知識。 @"\" と AllowThousands
// =============================================================
class Program
{
    // デバッグ実行でコンソールが消えちゃうときはCtrl+F5で実行するといいよ。


    static void Main(string[] args)
    {

        // 円マークつきとカンマつきを用意したぞ。
        string a = @"\500".Replace(@"\", string.Empty);
        string b = "20,000";

        int int_a = int.Parse(a, System.Globalization.NumberStyles.AllowThousands);
        int int_b = int.Parse(b, System.Globalization.NumberStyles.AllowThousands);

        decimal deci_a = decimal.Parse(a, System.Globalization.NumberStyles.AllowThousands);
        decimal deci_b = decimal.Parse(b, System.Globalization.NumberStyles.AllowThousands);

        Console.WriteLine(int_a + int_b);    // 20500
        Console.WriteLine(deci_a + deci_b);  // 20500
    }
}


// =============================================================
// 実用的にした util っぽい関数。パースできなかったら 0 が返る。
// GetInt と GetDecimal
// =============================================================
class Program
{
    // デバッグ実行でコンソールが消えちゃうときはCtrl+F5で実行するといいよ。

    static void Main(string[] args)
    {

        // 円マークつきとカンマつきを用意したぞ。
        string a = @"\500".Replace(@"\", string.Empty);
        string b = "20,000";

        Console.WriteLine(GetInt(a) + GetInt(b));  // 20500
        Console.WriteLine(GetDecimal(a) + GetDecimal(b));  // 20500
    }

    /// <summary>
    /// object を int として取得します。カンマ区切りの文字列も許可します。
    /// </summary>
    /// <param name="value">object.</param>
    /// <returns>int.</returns>
    static int GetInt(object value)
    {
        int test = 0;
        if (value == null || value is DBNull || !int.TryParse(value.ToString(),
                                                              System.Globalization.NumberStyles.AllowThousands,
                                                              null,
                                                              out test))
        {
            return 0;
        }

        return test;
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
                                                                  // decimal.TryParse はデフォルトで AllowThousands です。
                                                                  out test))
        {
            return 0;
        }

        return test;
    }
}


// =============================================================
// ゼロ埋め関数も作ったよ。
// =============================================================
class Program
{
    // デバッグ実行でコンソールが消えちゃうときはCtrl+F5で実行するといいよ。

    static void Main(string[] args)
    {

        string a = "";
        int b = 567;

        Console.WriteLine(ZeroPadding(a, 6));  // "000000"
        Console.WriteLine(ZeroPadding(b, 6));  // "000567"
    }

    /// <summary>
    /// ゼロ埋めして n 桁にします。
    /// </summary>
    /// <param name="obj"></param>
    /// <param name="n"></param>
    /// <returns></returns>
    static string ZeroPadding(object obj, int n)
    {
        return obj.ToString().PadLeft(n, '0');
    }
}
