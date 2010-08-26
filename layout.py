#!/usr/bin/python
import pygame

from viewport import Viewport, surface
from consts import *

class Layout:
	
	def __init__(self, players):
		self.players = players
		self.vps = []

#		# 3 viewporty, krasa
#		for p in players:
#			self.vps.append(Viewport(p, xres, yres, zoom = 170))
#			self.vps.append(Viewport(p, xres, yres, zoom = 13.6, stars = False))
#			self.vps.append(Viewport(p, xres, yres, zoom = 3.4, stars = False))

		for p in players:	# test 1 player, 2 pod sebou vp
			self.vps.append((
				Viewport(p, xres / 2 - 1, yres, zoom = 170),
			))
			self.vps.append((
				Viewport(p, xres / 2 - 1, yres, zoom = 170),
			))

	def drawLayout(self, arg):
		surface.fill((0, 0, 0))
		for vp in self.vps:
			vpa, vpb = vp
			vpa.paint(arg)
			surface.blit(vpa.surface, vpb)
		pygame.display.flip()
