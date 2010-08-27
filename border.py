#!/usr/bin/python
import ode
import pygame
from universe import world, space
from consts import *

class Border:
	def __init__(self, x, y, w, h):
		self.x, self.y = coord(x, y)
		self.w, self.h = ra(w), ra(h)
		self.body = b = ode.Body(world)
		b.setPosition((x, y, 0))
		self.geom = g = ode.GeomBox(space, (w, h, 0))
		g.setBody(b)

	def paint(self, surface, coord, ra):
		pygame.draw.rect(surface, (128, 0, 0), (self.x - self.w, self.y - self.h, self.x + self.w, self.y + self.h))
