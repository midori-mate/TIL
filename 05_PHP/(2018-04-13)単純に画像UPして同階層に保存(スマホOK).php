<?php

# 画像を同階層に保存する関数です。
function saveImage() {

    # アップロードファイル情報。
    $file = $_FILES['uploadFile'];

    # 画像情報。
    $imageInfo = getimagesize($file['tmp_name']);

    # ファイル名を決めて保存します。
    $saveName = 'uploadedFile' . image_type_to_extension($imageInfo[2]);
    move_uploaded_file($file['tmp_name'], $saveName);
    return $saveName;
}


# 画像がアップされてたら同階層に保存します。
$imgTag = '';
if (is_uploaded_file($_FILES['uploadFile']['tmp_name'])) {
    $saveName = saveImage();
    $imgTag = "<img src='$saveName' style='max-width:500px;height:auto;'>";
}


# htmlを出力します。
echo <<<EOF

<html>
  <head>
    <title>たいとるだよー</title>
  </head>

  <body>
    <form action="" method="post" enctype="multipart/form-data">
      <input type="file" name="uploadFile">
      <button type="submit">送信する!</button>
    </form>
    $imgTag
  </body>
</html>

EOF;
