#!/usr/bin/python
import ode
import pygame
from universe import world, space

class Checkpoint:
	def __init__(self, x, y):
		self.body = b = ode.Body(world)
		b.setPosition((x, y, 0))

	def paint(self, surface, coord, ra):
		x, y, z = self.body.getPosition()
		pygame.draw.circle(surface, (32, 0, 0), coord(x, y), ra(0.5), 0)
		pygame.draw.circle(surface, (40, 0, 0), coord(x, y), ra(0.4), 0)
		pygame.draw.circle(surface, (48, 0, 0), coord(x, y), ra(0.3), 0)
		pygame.draw.circle(surface, (56, 0, 0), coord(x, y), ra(0.2), 0)
		pygame.draw.circle(surface, (64, 0, 0), coord(x, y), ra(0.1), 0)
