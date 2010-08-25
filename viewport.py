#!/usr/bin/python
import pygame

pygame.init()
surface = pygame.display.set_mode((640, 480))

from star import Star
from random import random

def ra(r):
	return int(170 * r)

def xcoord(a, b):
	return lambda x, y: (int(a + ra(x)), int(b - ra(y)))


class Viewport:
	stars = [Star(random() * 3.764, random() * -2.823) for x in range(50)]
	lx = 0
	ly = 0

	def __init__(self, ship = None, w = 640, h = 480, ox = 0, oy = 0, zoom = 170):
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
			if (s.x > 3.764):
				s.x -= 3.764
				s.y = random() * -2.823

			if (s.x < 0):
				s.x += 3.764
				s.y = random() * -2.823

			if (s.y > 0):
				s.x = random() * 3.764
				s.y -= 2.823

			if (s.y < -2.823):
				s.x = random() * 3.764
				s.y += 2.823


	def paint(self, objs):
		surface.fill((0, 0, 0))
		sx, sy, sz = self.ship.body.getPosition()

		self.move_stars(self.lx - sx, self.ly - sy)
		for s in self.stars:
			s.paint(xcoord(0 + self.ox, 0 + self.oy), ra)

		for o in objs + [self.ship]:
			o.paint(xcoord(320 - ra(sx) + self.ox, 240 + ra(sy) + self.oy), ra)

		pygame.display.flip()
		self.lx, self.ly = sx, sy
