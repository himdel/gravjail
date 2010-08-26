#!/usr/bin/python
import pygame

from viewport import Viewport
from consts import *

class Layout:
	
	def __init__(players = 1):
		self.players = players
		self.vps = []	
		if players == 1:
			self.vps.append(ViewPort(ship[0], xres, yres, ox = 0, oy = 0, zoom = 170))
		elif players == 2:
			pass
		elif self.players == 3:
		else:

	def drawLayout() {
		for vp in vps:
			vps.paint()
	}
