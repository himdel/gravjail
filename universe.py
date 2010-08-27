#!/usr/bin/python
import ode

world = ode.World()
space = ode.SimpleSpace()

from ship import Ship
from hole import Hole
from checkpoint import Checkpoint
from random import random
from consts import *

hs = [Hole(random() * holes_spc - holes_spc / 2, random() * holes_spc - holes_spc / 2) for x in range(holes_num)]

# to be filled at game start
ships = []

cp = [Checkpoint(random() * holes_spc - holes_spc / 2, random() * holes_spc - holes_spc / 2) for x in range(4)]

#G = 6.67e-11
G = 6.67e-4

# universe initialization, so far only ships are created
def init(nplayers):
	global ships
	ships = []
	pos = [(1.5, -0.5), (1.5, -1.5), (0.5, -0.5), (0.5, -1.5)]
	for x in range(nplayers):
		ships.append(Ship(pos[x][0], pos[x][1], pcolors[x]))

def grav(o1, o2, c = 1):
	x1,y1,z1 = o1.body.getPosition()
	x2,y2,z2 = o2.body.getPosition()

	dx = x1 - x2
	dy = y1 - y2
	d = dx ** 2 + dy ** 2

	dix = 1 if dx > 0 else -1
	diy = 1 if dy > 0 else -1

	m = o1.mass.mass * o2.mass.mass

	if x1 == x2:
		Fx = 0
	else:
		Fx = -G * m * abs(dx) / d * dix

	if y1 == y2:
		Fy = 0
	else:
		Fy = -G * m * abs(dy) / d * diy

	o1.body.addForce((Fx * c, Fy * c, 0))
	o2.body.addForce((-Fx * c, -Fy * c, 0))


#TODO resit ty collision pointy a zjistit ktera lod umrela
def colvec(ss, g1, g2):
	s, s2 = ss
	contacts = ode.collide(g1, g2)
#	for c in contacts:
#		s.alive = False

def step(dt):
	# apply gravity on objects
	for h in hs:
		for s in ships:
			grav(h, s)

	# maintain game borders
	for sh in ships:
		x, y, z = sh.body.getPosition()
		if x < (holes_spc * -0.5):
			d = abs(x - (holes_spc * -0.5))
			sh.body.addForce((bounds_acc * d, 0, 0))
		if x > (holes_spc * +0.5):
			d = abs(x - (holes_spc * +0.5))
			sh.body.addForce((-bounds_acc * d, 0, 0))
		if y < (holes_spc * -0.5):
			d = abs(y - (holes_spc * -0.5))
			sh.body.addForce((0, bounds_acc * d, 0))
		if y > (holes_spc * +0.5):
			d = abs(y - (holes_spc * +0.5))
			sh.body.addForce((0, -bounds_acc * d, 0))

		sh.fx, sh.fy, fz = sh.body.getForce()

	world.step(dt)
	space.collide((ships, hs, cp), colvec)
