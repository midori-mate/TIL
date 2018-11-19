<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="/static/janken.css" media="all">
        <title>BOTTLE SERVER</title>
    </head>

    <body>
        ===== ===== BOTTLEテンプレートの書き方ノート ===== =====

        ● 単行python
        % if True:
            <p>Trueだよ</p>
        % end

        ● pythonブロック
        <%
        a = ''
        if True:
            a = 'endはゼッタイ必要'
        end
        %>

        ● 変数アクセス
        {{value}} {{lis[0]}} {{dic['a']}}
        ただしインラインpythonコードはできないっぽい。それがやりたけりゃjinja2を使おう。

        ● 他のテンプレートの読み込み
        % include('テンプレート名', var=テンプレートに渡したい変数)

    </body>
</html>