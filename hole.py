#!/usr/bin/python
import ode
import pygame
from universe import world, space
from viewport import surface

class Hole:
	def __init__(self, x, y):
		self.body = b = ode.Body(world)
		self.mass = M = ode.Mass()
		M.setSphere(250000, 0.1)
		b.setMass(M)
		b.setPosition((x, y, 0))
		self.geom = g = ode.GeomSphere(space, 0.1)
		g.setBody(b)

	def paint(self, coord, ra):
		x, y, z = self.body.getPosition()
		pygame.draw.circle(surface, (64, 64, 64), coord(x, y), ra(0.1), 0)
