# coding: utf-8 ファイルのエンコード。

import pygame
# pygame.image, .draw, .mouse といった基本的なモジュール。
from pygame.locals import *
# pygame の様々な定数を格納したモジュール。
# QUIT という定数は pygame.locals.QUIT だが from でインポートして省略して書けるようにしている。
import sys

pygame.init()
# pygame の各モジュールを初期化する関数。 pygame のモジュール使う前には必ず実行。


screen_size = (640, 480)
# 画面サイズ。()は tuple 。
screen = pygame.display.set_mode(screen_size)
# pygame.display.set_mode() という関数がメイン画面を作成する。引数には画面サイズを tuple で渡す。
# pygame では画像描画できる場所を surface という。メイン画面である display surface は set_mode() で作る。
# set_mode() の戻り値は surface オブジェクト。変数 screen に格納。
pygame.display.set_caption(u'Display Surface')
# この関数でメインウィンドウのタイトルバーにキャプションを設定。

while True:
# イベントドリブン方式。ゲームループをずっと回しておき、ユーザの要求(イベント)が来るたびに処理する。
# while True:
#     ゲームオブジェクトの更新
#     ゲームオブジェクトのレンダリング(描画)
#     画面の更新
#     イベント処理、ってのが一般的。
	screen.fill((100, 150, 100))
	# pygame.Surface.fill() surface を単色で塗りつぶす関数。引数には(r, g, b)でタプルで指定。
	# screen は上でも出てきた surface オブジェクト。
	pygame.display.update()
	# この関数は上にある「画面の更新」をする関数。
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
	# sys.exit() は python の関数。 QUIT はウィンドウの x ボタンとかで発生。

