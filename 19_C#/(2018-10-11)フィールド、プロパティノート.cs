
// 
// C# フィールド、プロパティノート
// 

// 正の数(1以上)じゃないといけない変数です。
// publicにしといたら負の数が代入されちゃう可能性あるじゃん。ね、プロパティいるでしょ?
private int _positiveNumber;  // これがフィールド
public int PositiveNumber     // これがプロパティ
{
    get { return _positiveNumber; }
    set { _positiveNumber = value > 0 ? value : 1; }
}

// なんでもいい変数です。こんなん別にpublicのフィールドでよくねって思うけど
// こういう場合もプロパティにするのはC#のコーディングルールみたい。
private int _anyNumber;
public int AnyNumber
{
    get { return _anyNumber; }
    set { _anyNumber = value; }
}

// ただし↑のは長いからこんな感じに書ける。
public int AnyNumber2 { get; set; }

// さらに6.0からは初期値も設定可能だよ。
public int AnyNumber3 { get; set; } = 5;
