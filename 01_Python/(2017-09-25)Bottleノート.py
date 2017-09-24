#!/usr/bin/env python
# coding: utf-8

'''BOTTLEノート
BOTTLEテンプレートノート.tplとペアになってるよ。
下記スクリプトで読み込んでるテンプレートはPython_Server_Retryプロジェクトのbottleに入ってる。
'''

from bottle import route, run, template, request
from bottle import error, redirect, HTTPResponse, static_file


# 一番シンプルですよ。
# http://localhost:8000/1/Wada
@route('/1/:name')
def page_01(name):
    return f'<h1>YO {name}!</h1>'


# テンプレートを使って同じことをしますよ。
# http://localhost:8000/2/Wada
@route('/2/:name')
def page_02(name='CINEVA'):
    a = {
        '1': 'AAA',
        'b': 'BBB',
    }
    return template('template_02', name=name, a=a)


# GET
# http://localhost:8000/3/
@route('/3/')
def page_03():
    # get一覧を見たいならこれですよ。すらすら出てきて満足。
    print(request.query.__dict__)

    get_content = request.query.name
    return template('template_03', get_content=get_content)


# POST
# http://localhost:8000/4/
@route('/4/')
@route('/4/', method='POST')
def page_04():
    # post一覧を見たいならこれですよ。
    print(request.params.__dict__)

    # これだと日本語文字化けする
    post_content = request.forms.get('name')
    # これなら文字化けしない
    post_content = request.forms.name

    return template('template_04', post_content=post_content)


# リダイレクト
# http://localhost:8000/5/ から /4/ へ飛ばしますよ。
@route('/5/')
def page_05():
    return redirect('/4/')


# HTTPステータスコードのハンドリング
@error(404)
def error_404(error):
    # errorの中ではredirect()使えない。
    r = HTTPResponse(status=302)
    r.set_header('Location', '/4/')
    return r


# 静的ファイル
@route('/static/:file_path')
def static(file_path):
    return static_file(file_path, root='./static')


@route('/7/')
def page_07():
    return template('template_07')


run(host='0.0.0.0', port=8000, debug=True, reloader=True)
