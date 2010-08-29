#!/usr/bin/python
import ode
import pygame
from math import *
from random import random
from universe import world, space, ships
from consts import *

class Ship:
	alive = True
	fx = 0
	fy = 0
	health = 100
	player = None

	def __init__(self, x, y, color):
		self.body = b = ode.Body(world)
		self.body.grobj = self
		self.mass = M = ode.Mass()
		self.angle = random() * 2 * pi
		M.setSphere(ship_mass, 0.05)
		b.setMass(M)
		b.setPosition((x, y, 0))
		b.setLinearVel((-1,0,0))
		self.geom = g = ode.GeomSphere(space, 0.05)
		g.setBody(b)
		self.color = color

	def paint(self, surface, coord, ra):
		if self.alive == False:
			return
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

	def acc(self, force):
		if self.alive == False:
			return
		fx = cos(self.angle) * force
		fy = sin(self.angle) * force
		self.body.addForce((fx, fy, 0))

	def turn(self, angle):
		if self.alive == False:
			return
		self.angle += angle * 0.1
		self.angle %= 2 * pi

	def kill(self, h, msg = "dead"):
		if self.alive == False:
			return
		self.health -= int(h)
		if self.health <= 0:
			self.health = 0
			self.alive = False
			ships.remove(self)
			print "player %s %s" % (self.player.name, msg)
