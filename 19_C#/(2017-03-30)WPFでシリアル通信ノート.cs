
// Visual Studio 2015 の WPF(windows presentation foundation)プロジェクトでシリアル通信をするノート


// コントロールとディスパッチャ(振り分けシステム)
private System.IO.Ports.SerialPort serialPort = new System.IO.Ports.SerialPort();
private System.Windows.Threading.Dispatcher dispatcher;

// メインウィンドウをメインスレッドとしてディスパッチャに登録しとく
public MainWindow()
{
    InitializeComponent();
    this.dispatcher = System.Windows.Threading.Dispatcher.CurrentDispatcher;
}

// シリアルポートコントロールのデータ受信時イベントメソッドを自分で作る
private void DataReceiveHandler(
    object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
{
    if (this.serialPort.IsOpen == false)
    {
        return;
    }
    // 文字列ならReadExisting() バイナリデータならRead()
    string received_data = this.serialPort.ReadExisting();
    // メインスレッドへデータをデリゲートする方法
    this.dispatcher.BeginInvoke(
        new Action(() => { textBox_input.Text += received_data; })
        );
}

// ポート名称、通信速度、フロー制御はそれぞれ string, int, System.IO.Ports.Handshake で指定する。
private void connect_port()
{
    if (this.serialPort.IsOpen == true)
    {
        this.serialPort.Close();
        button_connect.Content = "Connect";
        return;
    }
    // オープンするシリアルポートの名称
    this.serialPort.PortName  = comboBox_comport.SelectedItem.ToString();
    // 通信速度
    this.serialPort.BaudRate  = ((BaudRateData)comboBox_baudrate.SelectedItem).value;
    // フロー制御を設定
    this.serialPort.Handshake = ((HandShakeData)comboBox_flowcontrol.SelectedItem).value;
    // 1バイトのデータビット数
    this.serialPort.DataBits  = 8;
    // パリティビット
    this.serialPort.Parity    = System.IO.Ports.Parity.None;
    // ストップビット
    this.serialPort.StopBits  = System.IO.Ports.StopBits.One;
    // デフォルトはASCIIみたい
    this.serialPort.Encoding = Encoding.ASCII;
    // なんか、デザイナのほうでserialPortを登録できねーからコードのほうで手動で受信イベントを登録する
    this.serialPort.DataReceived += (DataReceiveHandler);
        // これでもいいよ長いけど
        // new System.IO.Ports.SerialDataReceivedEventHandler(DataReceiveHandler);
    this.serialPort.Open();
    button_connect.Content = "Disconnect";
}

// 上の例ではシリアルポートの名称とか、通信速度とか、フロー制御をコンボボックスから取得してるけど、
// そのコンボボックスを実装するのが下のクラス。
public class BaudRateData
{
    public string name;
    public int value;
    public override string ToString()
    {
        return this.name;
    }
}
public class HandShakeData
{
    public string name;
    public System.IO.Ports.Handshake value;
    public override string ToString()
    {
        return this.name;
    }
}

private void fill_combobox()
{
    // 利用可能なシリアルポートをコンボボックスへ
    string[] portlist = System.IO.Ports.SerialPort.GetPortNames();
    comboBox_comport.Items.Clear();
    foreach (var a in portlist)
    {
        comboBox_comport.Items.Add(a);
    }
    if (comboBox_comport.Items.Count > 0) comboBox_comport.SelectedIndex = 0;

    // ボーレートの一覧をコンボボックスへ
    string[] baudratenamelist = new string[4] { "4800bps", "9600bps", "19200bps", "115200bps" };
    int[] baudratevaluelist = new int[4] { 4800, 9600, 19200, 115200 };
    BaudRateData brdata;
    comboBox_baudrate.Items.Clear();
    for (int i = 0; i < 4; i++)
    {
        brdata = new BaudRateData();
        brdata.name = baudratenamelist[i];
        brdata.value = baudratevaluelist[i];
        comboBox_baudrate.Items.Add(brdata);
    }
    if (comboBox_baudrate.Items.Count > 0) comboBox_baudrate.SelectedIndex = 0;

    // フロー制御の一覧をコンボボックスへ
    string[] handshakenamelist = new string[4] { "なし", "XON/XOFF制御", "RTS/CTS制御", "XON/XOFF+RTS/CTS制御" };
    System.IO.Ports.Handshake[] handshakevaluelist = new System.IO.Ports.Handshake[4]
    {
        System.IO.Ports.Handshake.None,
        System.IO.Ports.Handshake.XOnXOff,
        System.IO.Ports.Handshake.RequestToSend,
        System.IO.Ports.Handshake.RequestToSendXOnXOff
    };
    HandShakeData hsdata;
    comboBox_flowcontrol.Items.Clear();
    for (int i = 0; i < 4; i++)
    {
        hsdata = new HandShakeData();
        hsdata.name = handshakenamelist[i];
        hsdata.value = handshakevaluelist[i];
        comboBox_flowcontrol.Items.Add(hsdata);
    }
    if (comboBox_flowcontrol.Items.Count > 0) comboBox_flowcontrol.SelectedIndex = 0;

}
