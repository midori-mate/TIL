#!/usr/bin/env python
# -*- coding: utf-8 -*-

# マウスに関するイベント
# MOUSEBUTTONDOWN: マウスボタンが押されたとき パラメータ: post, button
# MOUSEBUTTONUP: 離されたとき パラメータ: pos, button
# MOUSEMOTION: カーソル移動したとき パラメータ: pos, rel, buttons

# ぶっちゃけ突然説明が簡潔になったのでよくわかんない。ブチあたったら以下の url へ
# http://aidiary.hatenablog.com/entry/20080506/1275698497

import pygame
from pygame.locals import *
import sys

screen_size = (320, 240)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(u'マウスイベント'.encode('utf-8'))

backImg = pygame.image.load('funatsukiba.png').convert()
fieImg = pygame.image.load('gazou-fie.png').convert_alpha()
# イメージのロード。引数にはファイル名。戻り値はイメージが描画された surface 。
# convert() はオリジナルのイメージに透明色が指定されてないとき使う。
# _alpha() は透明色が指定されてるとき使う。

cur_pos = (0, 0) # フィーの位置
pythons_pos = [] # コピーしたフィーの位置リスト

while True:
	screen.blit(backImg, (0, 0))
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

		# クリックでフィーをコピー
		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			x, y = event.pos
			x -= fieImg.get_width() / 2
			y -= fieImg.get_height() / 2
			pythons_pos.append((x, y)) # フィーの位置を追加

		# マウス移動でフィーを移動
		if event.type == MOUSEMOTION:
			x, y = event.pos
			x -= fieImg.get_width() / 2
			y -= fieImg.get_height() / 2
			cur_pos = (x, y) 

	screen.blit(fieImg, cur_pos)
	for i, j in pythons_pos:
		screen.blit(fieImg, (i, j))

	pygame.display.update()