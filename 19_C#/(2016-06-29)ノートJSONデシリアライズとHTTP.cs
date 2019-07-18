
// JSONデシリアライズ
// 鬼門はJSONの形式にしたがってクラスを定義しないといけないところ。自動でやってくれよC#の旦那～

// 「アセンブリ参照不足」避け メニュー、プロジェクト、参照の追加、から以下を追加
//     System.Runtime.Serialization
//     System.ServiceModel.Web

private void button2_Click(object sender, EventArgs e)
{
    string url = "http://localhost/php/gameScore/index.php";
    // WebClientインスタンス作成
    var webClient = new System.Net.WebClient();
    // POST項目
    var collection = new System.Collections.Specialized.NameValueCollection();
    collection.Add("give", "data");
    // 返ってきたデータをbyteで取得
    byte[] resData = webClient.UploadValues(url, collection);
    webClient.Dispose();
    // byteをstringへ
    string resText = System.Text.Encoding.UTF8.GetString(resData);
    // ストリームを作る …なんだストリームって
    var stream = new System.IO.MemoryStream(Encoding.Unicode.GetBytes(resText));
    var serializer = new System.Runtime.Serialization.Json.DataContractJsonSerializer(typeof(MyJson));
    // 中身を取り出せるかたちにする
    var obj = (MyJson)serializer.ReadObject(stream);
    string str = string.Format("{0} {1} {2} {3}", obj.dic1.id, obj.dic1.score, obj.dic1.player, obj.dic1.day);
    MessageBox.Show(str);
}

// jsonの定義 [dic1=>{id=>1,score=>2,player=>3,day=>4}, dic2=>dic,] こんな感じのがくる
[System.Runtime.Serialization.DataContract]
public class MyJson
{
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic0 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic1 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic2 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic3 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic4 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic5 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic6 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic7 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic8 { get; set; }
    [System.Runtime.Serialization.DataMember]
    public ScoreDict dic9 { get; set; }
    [System.Runtime.Serialization.DataContract]
    public class ScoreDict
    {
        [System.Runtime.Serialization.DataMember]
        public string id { get; set; }
        [System.Runtime.Serialization.DataMember]
        public string score { get; set; }
        [System.Runtime.Serialization.DataMember]
        public string player { get; set; }
        [System.Runtime.Serialization.DataMember]
        public string day { get; set; }
    }
}

// asp.net でも出会った。
// 
// 1. 参照を追加
// 2. using 追加
// 3. クラスを DataContract 化 
// 4. フィールドを DataMember 化
// 
// かいてるうちにすげー面倒くさくなってきた。
// C# なんてどうでもいい…… Python やりたい…… ゼッタイもっとラクに json 化させてくれる……
// まあいつか困ったときのためにシンプルな json 化だけ下にメモっとくよ。
// 

using System.Runtime.Serialization;
using System.IO;
using System.Runtime.Serialization.Json;

[DataContract]
public class SignModel
{
    [DataMember(Name = "ContactId")]
    public string ContactId { get; set; }

    [DataMember(Name = "SignStatus")]
    public string SignStatus { get; set; }
}

public class SignData : AbstractModel
{
    public List<SignModel> Models { get; set; }

    public string ModelsJson
    {
        get
        {
            // この部分が json 化だよ。
            using (var stream = new MemoryStream())
            {
                var serializer = new DataContractJsonSerializer(Models.GetType());
                serializer.WriteObject(stream, Models);
                return Encoding.UTF8.GetString(stream.ToArray());
            }

        }
    }
}
