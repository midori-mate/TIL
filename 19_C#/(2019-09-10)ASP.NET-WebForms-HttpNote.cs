
/// <summary>
/// 
/// ASP.NET Web Forms で Http 通信をする
/// Python の requests に比べてクッソ面倒。
/// なんで C# が人気あるのかわからん。
/// 
/// </summary>

/// <summary>
/// aspx は html を何も書かない。コレだけ書く。
/// <%@ Page Language="C#" AutoEventWireup="true" CodeFile="Test.aspx.cs" Inherits="Test" %>
/// </summary>

/// <summary>
/// aspx.cs はこう。
/// ノートなので、
/// </summary>
protected void Page_Load(object sender, EventArgs e)
{
    // ■ [HttpRequest] クライアントからのリクエスト情報取得。
    // 例えば POST の受け取りとか、 UserAgent の取得とか。
    // Request は上位クラスの System.Web.UI.Page から継承している。
    // HttpRequest から取得できる情報はここに。
    // https://docs.microsoft.com/ja-jp/dotnet/api/system.web.httprequest?view=netframework-4.8#%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3
    // クライアントからの POST データはこう。
    string foo = Request.Form["foo"];

    // ■ [HttpWebRequest] C# からリクエストを送信したいとき。 Python が requets でサクッとやってくれること。
    // HttpWebRequest を生成する前に TLS1.1 および 1.2 を有効にする。
    // (SecurityProtocolType.Tls | Tls11 | Tls12) が存在しない環境では代替として 0x を用いていることができる。
    System.Net.ServicePointManager.SecurityProtocol = (System.Net.SecurityProtocolType)(0xc0 | 0x300 | 0xc00);
    // HttpWebRequest の作成。
    var webReq = (System.Net.HttpWebRequest)System.Net.WebRequest.Create("https://...");
    // HttpWebRequest のリクエストヘッダ作成。
    // Python の requests を見習うべき、煩雑な手法。
    webReq.Method = "POST";
    webReq.ContentType = "application/json;charset=utf-8";
    webReq.CachePolicy = new System.Net.Cache.HttpRequestCachePolicy(System.Net.Cache.HttpRequestCacheLevel.NoCacheNoStore);
    webReq.Accept = "application/json";
    webReq.Headers.Set("X-FORWARDED-FOR", HttpContext.Current.Request.UserHostAddress);
    webReq.Timeout = 3000;
    webReq.ReadWriteTimeout = 3000;
    // POST データを作成。
    // Python の requests を見習うべき、煩雑な手法。いちいち byte[] に変換して書き込まないといけない。
    // 送信したいもの。
    object obj = new
    {
        foo = "foo",
        bar = "bar",
    };
    // これを JSON に変換。これは結構便利ね。
    var serializer = new System.Web.Script.Serialization.JavaScriptSerializer();
    string json = serializer.Serialize(obj);
    // JSON を byte[] に変換。
    byte[] bytes = System.Text.Encoding.UTF8.GetBytes(json);
    // 作成した POST データを HttpWebRequest にくっつける。
    webReq.ContentLength = bytes.Length;
    using (System.IO.Stream stream = webReq.GetRequestStream())
    {
        stream.Write(bytes, 0, bytes.Length);
    }

    // ■ [HttpWebResponse] 作った HttpWebRequest を送信。
    // ここではレスポンスのステータスコードと、メッセージ部を取得してみる。
    System.Net.HttpWebResponse webRes = null;
    System.Net.HttpStatusCode statusCode;
    string responseText = string.Empty;
    try
    {
        webRes = (System.Net.HttpWebResponse)webReq.GetResponse();
        // System.Net.HttpStatusCode の一覧はここに。
        // https://www.atmarkit.co.jp/fdotnet/dotnettips/817httpstatus/httpstatus.html
        statusCode = webRes.StatusCode;
        // メッセージ部を取得。
        using (System.IO.Stream stream = webRes.GetResponseStream())
        using (System.IO.StreamReader sr = new System.IO.StreamReader(stream, System.Text.Encoding.UTF8))
        {
            responseText = sr.ReadToEnd();
        }

    }
    catch (System.Net.WebException ex)
    {
        // サーバ接続不可などの場合。
        webRes = (System.Net.HttpWebResponse)ex.Response;
        if (webRes == null)
        {
            // 再スロー。
            throw;
        }
        // ステータスコードは取得できている場合。
        statusCode = webRes.StatusCode;
    }
    finally
    {
        if (webRes != null)
        {
            webRes.Close();
        }
    }
    // 我慢できなくて言いますけど Python の requests なら以上の作業はこれで済む。
    // res = requests.post('https://...', data={'foo':'foo','bar':'bar'}, headers={...})
    // print( res.status_code, res.text ) 

    // ■ [HttpResponse] 任意のレスポンスをクライアントへ返す。
    Response.ContentType = "application/json; charset=UTF-8";
    // r は RFC1123 という形式の日付。 "ddd, dd MMM yyyy HH':'mm':'ss 'GMT'"
    Response.AddHeader("Last-Modified", DateTime.Now.ToString("r"));
    Response.AddHeader("Cache-Control", "no-store, no-cache, must-revalidate");
    Response.AddHeader("Cache-Control", "post-check=0, pre-check=0");
    Response.AddHeader("Pragma", "no-cache");
    // Output します。今回の場合 JSON を返してみます。
    Response.Output.Write("{\"foo\":\"foo\",\"bar\":0,\"baz\":1}");
}
