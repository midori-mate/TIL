
// 手動コントロールイベント登録
// ツールボックスに目当てのコントロールが見受けられねーときのために

private System.IO.Ports.SerialPort serialPort = new System.IO.Ports.SerialPort();

// たとえばシリアルポートがデータ受信時のイベント
private void DataReceiveHandler(
    object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
{
    // something
}

private void foo()
{
    // こんな風に登録する
    this.serialPort.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(DataReceiveHandler);

    // イベント側に e の引数があれば、イベントの種類を特定しなくてもいいみたい。
    this.serialPort.DataReceived += (DataReceiveHandler);
}

