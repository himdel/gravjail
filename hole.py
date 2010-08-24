#!/usr/bin/python
import ode
import pygame
from universe import world, space
from viewport import surface

class Hole:
	def __init__(self, x, y):
		self.body = b = ode.Body(world)
		self.mass = M = ode.Mass()
		M.setSphere(50000, 0.3)
		b.setMass(M)
		b.setPosition((x, y, 0))
		self.geom = g = ode.GeomSphere(space, 0.03)
		g.setBody(b)

	def paint(self, coord, ra):
		x, y, z = self.body.getPosition()
		pygame.draw.circle(surface, (64, 64, 64), coord(x, y), ra(0.5), 0)
		pygame.draw.circle(surface, (56, 56, 56), coord(x, y), ra(0.4), 0)
		pygame.draw.circle(surface, (48, 48, 48), coord(x, y), ra(0.3), 0)
		pygame.draw.circle(surface, (40, 40, 40), coord(x, y), ra(0.2), 0)
		pygame.draw.circle(surface, (32, 32, 32), coord(x, y), ra(0.1), 0)
		pygame.draw.circle(surface, (0, 0, 0), coord(x, y), ra(0.03), 0)
