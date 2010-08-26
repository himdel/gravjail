#!/usr/bin/python
import ode
import pygame
from math import *
from random import random
from universe import world, space
from consts import *

class Ship:
	alive = True
	fx = 0
	fy = 0
	lives = 5

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

	def paint(self, surface, coord, ra):
		px, py, z = self.body.getPosition()
		x, y = coord(px, py)
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

		#TODO toto kreslit jen na hlavni display
		vx, vy, vz = self.body.getLinearVel()
		pygame.draw.line(surface, huds_vel, (x, y), coord(px + vx * 0.1, py + vy * 0.1))

		pygame.draw.line(surface, huds_force, (x, y), coord(px + self.fx, py + self.fy))

	def acc(self, force):
		fx = cos(self.angle) * force
		fy = sin(self.angle) * force
		self.body.addForce((fx, fy, 0))

	def turn(self, angle):
		self.angle += angle * 0.1
		self.angle %= 2 * pi
