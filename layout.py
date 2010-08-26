#!/usr/bin/python
import pygame
from pygame.locals import *

from viewport import Viewport, surface
from consts import *

def add_p(vps, player, w, h, l, r):
	vps += [
			((
				Viewport(player, w, h, zoom = 170),
				pygame.Rect(l, r, w, h),
			)),
			((
				Viewport(player, w, h, zoom = 13.6, stars = False),
				pygame.Rect(l, r, w, h),
			)),
			((
				Viewport(player, w, h, zoom = 3.4, stars = False),
				pygame.Rect(l, r, w, h),
			)),
	]

class Layout:

	def __init__(self, players):
		self.players = players
		self.vps = []

		add_p(self.vps, players[0], xres / 2 - 1, yres, 0, 0)
		add_p(self.vps, players[1], xres / 2 - 1, yres, xres / 2 + 1, 0)

#		for p in players:	# test 1 player, 2 pod sebou vp
##			add_p(self.vps, p, xres, yres, 0, 0)
#			add_p(self.vps, p, xres / 2 - 1, yres / 2 - 1, 0, 0)
#			add_p(self.vps, p, xres / 2 - 1, yres / 2 - 1, xres / 2 + 1, 0)
#			add_p(self.vps, p, xres / 2 - 1, yres / 2 - 1, 0, yres / 2 + 1)
#			add_p(self.vps, p, xres / 2 - 1, yres / 2 - 1, xres / 2 + 1, yres / 2 + 1)


	def drawLayout(self, arg):
		surface.fill((0, 0, 0))
		for vp in self.vps:
			vpa, vpb = vp
			vpa.paint(arg)
			surface.blit(vpa.surface, vpb, None, BLEND_ADD)

		pygame.draw.line(surface, (192, 192, 192), (xres / 2, 0), (xres / 2, yres - 1))

		pygame.display.flip()
