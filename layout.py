#!/usr/bin/python
import pygame
from pygame.locals import *

from viewport import Viewport, surface
from consts import *

def add_p(vps, player, w, h, l, r):
	main = True
	for z in vp_zoom:
		vps.append((
			Viewport(player, w, h, zoom = z, drawStars = main, drawVectors = main),
			pygame.Rect(l, r, w, h),
		))
		main = False

class Layout:
	def __init__(self, players):
		self.players = players
		self.vps = []

		if len(players) == 1:
			add_p(self.vps, players[0], xres, yres, 0, 0)
		elif len(players) == 2:
			add_p(self.vps, players[0], xres / 2 - 1, yres, 0, 0)
			add_p(self.vps, players[1], xres / 2 - 1, yres, xres / 2, 0)
		elif len(players) == 3:
			add_p(self.vps, players[0], xres / 3 - 1, yres, 0, 0)
			add_p(self.vps, players[1], xres / 3 - 1, yres, xres / 3, 0)
			add_p(self.vps, players[2], xres / 3 - 1, yres, 2 * xres / 3, 0)
		elif len(players) == 4:
			add_p(self.vps, players[0], xres / 2 - 1, yres / 2 - 1, 0, 0)
			add_p(self.vps, players[1], xres / 2 - 1, yres / 2 - 1, xres / 2 + 1, 0)
			add_p(self.vps, players[2], xres / 2 - 1, yres / 2 - 1, 0, yres / 2 + 1)
			add_p(self.vps, players[3], xres / 2 - 1, yres / 2 - 1, xres / 2 + 1, yres / 2 + 1)


	def drawLayout(self, arg):
		surface.fill((0, 0, 0))

		for vp in self.vps:
			vpa, vpb = vp
			vpa.paint(arg)
			surface.blit(vpa.surface, vpb, None, BLEND_ADD)

		# viewport borders
		if len(self.players) == 2:
			pygame.draw.line(surface, (192, 192, 192), (xres / 2, 0), (xres / 2, yres))
		elif len(self.players) == 3:
			pygame.draw.line(surface, (192, 192, 192), (xres / 3, 0), (xres / 3, yres))
			pygame.draw.line(surface, (192, 192, 192), (2 * xres / 3, 0), (2 * xres / 3, yres))
		elif len(self.players) == 4:
			pygame.draw.line(surface, (192, 192, 192), (xres / 2, 0), (xres / 2, yres))
			pygame.draw.line(surface, (192, 192, 192), (0, yres / 2), ( xres, yres / 2))

		pygame.display.flip()
