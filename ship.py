#!/usr/bin/python
import ode
import pygame
from universe import world, space
from viewport import surface

class Ship:
	alive = True

	def __init__(self, x, y):
		self.body = b = ode.Body(world)
		self.mass = M = ode.Mass()
		M.setSphere(250, 0.05)
		b.setMass(M)
		b.setPosition((x, y, 0))
		b.setLinearVel((-0.3,0,0))
		self.geom = g = ode.GeomSphere(space, 0.05)
		g.setBody(b)

	def paint(self, coord, ra):
		x, y, z = self.body.getPosition()
		pygame.draw.circle(surface, (0, 0, 255), coord(x, y), ra(0.05), 0)
