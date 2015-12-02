<?php

/* ********************
やりたいこと:フォームに入力したものを計算して、その結果をPOSTで飛ばして別窓で表示する

手順
ph.phpのフォームに入力する。/<form id="f"><input type="text" id="a" value=""></form>
そのデータをjavascriptで取り出す。/document.forms["f"].elements["a"].value
取り出したものをてきとうに計算する。/int * 2
hiddenにその結果を入れる。/document.getElementById("hidden").value = int
別窓を作ってPOSTを飛ばす。/function foo()内参照
******************** */

if (isset($_POST["hidden"])) {
    print <<<EOF
<body>
{$_POST["hidden"]}
</body>
EOF;
    exit();
} else {
    print <<<EOF
<head>
<script type="text/javascript">
function foo() {
    var int = parseInt(document.forms["f"].elements["a"].value) * 2;
    document.getElementById("hidden").value = int;
    window.open("about:blank", "new");
    document.f.target = "new";
    document.f.submit();
}
</script>
</head>
<body>
<div>
<form action="ph.php" name="f" method="post">
<input type="hidden" name="hidden" id="hidden" value="">
<input type="text" id="a" value=""></form>
</div>
<input type="button" onclick="foo();">
</body>
EOF;
}
