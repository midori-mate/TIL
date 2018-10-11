
// 
// 文字列連結方法
// 

/// <summary>
/// 長い文字列を書きたい。StringBuilderの場合。
/// </summary>
private static int FooStringBuilder(int num)
{
    int t = System.Environment.TickCount;
    for (int i = 0; i < num; i++)
    {
        StringBuilder builder = new StringBuilder();
        builder.Append("SELECT ");
        builder.Append("    * ");
        builder.Append("FROM ");
        builder.Append("    tbl ");
        builder.Append("WHERE ");
        builder.Append("    age = 5");
        // Console.WriteLine(builder.ToString());
    }
    return System.Environment.TickCount - t;
}

/// <summary>
/// 長い文字列を書きたい。配列連結の場合。
/// </summary>
private static int FooArrayJoin(int num)
{
    int t = System.Environment.TickCount;
    for (int i = 0; i < num; i++)
    {
        string str = string.Join(" ", new string[] {
        "SELECT",
        "    *",
        "FROM",
        "    tbl",
        "WHERE",
        "    age = 5",
        });
        // Console.WriteLine(str);
    }
    return System.Environment.TickCount - t;
}

/// <summary>
/// 長い文字列を書きたい。+の場合。
/// </summary>
private static int FooPlus(int num)
{
    int t = System.Environment.TickCount;
    for (int i = 0; i < num; i++)
    {
        string s = "";
        s += "SELECT ";
        s += "    * ";
        s += "FROM ";
        s += "    tbl ";
        s += "WHERE ";
        s += "    age = 5";
        // Console.WriteLine(s);
    }
    return System.Environment.TickCount - t;
}