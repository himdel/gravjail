#!/usr/bin/python
import pygame
from consts import *

pygame.init()
surface = pygame.display.set_mode((xres, yres))

from star import Star
from random import random
from consts import *

class Viewport:
	lx = 0
	ly = 0

	def __init__(self, player = None, w = xres, h = yres, ox = 0, oy = 0, zoom = 170, stars = True):
		self.player = player
		self.ship = player.ship
		self.w = w
		self.h = h
		self.ox = ox
		self.oy = oy

		self.ra = lambda x: int(zoom * x)
		self.xcoord = lambda a, b: lambda x, y: (int(a + self.ra(x)), int(b - self.ra(y)))

		self.star_x = float(w) / zoom
		self.star_y = -float(h) / zoom

		if stars:
			self.stars = [Star(random() * self.star_x, random() * self.star_y) for x in range(50)]
		else:
			self.stars = []


	def move_stars(self, dx, dy):
		for s in self.stars:
			s.x += dx
			s.y += dy

			if (s.x > self.star_x):
				s.x -= self.star_x
				s.y = random() * self.star_y

			if (s.x < 0):
				s.x += self.star_x
				s.y = random() * self.star_y

			if (s.y > 0):
				s.x = random() * self.star_x
				s.y += self.star_y

			if (s.y < self.star_y):
				s.x = random() * self.star_x
				s.y -= self.star_y


	def paint(self, objs):
		sx, sy, sz = self.ship.body.getPosition()

		self.move_stars(self.lx - sx, self.ly - sy)
		for s in self.stars:
			s.paint(self.xcoord(0 + self.ox, 0 + self.oy), self.ra)

		#FIXME: paint only visible ones
		for o in objs + [self.ship]:
			o.paint(self.xcoord(self.w / 2 - self.ra(sx) + self.ox, self.h / 2 + self.ra(sy) + self.oy), self.ra)

		self.lx, self.ly = sx, sy
