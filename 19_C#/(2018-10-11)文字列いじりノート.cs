
// 
// 文字列いじりノート
// 

// 変数埋め込み
// あいつはYurika クルマのナンバーは8192 誕生日は10-11 兄弟の年齢はSystem.Double[]

string name = "Yurika";
int number = 8192;
DateTime birthday = DateTime.Now;
double[] doubleList = new double[] { 1.3, 1.5 };

// 6.0 からこれがOK
Console.WriteLine($"あいつは{name} クルマのナンバーは{number} 誕生日は{birthday:MM-dd} 兄弟の年齢は{doubleList}");
// それよか前はこれー
Console.WriteLine(string.Format("あいつは{0} クルマのナンバーは{1} 誕生日は{2:MM-dd} 兄弟の年齢は{3}", name, number, birthday, doubleList));
// WriteLine内だけでよければ string.Format 要らない。
Console.WriteLine("あいつは{0} クルマのナンバーは{1} 誕生日は{2:MM-dd} 兄弟の年齢は{3}", name, number, birthday, doubleList);


// @ 自動エスケープ(逐語的識別子)
//     ただこれはねえ、行の前のインデントもはいっちゃうよ。
var str = @"
SELECT
    x
FROM table
LEFT JOIN table2
    ON table.table_id = table2.table_id
ORDER BY
    table.table_id
";
Console.WriteLine(str);

