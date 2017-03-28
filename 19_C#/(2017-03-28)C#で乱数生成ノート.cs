
// C#で乱数生成ノート
// pythonではメッサ簡単だった乱数生成、こっちではシードを自分で設定しないといけないのでちと厄介

// ランダム値を返す関数
private int get_random_number(int start, int end, int seed)
{
    var random = new System.Random(seed);
    return random.Next(start, end);
}

// 呼び出し側がシード値を毎回変えるようにしないとダメ
private void button_Click(object sender, RoutedEventArgs e)
{
    // 基本のシード値にはPC起動後の時間を使う
    int seed = Environment.TickCount;
    var arr = new int[] { 0, 0, 0, 0, 0, 0 };
    for (int i = 0; i < 100; i++)
    {
        int dice = get_random_number(0, 6, seed + i);
        arr[dice]++;
    }
    Console.WriteLine("{0}, {1}, {2}, {3}, {4}, {5}",
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]);
}

// ▼ 毎回シード値に1足して100回行った結果の一例
// 1:17 2:15 3:18 4:16 5:16 6:18


