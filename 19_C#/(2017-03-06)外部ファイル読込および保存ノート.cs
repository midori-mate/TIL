
// 外部ファイル読込および保存ノート
// 「ファイルを開く」関数
// 「読み込む」関数
// 「名前をつけて保存」関数
// 「テキスト出力」関数

// CSVを処理する(ディクショナリにしたり)は「外部ファイルを開くノート」に書いてある


// 「ファイルを開く」ダイアログを開いて、ユーザの選んだパスをゲットする関数
private string open_dialog()
{
    var return_path = "";
    var open_dialog = new System.Windows.Forms.OpenFileDialog();
    open_dialog.Title = "ふぁいるを開く";
    open_dialog.InitialDirectory = @"";
    open_dialog.Filter = "テキストファイル|*.txt;*.log|すべてのファイル|*.*";
    open_dialog.FilterIndex = 2;
    open_dialog.RestoreDirectory = true;
    open_dialog.Multiselect = false;
    if (open_dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
    {
        return_path = open_dialog.FileName;
    }
    return return_path;
}

// 読み込む関数
private void input_text()
{
    // 上の関数からパスを取得
    string text_path = open_dialog();
    if (text_path == "")
    {
        return;
    }
    using (var sr = new System.IO.StreamReader(path, Encoding.GetEncoding("UTF-8")))
    {
        while (!sr.EndOfStream)
        {
            var line = sr.ReadLine();
            // CSVだったらこんなふうにしたりして
            // var values = line.Split(',');
            Console.WriteLine(line);
        }
    }
}

// 「名前をつけて保存」ダイアログを開いて、ユーザの選んだパスをゲットする関数
private string save_dialog()
{
    var return_path = "";
    var save_dialog = new System.Windows.Forms.SaveFileDialog();
    save_dialog.FileName = "GCCS出力テキスト.txt";
    save_dialog.InitialDirectory = @"";
    save_dialog.Filter = "TXTファイル(*.txt)|*.txt|すべてのファイル(*.*)|*.*";
    save_dialog.Title = "保存先を選んでください。";
    save_dialog.RestoreDirectory = true;
    save_dialog.OverwritePrompt = true;
    if (save_dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
    {
        return_path = save_dialog.FileName;
    }
    return return_path;
}

// 出力する関数
private void output_text()
{
    // 出力する内容はその都度テキトーにかえる。リストが便利。
    var value_list = new List<string>();
    value_list.Add( this.textBox_name.Text );
    var data = (ComboboxData)this.comboBox_job.SelectedItem;
    value_list.Add( data.getValue().ToString() );

    // 上の関数からパスを取得
    string text_path = save_dialog();
    if (text_path == "")
    {
        return;
    }
    // リストをforeachして一行ずつ書き込む
    using (var sw = new System.IO.StreamWriter(text_path, false, Encoding.GetEncoding("SJIS")))
    {
        foreach (string line in value_list)
        {
            sw.WriteLine(line);
        }
    }
}





