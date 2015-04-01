# coding: utf-8

import pygame
from pygame.locals import *
import sys

scr_width, scr_height = 320, 240

pygame.init()
screen = pygame.display.set_mode((scr_width, scr_height)) # ここは二重にしないとダメ。
pygame.display.set_caption(u'アニメーション'.encode('utf-8'))

img = pygame.image.load('gazou-fie.png').convert_alpha()
img_rect = img.get_rect()

vx = vy = 2 # 1 フレームの移動ピクセル
clock = pygame.time.Clock()

print img_rect

while True:
	clock.tick(60) # 60fps
	# 画像の移動
	img_rect.move_ip(vx, vy)
	# 跳ね返り処理
	if img_rect.left < 0 or img_rect.right > scr_width:
		vx = - vx
	if img_rect.top < 0 or img_rect.bottom > scr_height:
		vy = - vy

	screen.fill((100, 250, 100))
	screen.blit(img, img_rect)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT: sys.exit()
		if event.type == KEYDOWN and event.key == K_ESCAPE: sys.exit()
