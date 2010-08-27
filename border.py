#!/usr/bin/python
import ode
import pygame
from universe import world, space
from consts import *

class Border:
	def __init__(self, x, y, w, h):
		self.x, self.y = x, y
		self.w, self.h = w, h
		self.body = b = ode.Body(world)
		b.setPosition((x, y, 0))
		self.geom = g = ode.GeomBox(space, (w, h, 0))
		g.setBody(b)

	def paint(self, surface, coord, ra):
		x, y = coord(self.x, self.y)
		w, h = ra(self.w) / 2, ra(self.h) / 2
		pygame.draw.rect(surface, (128, 0, 0), (x - w, y - h, x + w, y + h))
