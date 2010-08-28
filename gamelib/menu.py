#!/usr/bin/python
import pygame
from pygame.locals import *

from viewport import surface
from consts import *
import data

def play(n):
	pass

def about():
	surface.fill((0, 0, 64))
	surface.blit(pabout, (0, 0, xres, yres))
	pygame.display.flip()
	while True:
		events = pygame.event.get()
		for e in events:
			if e.type == QUIT:
				quit()
			if e.type == KEYDOWN:
				return

def quit():
	import sys
	sys.exit(0)

try:
	menubg = pygame.image.load(data.filepath("main.png"))
except:
	menubg = pygame.Surface((xres, yres))

try:
	pabout = pygame.image.load(data.filepath("about.png"))
except:
	pabout = pygame.Surface((xres, yres))

wait = None

def menu():
	fnt = pygame.font.SysFont(pygame.font.get_default_font(), 32)

	x = True
	item = 0
	items = [
		("Single player", lambda: play(1)),
		("Two players", lambda: play(2)),
		("Three players", lambda: play(3)),
		("Four players", lambda: play(4)),
		("About", about),
		("Quit", quit),
	]
	while x:
		surface.fill((0, 0, 64))
		surface.blit(menubg, (0, 0, xres, yres))

		ii = 0
		for i in items:
			if ii == item:
				c = menu_active_item
			else:
				c = menu_item
			surface.blit(fnt.render(i[0], False, c), (256, 200 + 64 * ii, 800, 600))
			ii += 1

		events = pygame.event.get()
		for e in events:
			if e.type == QUIT:
				quit()
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					quit()
				if e.key == K_DOWN:
					item += 1
					item %= len(items)
				if e.key == K_UP:
					item -= 1
					item %= len(items)
				if e.key == K_RETURN:
					items[item][1]()
					x = False	#TODO remove

		pygame.display.flip()
		wait()
