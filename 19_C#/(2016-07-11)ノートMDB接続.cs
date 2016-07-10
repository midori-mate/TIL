
// MDB接続ノート

// まずusingにこれを追加
using System.Data.OleDb;


// ==============================
// connをコンストラクタで定義する場合の書き方
// ==============================
private OleDbConnection conn;
public Form1()
{
    conn = new OleDbConnection();
    conn.ConnectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source="+Properties.Settings.Default.mdbPath;
}


// ==============================
// SELECT以外
// ==============================

OleDbConnection conn = new OleDbConnection();
conn.ConnectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=DoDoToDo1.mdb";
conn.Open();
OleDbTransaction transaction = conn.BeginTransaction(IsolationLevel.ReadCommitted);
try
{
    OleDbCommand cmd = conn.CreateCommand();
    cmd.Transaction = transaction;

    // INSERT
    cmd.CommandText = "INSERT INTO main (`do`, `day`) VALUES ('aaaa', '2016/06/22');";
    // UPDATE
    cmd.CommandText = "UPDATE main SET `do`='updated',`day`='2016/06/23' WHERE `id`=1;";
    // DELETE
    cmd.CommandText = "DELETE FROM main WHERE `id`=1;";

    // プリペアドステートメントつかう場合のUPDATE
    string str1 = "pre'pared";
    string str2 = "2016/06/24";
    cmd.CommandText = "UPDATE main SET `do`=@do,`day`=@day WHERE `id`=1;";
    cmd.Parameters.Clear();
    cmd.Parameters.Add("@do", OleDbType.LongVarChar).Value = str1;
    cmd.Parameters.Add("@day", OleDbType.Date).Value = str2;

    // クエリ実行する
    cmd.ExecuteNonQuery();
    transaction.Commit();
}
catch (System.Exception)
{
    transaction.Rollback();
}
finally
{
    conn.Close();
}


// ==============================
// SELECT dataGridView
// ==============================

OleDbConnection conn = new OleDbConnection();
conn.ConnectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=DoDoToDo1.mdb";
conn.Open();
OleDbCommand cmd = conn.CreateCommand();
cmd.CommandText = "SELECT id,do,day FROM main ORDER BY id DESC;";
OleDbDataReader rd = cmd.ExecuteReader();
// dataGridViewに書き出す方法 あらかじめdataGridView1にカラムは用意しておくこと
dataGridView1.Rows.Clear();
while (rd.Read())
{
    DataGridViewRow dgvr = new DataGridViewRow();
    dgvr.CreateCells(dataGridView1);
    dgvr.Cells[0].Value = rd[0].ToString();
    dgvr.Cells[1].Value = rd[1].ToString();
    dgvr.Cells[2].Value = rd[2].ToString();
    // 行ごとに色を変える
    dgvr.DefaultCellStyle.BackColor = Color.Yellow;
    dataGridView1.Rows.Add(dgvr);
}
rd.Close();
conn.Close();
dataGridView1.AllowUserToAddRows = false;


// ==============================
// SELECT 特定のセルを取り出す
// ==============================

OleDbConnection conn = new OleDbConnection();
conn.ConnectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=DoDoToDo1.mdb";
conn.Open();
OleDbCommand cmd = conn.CreateCommand();
cmd.CommandText = "SELECT id,do,day FROM main ORDER BY id DESC;";
OleDbDataReader rd = cmd.ExecuteReader();
// たとえば一番若いidを取り出す場合
string id = "";
while (rd.Read())
{
    id = rd["id"].ToString();
}
rd.Close();
conn.Close();
return id;


// ==============================
// DataTableを使う方法
// ==============================
// まずは基本的なMDBオープンからcmd作成まで
var conn = new OleDbConnection();
conn.ConnectionString = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source="+Properties.Settings.Default.mdbPath;
conn.Open();
OleDbCommand cmd = conn.CreateCommand();
cmd.CommandText = "SELECT * FROM WORK_LOGS " + condition; // 適当にwhere句など
// 必要ならプリペアドステートメント
cmd.Parameters.Add("@example", OleDbType.LongVarChar).Value = example;
// ここから違う
var adapter = new System.Data.OleDb.OleDbDataAdapter(cmd);
var dataTable = new DataTable();
adapter.Fill(dataTable);
adapter.Dispose();
conn.Close();

// DataTableの中身の取り出し 例としてCSV出力
using (var writer = new System.IO.StreamWriter(dstPath, false, System.Text.Encoding.GetEncoding("shift_jis")))
{
    foreach (DataRow row in dataTable.Rows)
    {
        var str = string.Empty;
        for (int i = 0; i < dataTable.Columns.Count; i++)
        {
            writer.Write(str + "\"" + row[i].ToString().Replace("\"", "\"\"") + "\"");
            str = ",";
        }
        writer.WriteLine();
    }
}








