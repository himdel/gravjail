#!/usr/bin/python
import pygame

pygame.init()
surface = pygame.display.set_mode((640, 480))

from star import Star
from random import random
from consts import *

def ra(r):
	return int(170 * r)

def xcoord(a, b):
	return lambda x, y: (int(a + ra(x)), int(b - ra(y)))

x_dimMax = 3.764
y_dimMax = 0
y_dimMin = -2.823
x_dimMin = 0

class Viewport:
	stars = [Star(random() * x_dimMax, random() * y_dimMin) for x in range(50)]
	lx = 0
	ly = 0

	def __init__(self, ship = None, w = xres, h = yres, ox = 0, oy = 0, zoom = 170):
		self.ship = ship
		self.w = w
		self.h = h
		self.ox = ox
		self.oy = oy
		# TODO zoom, neignorovat tady toto

	def move_stars(self, dx, dy):
		for s in self.stars:
			s.x += dx
			s.y += dy
			if (s.x > x_dimMax):
				s.x -= x_dimMax
				s.y = random() * y_dimMin

			if (s.x < x_dimMin):
				s.x += x_dimMax
				s.y = random() * y_dimMin

			if (s.y > y_dimMax):
				s.x = random() * x_dimMax
				s.y += y_dimMin

			if (s.y < y_dimMin):
				s.x = random() * x_dimMax
				s.y -= y_dimMin


	def paint(self, objs):
		surface.fill((0, 0, 0))
		sx, sy, sz = self.ship.body.getPosition()

		self.move_stars(self.lx - sx, self.ly - sy)
		for s in self.stars:
			s.paint(xcoord(0 + self.ox, 0 + self.oy), ra)

		#FIXME: paint only visible ones
		for o in objs + [self.ship]:
			o.paint(xcoord(xres/2 - ra(sx) + self.ox, yres/2 + ra(sy) + self.oy), ra)

		pygame.display.flip()
		self.lx, self.ly = sx, sy
