<?php

# ==============================
# 画像アップロード and サイズ変更  実験ノート
#     参考: http://dot-town-lab.com/laboratory/item/60    サイズ変更のとこでFatalError出たので廃棄
#     参考: http://qiita.com/mpyw/items/73ee77a9535cc65eff1e    
# ==============================

function bar() {
    $files = $_FILES['uploadFile'];
        # Array(
        #     [name] => Array
        #         (
        #             [0] => bz.jpg
        #             [1] => rockman.jpg
        #         )
        #     [type] => Array
        #         (
        #             [0] => image/jpeg
        #             [1] => image/jpeg
        #         )
        #     [tmp_name] => Array
        #         (
        #             [0] => C:\xampp\tmp\phpFFD3.tmp
        #             [1] => C:\xampp\tmp\phpFFE3.tmp
        #         )
        #     [error] => Array
        #         (
        #             [0] => 0
        #             [1] => 0
        #         )
        #     [size] => Array
        #         (
        #             [0] => 6285
        #             [1] => 25734
        #         )
        # )

    foreach ($_FILES['uploadFile']['error'] as $key => $errorCode) {
        # エラーコードのチェック
        switch ($errorCode) {
            case UPLOAD_ERR_OK:
                $msg = '値: 0; エラーはなく、ファイルアップロードは成功しています。'; break;
            case UPLOAD_ERR_INI_SIZE:
                $msg = '値: 1; アップロードされたファイルは、php.ini の upload_max_filesize ディレクティブの値を超えています。'; break;
            case UPLOAD_ERR_FORM_SIZE:
                $msg = '値: 2; アップロードされたファイルは、HTML フォームで指定された MAX_FILE_SIZE を超えています。'; break;
            case UPLOAD_ERR_PARTIAL:
                $msg = '値: 3; アップロードされたファイルは一部のみしかアップロードされていません。'; break;
            case UPLOAD_ERR_NO_FILE:
                $msg = '値: 4; ファイルはアップロードされませんでした。'; break;
            case UPLOAD_ERR_NO_TMP_DIR:
                $msg = '値: 6; テンポラリフォルダがありません。'; break;
            case UPLOAD_ERR_CANT_WRITE:
                $msg = '値: 7; ディスクへの書き込みに失敗しました。'; break;
            case UPLOAD_ERR_EXTENSION:
                $msg = '値: 8; PHP の拡張モジュールがファイルのアップロードを中止しました。'; break;
        }

        # mimeチェック
        $info = getimagesize($_FILES['uploadFile']['tmp_name'][$key]);
            # Array(
            #     [0] => 240    width
            #     [1] => 240    height
            #     [2] => 2      imagetype
            #     [3] => width="240" height="240"
            #     [bits] => 8
            #     [channels] => 3
            #     [mime] => image/jpeg
            # )
        if (!in_array($info[2], [IMAGETYPE_GIF, IMAGETYPE_JPEG, IMAGETYPE_PNG], true)) {
            $msg .= 'gif,jpg,pngのどれかにしてください。';
        }

        # 縦横比維持、120*120以下、の条件でサイズを決める
        if ($info[0] >= $info[1]) {
            $w = 120;
            $h = ceil(120 * $info[1] / max($info[0], 1));
        } else {
            $w = ceil(120 * $info[0] / max($info[1], 1));
            $h = 120;
        }

        # 画像処理に使う関数名を決定する
        $createFunc = str_replace('/', 'createfrom', $info['mime']);
        $outputFunc = str_replace('/', '', $info['mime']);

        # 元画像リソースを生成する
        $src = $createFunc($_FILES['uploadFile']['tmp_name'][$key]);

        # リサンプリング先画像リソースを生成する
        $dst = imagecreatetruecolor($w, $h);

        # リサンプリング  (コピー先dst,コピー元src,dstX座標,dstY座標,srcX座標,srcY座標,dst幅,dst高さ,src幅,src高さ)
        imagecopyresampled($dst, $src, 0, 0, 0, 0, $w, $h, $info[0], $info[1]);

        # ファイル名を決定して保存する  while文は名前重複チェック
        $saveDir = '/uploadedImages';
        $saveBaseName = 'uploadedImage' . date('YmdHi');
        $saveFileName = $saveBaseName;
        $savePath = "./$saveDir/$saveFileName" . image_type_to_extension($info[2]);
        while (file_exists($savePath)) {
            $saveFileName .= 'n';
            $saveBaseName = $saveFileName;
            $savePath = "./$saveDir/$saveFileName" . image_type_to_extension($info[2]);
        }
        # imagejpeg(画像リソース, 保存先パス)
        $outputFunc($dst, $savePath);

        # リソース解放する
        imagedestroy($src);
        imagedestroy($dst);
    }

}

# ファイル送信されたとき
if (!is_null(filter_input(INPUT_POST, 'submit'))) {
    bar();
}

?>
<html>
<body>

<form action="" method="post" enctype="multipart/form-data">
    <ul>
        <li><input type="file" name="uploadFile[]"></li>
        <li><input type="file" name="uploadFile[]"></li>
    </ul>
    <input type="submit" name="submit">
</form>

<div>
    <pre><?php if (isset($print)) print_r($print); ?></pre>
</div>

</body>
</html>