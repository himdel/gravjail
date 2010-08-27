#!/usr/bin/python
import pygame
from pygame.locals import *

from viewport import surface
import graphics
from consts import *

def single():
	pass

def double():
	pass

def about():
	pass

def quit():
	import sys
	sys.exit(0)


def menu():
	fps = 10
	dt = 1.0/fps
	clk = pygame.time.Clock()
	fnt = pygame.font.SysFont(pygame.font.get_default_font(), 32)

	x = True
	item = 0
	items = [
		("Single player", single),
		("Two players", double),
		("About", about),
		("Quit", quit),
	]
	while x:
		surface.fill((0, 0, 0))
		surface.blit(graphics.menubg, (0, 0, xres, yres), None, BLEND_ADD)

		ii = 0
		for i in items:
			if ii == item:
				c = menu_active_item
			else:
				c = menu_item
			surface.blit(fnt.render(i[0], False, c, (0, 0, 0)), (200, 200 + 100 * ii, 200, 200), None, BLEND_ADD)
			ii += 1

		events = pygame.event.get()
		for e in events:
			if e.type == QUIT:
				x = False
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					x = False
				if e.key == K_DOWN:
					item += 1
					item %= len(items)
				if e.key == K_UP:
					item -= 1
					item %= len(items)
				if e.key == K_RETURN:
					items[item][1]()

		clk.tick(fps)
