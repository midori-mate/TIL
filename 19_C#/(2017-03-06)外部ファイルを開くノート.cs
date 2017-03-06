
// C#で外部ファイルを開くノート

// シンプルな形
// Pythonのwithみたいなもん
using (var sr = System.IO.StreamReader(path, Encoding.GetEncoding("UTF-8")))
{
    while (!sr.EndOfStream)
    {
        // 一行ずつlineに格納する。lineはstring。
        var line = sr.ReadLine();
        Console.WriteLine(line);
    }
}

// 1. ディクショナリにしたいとき
// あらかじめ宣言しとくもの
var dic = new Dictionary<int, string>();
// ディクショナリに追加する
var values = line.Split(',');
dic.Add(int.Parse(values[0]), values[1]);

// オマケ:ディクショナリをコンソールに出力
private void print_dictionary(Dictionary<int, string> dic)
{
    foreach (var key in dic.Keys)
    {
        Console.WriteLine(string.Format("int {0} => string {1}", key, dic[key]));
    }
}

// オマケ2:ディクショナリを

// 2. そのまま配列としてつっこむ(結果として二次元配列)
// 宣言。配列は長さを宣言しとかないといけないので、長さが不定であるこの場合はリストを使う
var lis = new List<string[]>();
// リストに追加する
var values = line.Split(',');
lis.Add(values);
// 追加が終わったら、配列へ変換する
return lis.ToArray();

// オマケ:二次元配列をコンソールに出力
private void print_array_2d(string[][] array_2d)
{
    foreach (string[] array in array_2d)
    {
        string str = "";
        foreach (string a in array)
        {
            str += string.Format("string {0}, ", a);
        }
        Console.WriteLine(str);
    }
}



