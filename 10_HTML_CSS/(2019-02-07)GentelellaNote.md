
Gentelella Note GentelellaNote
===

## 場合別 Tips

### テーブルを折り返さない

`<table id="datatable-buttons" class="table table-striped table-bordered nowrap bg-white">`

### Daterangepicker

日本語化。

`<script src="../vendors/moment/locale/ja.js"></script>`

初期化。

```javascript
// デフォルト値を先月～今日にしている。
var today = new Date();
var lastMonth = new Date(today.getFullYear(), today.getMonth()-1, today.getDate());

$('#reservation').daterangepicker({
  startDate: lastMonth.toLocaleDateString(),
  endDate: today.toLocaleDateString(),
  locale: {
    applyLabel: '決定',
    cancelLabel: 'クリア',
  },
});
```

daterangepicker.js 書き換え。

```javascript
// dateHtml の内容を変える。
// var dateHtml = this.locale.monthNames[calendar[1][1].month()] + calendar[1][1].format(" YYYY");
var dateHtml;
if (this.locale.cancelLabel.match(/[A-Za-z]/)) {
  dateHtml = this.locale.monthNames[calendar[1][1].month()] + calendar[1][1].format(" YYYY");
} else {
  dateHtml =  calendar[1][1].format("YYYY") + "年 " + this.locale.monthNames[calendar[1][1].month()]
}
```


### Datetimepicker

```html
<!-- bootstrap-datetimepicker -->
<link href="../vendors/bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.min.css" rel="stylesheet">
<!-- bootstrap-datetimepicker -->
<script src="../vendors/bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js"></script>
```

```javascript
function init_my_monthpicker() {
    if( typeof ($.fn.datetimepicker) === 'undefined') {
        return;
    }

    $('.__monthpicker').datetimepicker({
        format: 'YYYY/MM',
        locale: moment.locale('ja'),  // たぶん moment のインポートが必要、か?
        maxDate: (new Date()).toLocaleDateString(),  // これがあると勝手にデフォルト入力値が上書きされる。今の所解決策見つからず。バグじゃないの?
    });
}
```
