#!/usr/bin/python
import pygame

from viewport import Viewport, surface
from consts import *

class Layout:
	
	def __init__(self, players):
		self.players = players
		self.vps = []
		for p in players:
			self.vps.append(Viewport(p, xres, yres, ox = 0, oy = 0, zoom = 170))

	def drawLayout(self, arg):
		surface.fill((0, 0, 0))
		for vp in self.vps:
			vp.paint(arg)
		pygame.display.flip()
