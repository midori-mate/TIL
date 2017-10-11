<?php

# これをCSVにしてDLさせる
$a = [
    ['aaa', 'bbb', 'ccc'],
    ['ああ', 'いい', 'うう'],
    ['黄金', '砂場', '増田'],
];

# 5MBを制限とする一時ファイルを作成する。
$f = fopen('php://temp/maxmemory:'.(5*1024*1024), 'r+');
foreach ($a as $b) {
    fputcsv($f, $b);
}

# ファイルポインタを先頭へ
rewind($f);

# 文字列取得して文字コード変換
$csv = mb_convert_encoding(stream_get_contents($f), 'SJIS-win', 'UTF-8');

# 吐き出し
header('Content-Type: text/csv');
header('Content-Disposition: attachment; filename=FILENAME.csv');
echo $csv;

# 終了
fclose($f);

# なお、呼び出すときhtml側はこうするといいよ!
'
<!-- type="button"にしましょー -->
<form method="get" name="search_form">
    <button type="button">CSVDL</button>
</form>

<script>
    // 別窓を出さないと Resource interpreted as Document but transferred with MIME type text/csv みてーなエラー出る
    $("button[name=search_form]").on("click", function() {
        document.search_form.target = "_blank";
        $("form#search-form").submit();
        document.search_form.target = "";
    });
</script>
';
