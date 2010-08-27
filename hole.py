#!/usr/bin/python
import ode
import pygame
from universe import world, space
from consts import *
import graphics

class Hole:
	def __init__(self, x, y):
		self.body = b = ode.Body(world)
		self.mass = M = ode.Mass()
		M.setSphere(hole_mass, hole_r)
		b.setMass(M)
		b.setPosition((x, y, 0))
		self.geom = g = ode.GeomSphere(space, hole_r)
		g.setBody(b)

	def paint(self, surface, coord, ra):
		x, y, z = self.body.getPosition()

		if graphics.blackhole:
			xx, yy = coord(x - hole_w, y + hole_w)
			side = ra(2 * hole_w)
			surface.blit(graphics.scale(graphics.blackhole, side), (xx, yy, side, side))
		else:
			pygame.draw.circle(surface, (64, 64, 64), coord(x, y), ra(hole_w), 0)
			pygame.draw.circle(surface, (48, 40, 40), coord(x, y), ra(hole_r), 0)
			pygame.draw.circle(surface, (0, 0, 0), coord(x, y), ra(hole_r / 3), 0)
