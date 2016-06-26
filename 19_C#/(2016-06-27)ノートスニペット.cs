
// benry snippet


// ==============================
// 日付型の判定
// ==============================
string str = textBox1.Text;
DateTime dt;
if (DateTime.TryParse(str, out dt))
{
    // dtにDateTime化したstrが入ってる
}
else
{
    MessageBox.Show("不適切だよ");
    return;
}

// ==============================
// でかい画像を切り分けてディクショナリに保存する
// つかうときは
//     pictureBox1.Image = imageDict[String.Format("{0:D2}", dictNum)];
// ==============================
static private Dictionary<string, Bitmap> createImageDict()
{
    // 100枚の画像をあらかじめ作っておく
    Bitmap bmpBig = Properties.Resources.tohoicons;
    int x = 0;
    int y = 0;
    Dictionary<string, Bitmap> imageDict = new Dictionary<string, Bitmap>();
    // x=0 y=10になったら終了
    while (y != 10)
    {
        // {"0~99の文字列": 切り取ったbitmap}っていうディクショナリにする
        Bitmap bmpSmall = new Bitmap(60, 80);
        Graphics g = Graphics.FromImage(bmpSmall);
        Rectangle srcRect = new Rectangle(60 * x, 80 * y, 60, 80);
        Rectangle dstRect = new Rectangle(0, 0, 60, 80);
        g.DrawImage(bmpBig, dstRect, srcRect, GraphicsUnit.Pixel);
        g.Dispose();
        imageDict.Add(y.ToString() + x.ToString(), bmpSmall);
        // 座標のインクリメント
        if (x != 9)
        {
            x += 1;
        }
        else
        {
            x = 0;
            y += 1;
        }
    }
    // 画像リソース解放
    bmpBig.Dispose();
    return imageDict;
}

// ==============================
// フェードアウト
// ==============================
// フェードアウトとして、不透明度を減らしていく
for (int i = 99; i >= 0; i--)
{
    // 1%まで不透明度を減らす
    this.Opacity = (double)i / 100;
    // ミリ秒停止
    System.Threading.Thread.Sleep(10);
}
this.Close();

// ==============================
// 一文字ずつ表示する
// ==============================
private string message;
private void buttonMain_Click(object sender, EventArgs e)
{
    message = "aaaaaaaaaaaaaaa.";
    labelMain.Text = "";
    timerMessage.Enabled = true;
}
private void timerMessage_Tick(object sender, EventArgs e)
{
    // 現在の表示
    string now = labelMain.Text;
    // 現在表示しているものがmessageと同じなら終了する
    if (now == message)
    {
        timerMessage.Enabled = false;
        return;
    }
    // 現在の表示の長さ+1のぶんだけmessageを表示する
    labelMain.Text = message.Substring(0, now.Length + 1);
}

// ==============================
// 改行はどれでもいい
// ==============================
message = "あああああ\nいいいいい\rううううう\r\nえええええ";

// ==============================
// 割り算
// ==============================
Console.WriteLine(4.0/5.0); // 0.8
Console.WriteLine(4/5);     // 0


