JavascriptFileUploadNote
===

サーバに送信せず Javascript 内でアップロードファイルを扱いたくない? 扱いたいだろ?

## Jquery 使用

```javascript
$('#input[type=file]のID').on('change', function(){

  // これでファイルを取得できた気がするし、
  // ファイル名とかサイズも取得できるのに内容が取得できない!
  var file = $(this).prop('files')[0];

  // file のもつフィールド。
  console.log(file.lastModified);
  console.log(file.lastModifiedDate);
  console.log(file.name);
  console.log(file.size);
  console.log(file.type);
  console.log(file.webkitRelativePath);

  // 内容を取り出すには FileReader。
  var reader = new FileReader();

  // https://developer.mozilla.org/ja/docs/Web/API/FileReader/onload
  // readAsArrayBuffer や readAsBinaryString、 readAsDataURL、readAsText でのコンテンツ読み込みが完了して、利用可能になると発火する。
  reader.onload = function() {
    console.log(reader.result);
  };

  // 今回は使わないけど base64 エンコーディングされた data: URL の文字列 で取得。
  // こんな感じ data:text/csv;base64,77u/SUQs5ZCN5YmNLOOBi...
  reader.readAsDataURL(file);

  // ファイルの中身を文字列で取得。
  reader.readAsText(file);
  return false;
});
```
