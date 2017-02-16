<?php

# 以下、2016.12.16.
# ブラウザ表示にしたい場合
header('Content-Type: application/pdf');

# ダウンロードにしたい場合
header('Content-Type: application/force-download');
header("Content-Disposition: attachment; filename=filename.pdf");
header('Content-Length: ' . filesize($pdfPath));

# このバッファクリーンがなかったせいでファイルが破損することがあった
// ob_end_clean();
# それは大間違いだった!
# 詳しくは清凉会メモ3参照だが、サーバのバッファ層設定がゼロのときcleanをやるとエラーが出てPDFがめちゃめちゃになる。
# それより、readfile()は理想的なバッファまわしでやってくれるから、サーバのバッファ設定を切るよう以下の処理を加えよう。
while (ob_get_level() > 0) {
    ob_end_flush();
}

# FILE_BINARYの意味は謎
readfile($pdfPath, FILE_BINARY);



# 以下、2016.09.16.
# ファイルタイプを指定
header('Content-Type: application/pdf');

# ファイルサイズを取得し、ダウンロード進捗表示する (ブラウザに直接表示するときは省略)
header('Content-Length: ' . filesize($filePath));

# リネーム指示 (ブラウザに直接表示するときは省略)
header('Content-Disposition: attachment; filename="' . $fileName . '"');

# ダウンロード (容量の大きなファイルはfile_get_contentsじゃなくreadfileで読む)
readfile($filePath);



