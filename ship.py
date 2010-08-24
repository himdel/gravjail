#!/usr/bin/python
import ode
import pygame
from math import *
from random import random
from universe import world, space
from viewport import surface

class Ship:
	alive = True

	def __init__(self, x, y):
		self.body = b = ode.Body(world)
		self.mass = M = ode.Mass()
		self.angle = random() * 2 * pi
		M.setSphere(250, 0.05)
		b.setMass(M)
		b.setPosition((x, y, 0))
		b.setLinearVel((-1,0,0))
		self.geom = g = ode.GeomSphere(space, 0.05)
		g.setBody(b)

	def paint(self, coord, ra):
		x, y, z = self.body.getPosition()
		pygame.draw.circle(surface, (0, 0, 255), coord(x, y), ra(0.05), 0)
		fx = cos(self.angle) * 0.05
		fy = sin(self.angle) * 0.05
		pygame.draw.circle(surface, (255, 0, 0), coord(x + fx, y + fy), ra(0.02), 0)

	def acc(self, force):
		fx = cos(self.angle) * force
		fy = sin(self.angle) * force
		self.body.addForce((fx, fy, 0))
	
	def turn(self, angle):
		self.angle += angle * 0.1
