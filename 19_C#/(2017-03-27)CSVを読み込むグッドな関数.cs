
// CSVを読み込むグッドな関数
// Microsoft.VisualBasic のアセンブリ参照を追加すること。

// GCCS-CSに使ったバージョン
// リソースに対応
private string[][] foo(string csv_path, string resource)
{
    // Microsoft.VisualBasicのアセンブリ参照を追加しておくこと。
    Microsoft.VisualBasic.FileIO.TextFieldParser parser;

    // CSVファイルを確認できたらそれを使い、なければリソースを使う
    if (System.IO.File.Exists(csv_path))
    {
        parser = new Microsoft.VisualBasic.FileIO.TextFieldParser(
            csv_path, Encoding.GetEncoding("UTF-8"));
    }
    else
    {
        // TextFieldParserに直接文字列を渡すときはstringじゃなく
        // StringReaderを通さないとダメ
        var reader = new System.IO.StringReader(resource);
        parser = new Microsoft.VisualBasic.FileIO.TextFieldParser(
            reader);
    }

    // 二次元配列化
    var lis = new List<string[]>();
    using (parser)
    {
        // 区切り文字を指定
        parser.TextFieldType =
            Microsoft.VisualBasic.FileIO.FieldType.Delimited;
        parser.SetDelimiters(",");
        while (!parser.EndOfData)
        {
            string[] row = parser.ReadFields();
            var lis_row = new List<string>();
            foreach (string r in row)
            {
                lis_row.Add(r);
            }
            lis.Add(lis_row.ToArray());
        }
    }
    return lis.ToArray();
}

// 二次元配列表示
private void print_2D_array(string[][] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        string format = string.Format("[{0}] => [\r\n", i);
        for (int j = 0; j < array[i].Length; j++)
        {
            format += string.Format("    [{0}] => {1},\r\n", j, array[i][j]);
        }
        format += "],";
        Console.WriteLine(format);
    }
}


// 2019-02-28
// 
// asp.net で asp:FileUpload から送られてきたCSVを読み込む場合。
// 

using Microsoft.VisualBasic.FileIO;
using System.Text;

// これに詰めるよ。
List<string[]> data = new List<string[]>();
if (this.FileUploadCsv.HasFile)
{
    // 注意: FileContent は System.IO.Stream なんだけど、一度読み込んだら2度はできないみたい。
    using (TextFieldParser parser = new TextFieldParser(this.FileUploadCsv.FileContent,
                                                        Encoding.GetEncoding("Shift_JIS")))
    {
        // カンマで区切る設定。
        parser.TextFieldType = FieldType.Delimited;
        parser.SetDelimiters(",");

        // フィールドがクォートで囲まれているか。これは別にクォートがついてなくてもエラーにならない。
        // 数字が 1,000 とかになってることもあるからつけとけ。
        parser.HasFieldsEnclosedInQuotes = true;
        // フィールドの空白はトリムするか。
        parser.TrimWhiteSpace = true;

        // フィールド読み込み。
        while (!parser.EndOfData)
        {
            data.Add(parser.ReadFields());
        }
    }
}
