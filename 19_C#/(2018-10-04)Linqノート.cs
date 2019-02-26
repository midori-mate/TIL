using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;

namespace cs_lab
{
    class Program
    {
        // デバッグ実行でコンソールが消えちゃうときはCtrl+F5で実行するといいよ。

        //
        // Linq Note
        //     foreachの強化版だとかいう言い方をされてるけど、
        //     ぼく的には「pythonの高階関数ができる」っていうほうがわかりやすい。
        //

        static void Main(string[] args)
        {
            var list = new List<int> { 0, 1, 2, 3, 4, 5 };

            // query構文
            var query = from x in list
                        where x % 2 == 0
                        orderby x
                        select x * 3;

            // method構文
            var method = list
                        .Where(x => x % 2 == 0)
                        .OrderBy(x => x)
                        .Select(x => x * 3);

            // Linqの前に覚えておきたい 匿名クラス
            var fruitList = new[]
            {
                new {Name = "apple", Price = 300},
                new {Name = "banana", Price = 200},
                new {Name = "pineapple", Price = 1000},
            };
            foreach (var fruit in fruitList)
            {
                Console.WriteLine(fruit);
            }

            // Linqの前に覚えておきたい ラムダ式
            var findAllList = list.FindAll(x => x % 2 == 0);
            foreach (var x in findAllList)
            {
                Console.WriteLine(x);
            }

            // Linq 要素取得
            list.First();
            list.Last();

            // Linq 集計
            list.Max();
            list.Min();
            list.Average();
            list.Sum();
            list.Count();

            // Linq 変換
            int[] array = list.ToArray();
            List<object> objectList = list.Cast<object>().ToList();

            // Linq 重複を除く
            list.Distinct();

            // Linq 先頭から指定数スキップ
            list.Skip(3);

            // Linq 先頭から指定数取得
            list.Take(3);

            // Linq 判定 すべて100未満
            list.All(x => x < 100);

            // Linq 判定 いずれか100未満
            list.Any(x => x < 100);

            // Linq 判定 含まれる
            list.Contains(3);

            // Linq 和集合
            var list2 = new List<int> { 4, 5, 6, 7, 8 };
            list.Union(list2);

            // Linq 差集合
            list.Except(list2);

            // Linq 積集合
            list.Intersect(list2);

            // Linq ソート 昇順
            fruitList.OrderBy(x => x.Price);

            // Linq ソート 降順
            fruitList.OrderByDescending(x => x.Price);

            // Linq ソート 逆順
            fruitList.Reverse();

            // Linq メソッドの組み合わせ
            list
                .Distinct()        // 重複削除
                .Skip(2)           // 先頭からふたつ飛ばす
                .OrderBy(x => x);  // 昇順

            // Linq 以外のメソッドも組み合わせる
            list
                .FindAll(x => x % 2 == 0)
                .OrderBy(x => x)
                .ToList()  // ConvertAllのために一旦Listに変換
                .ConvertAll(x => x * 3);

            // ↑のをSelectとWhereで書き換える
            list
                .Where(x => x % 2 == 0)
                .OrderBy(x => x)
                .Select(x => x * 3);

            // ↑のをquery構文で書き換える(ただ格納しないとエラーになったよ)
            var _ = from x in list
                    where x % 2 == 0
                    orderby x
                    select x * 3;

            // 2019-02-26
            // 実際に「[f'"{a}"' for a in array]みたいなことがしたいな」と思って書いたやつ。
            string[] array = new string[] {"foo", "bar"};
            array = array.Select(x => "\"" + x + "\"").ToArray();
            // ToArray をつけないと string[] には格納できないよ。
        }
    }
}
