
// ディクショナリと配列

// ディクショナリの作り方
var d1 = new Dictionary<string, string>()
{
    {"id", "1"},
    {"score", "3"},
    {"player", "Watashi"},
};
var d2 = new Dictionary<string, string>()
{
    {"id", "2"},
    {"score", "4"},
    {"player", "Akaru Sate"},
};
var d3 = new Dictionary<string, string>()
{
    {"id", "3"},
    {"score", "5"},
    {"player", "Yurika Saijou"},
};

// 配列の作り方
Dictionary<string, string>[] array = {d1, d2};

// 配列に追加する方法
var list = new List<Dictionary<string, string>>(array);
list.Add(d3);
Dictionary<string, string>[] array2 = list.ToArray();



