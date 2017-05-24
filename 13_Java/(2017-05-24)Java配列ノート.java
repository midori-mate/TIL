// Java配列ノート

// =======================================================
// 配列を表示する
System.out.println(Arrays.asList( ここに配列 ));


// =======================================================
// LIST

// Listの定義はこう!
List<String> string_list = new ArrayList<String>(
        Arrays.asList("zero","one","two","three"));

// 追加はこう!
string_list.add("four");

// 配列使って追加はこう!
for (String s: new String[] {"five", "six", "seven"}) {
    string_list.add(s);
}

// 複数add! おすすめ!
Collections.addAll(string_list, "eight", "nine");

// 取り出しは list[8] とかじゃなくてー。
System.out.println(string_list.get(8)); // eight

// foreachで回す場合。
for (String s: string_list) {
    System.out.print(s); // zeroonetwothreefourfivesixseveneightnine
}

// データの追加：List.add(データ);
// データの取得：List.get(インデックス);
// データの削除：List.remove(インデックス);
// データの更新：List.set(インデックス, データ);
// リストの長さ：List.size();

// =======================================================
// Map

// 連想配列、Mapの定義はこう!
Map<String, String> string_map = new HashMap<String, String>() {
    {
        put("one", "ONE");
        put("two", "TWO");
        put("three", "THREE");
    }
};

// 追加はこう!
string_map.put("four", "FOUR");

// 取り出しは string_map["one"] じゃなくて…。
System.out.println(string_map.get("one")); // ONE

// 取り出しはこう! ただし順番はめちゃくちゃ。
for (Map.Entry<String, String> m : string_map.entrySet()) {
    System.out.print(m.getKey());
    System.out.println(m.getValue());
}

// =======================================================
// HashMapのList
// HashMap<String, String>[]

// まず外枠の宣言。
List<HashMap<String, String>> lis = new ArrayList<HashMap<String,String>>();
// 中にいれるHashMapの宣言。
HashMap<String, String> hm = new HashMap<String, String>();
// 追加。
lis.add(hm);
// 確認。[{chief_cd=30, s_constr_no=400, constr_cd=200      }]
System.out.println(lis);

// HashMapを出力したとき中身も表示してくれるのめっちゃ嬉しくね!?
// いやpythonたちはフツーにやってくれることだけど!



