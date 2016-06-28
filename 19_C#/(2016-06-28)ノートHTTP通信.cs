
// HTTP通信ノート

// インスタンス作り
var webClient = new System.Net.WebClient();
var collection = new System.Collections.Specialized.NameValueCollection();
// POSTデータ作り
collection.Add("score", "3");
collection.Add("player", Environment.UserName);
// 送信と受信は同時に行われる
byte[] resData = webClient.UploadValues("http://localhost/php/gameScore/index.php", collection);
webClient.Dispose();
// 受信データをstringに直す
string resText = System.Text.Encoding.UTF8.GetString(resData);
MessageBox.Show(resText);





