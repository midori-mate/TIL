#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

screen_size = (320, 240)

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(u'画像表示'.encode('utf-8'))

backImg = pygame.image.load('funatsukiba.png').convert()
fieImg = pygame.image.load('gazou-fie.png').convert_alpha()
# イメージのロード。引数にはファイル名。戻り値はイメージが描画された surface 。
# convert() はオリジナルのイメージに透明色が指定されてないとき使う。
# _alpha() は透明色が指定されてるとき使う。

'''
planeImg = pygame.image.load('plane.png').convert()
planeImg2 = pygame.image.load('plane.png').convert()
colorkey = planeImg2.get_at((0, 0))
planeImg2.set_colorkey(colorkey, RLEACCEL)
# colorkey は透明色のこと。イメージの左上隅の色を surface.get_at() 関数で取得し透明にする。
'''

while True:
	screen.blit(backImg, (0, 0))
	screen.blit(fieImg, (100, 100))
	pygame.display.update()
	# blit は surface 上に配置(転送)すること。

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

'''
	screen.fill((0, 0, 0))
	screen.blit(planeImg, (100, 100))
	screen.blit(planeImg2, (200, 100))
	pygame.display.update()
'''


# --- ---
'''
def load_image(filename, colorkey = None):
	try:
		image = pygame.image.load(filename)
	except pygame.error, message:
		print 'Cannot load image:', filename
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is - 1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()
# 使い方
planeImag, planeRect = load_image('plane.png', colorkey = - 1)
'''