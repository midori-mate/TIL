
// コンボボックスにディクショナリをはめる
// および値を取り出すノート
// なおディクショナリなのは今回限定の事情であり、配列だったら下のforeachのところを配列仕様に変えてよ。

// まず [int=>string] のディクショナリを作成
// csvから生成する方法は「外部ファイルを開くノート」に書いた。
var dic = new Dictionary<int, string>();
dic.Add(0,"aaa");
dic.Add(1,"bbb");

// このディクショナリをオブジェクトにする
class ComboboxData
{
    private string name;
    private int val;
    public ComboboxData(int i, string s)
    {
        name = s;
        val = i;
    }
    public override string ToString()
    {
        // 通常、コンボボックスに表示されるもんは combobox.Add したオブジェクトに ToString() をかけたものなんだ。
        // 今回オブジェクトは自作のComboboxDataオブジェクトだから、
        // そのままToStringするとコンボボックスにComboboxDataオブジェクトって表示されちまう。
        // だからこのオブジェクトにおいてはToStringはこっちが指定した name を文字列で返す仕様にしておく。
        return name;
    }
    public int getVal()
    {
        // で、コンボボックスから値を引き抜くときは combobox.SelectedItem の戻り値を使うんだが、
        // こうして引き抜いたものもComboboxDataオブジェクトでそのままじゃ使えないから、
        // そこから値を抽出するメソッドを用意しといてやる。
        return val;
    }
}

// ディクショナリを自作オブジェクトに変換して、コンボボックスに追加
foreach (var key in dic.Keys)
{
    var data  = new ComboboxData(key, dic[key]);
    combobox.Item.Add(data);
}

// 値の取り出し方
var data = (ComboboxData)combobox.SelectedItem;
// 各メソッドは、上の自作クラスで自分で作ったもの。
Console.WriteLine(data.ToString());
Console.WriteLine(data.getVal());

// オマケで、初期値を表示
combobox.SelectedIndex = 0;

