#!/usr/bin/python
import pygame
from viewport import surface

class Star:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def paint(self, coord, ra):
		pygame.draw.circle(surface, (255, 255, 255), coord(self.x, self.y), ra(0.001), 0)
