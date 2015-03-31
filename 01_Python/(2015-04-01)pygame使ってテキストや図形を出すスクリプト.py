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

sysfont = pygame.font.SysFont(None, 80)
# font オブジェクトは pygame.font.SysFont() で作成。引数にはフォント名とサイズ。 None で freeansbold.ttf 。
# どんなフォントが使えるかは print pygame.font.get_fonts() で見れる。
# フォントを添付し、使うことも可能。 myfont = pygame.font.Font('myfont.ttf', 16) とかで。

hello1 = sysfont.render('fuckin son of a bitch!', False, (0, 0, 0))
hello2 = sysfont.render('god damn it!', True, (0, 0, 0))
hello3 = sysfont.render('baga-mi-as pula!', True, (250, 100, 100), (100, 100, 250))
# 第一引数は書きたい文字列。第二はアンチエイリアシングを使うかどうか。第三は文字の色。第四は背景色。省略で透明。
# 戻り値はテキストを描画した surface なので、この段階でテキストは画像になった。描画はまだ。

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

	screen.blit(hello1, (20, 50))
	screen.blit(hello2, (20, 150))
	screen.blit(hello3, (20, 350))
	# スクリーンに描画。画面を表す surface である screen に。第二引数には座標をタプルで指定。
	# バックバッファに書き込んだだけなので画面には表示されない。画面更新の pygame.display.update() で表示される。

	pygame.draw.rect(screen, (100, 100, 0), Rect(10, 10, 300, 200)) # 黄色の矩形
	pygame.draw.circle(screen, (100, 0, 0), (320, 240), 100) # 赤の円
	pygame.draw.ellipse(screen, (100, 0, 100), (400, 300, 200, 100)) # 紫の楕円
	pygame.draw.line(screen, (100,100,100), (0, 0), (640, 480)) # 白線
	# 第一引数： surface 指定。第二：色。第三：図形によって違う。第四：線の太さ。空欄で内部塗りつぶし。
	# 塗りつぶす矩形は screen.fill((100, 100, 0), Rect(10, 10, 300, 200)) でもOK.
	# 直線は始点と終点を指定する。

	pygame.display.update()
	# この関数は上にある「画面の更新」をする関数。
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
	# sys.exit() は python の関数。 QUIT はウィンドウの x ボタンとかで発生。

