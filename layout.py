#!/usr/bin/python
import pygame

from viewport import Viewport
from consts import *

class Layout:
	
	def __init__(self, players):
		self.players = players
		self.vps = []
		self.vps.append(Viewport(players[0].ship, xres, yres, ox = 0, oy = 0, zoom = 170))

	def drawLayout(self, arg):
		for vp in self.vps:
			vp.paint(arg)
