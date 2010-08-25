#!/usr/bin/python
import ode
import pygame
from math import *
from random import random
from universe import world, space
from viewport import surface

class Ship:
	alive = True

	def __init__(self, x, y, color):
		self.body = b = ode.Body(world)
		self.mass = M = ode.Mass()
		self.angle = random() * 2 * pi
		M.setSphere(250, 0.05)
		b.setMass(M)
		b.setPosition((x, y, 0))
		b.setLinearVel((-1,0,0))
		self.geom = g = ode.GeomSphere(space, 0.05)
		g.setBody(b)
		self.color = color

	def paint(self, coord, ra):
		x, y, z = self.body.getPosition()
		x, y = coord(x, y)
		r = ra(0.05)
		fx1 = cos(self.angle) * 1.8 * r
		fy1 = -sin(self.angle) * 1.8 * r
		fx2 = cos(self.angle + 2 * pi / 3) * r
		fy2 = -sin(self.angle + 2 * pi / 3) * r
		fx3 = cos(self.angle - 2 * pi / 3) * r
		fy3 = -sin(self.angle - 2 * pi / 3) * r

		pygame.draw.polygon(surface, self.color, [
			( x + fx1, y + fy1 ),
			( x + fx2, y + fy2 ),
			( x + fx3, y + fy3 ),
		])

	def acc(self, force):
		fx = cos(self.angle) * force
		fy = sin(self.angle) * force
		self.body.addForce((fx, fy, 0))

	def turn(self, angle):
		self.angle += angle * 0.1
		self.angle %= 2 * pi
