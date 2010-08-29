#!/usr/bin/python
import ode

world = ode.World()
space = ode.SimpleSpace()
contactgroup = ode.JointGroup()

ships = []
holes = []
checkpoints = []
players = []

from consts import *
from math import *


#G = 6.67e-11
G = 6.67e-4

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


def collision_handler(data, g1, g2):
	world, contactgroup = data
	contacts = ode.collide(g1, g2)

	m1 = g1.getBody().getMass().mass
	m2 = g2.getBody().getMass().mass
	vx1, vy1, vz1 = g1.getBody().getLinearVel()
	vx2, vy2, vz2 = g2.getBody().getLinearVel()

	bounce = False

	# collision between 2 ships
	if g1.getBody().grobj.__class__ == Ship and g2.getBody().grobj.__class__ == Ship:
		bounce = True
		h = (m1 + m2) * sqrt((vx1 - vx2) ** 2 + (vy1 - vy2) ** 2) / hfactor
		g1.getBody().grobj.kill(h)
		g2.getBody().grobj.kill(h)
	# collision between 2 non-ships
	elif g1.getBody().grobj.__class__ != Ship and g2.getBody().grobj.__class__ != Ship:
		bounce = True
	# ship and hole or checkpoint
	else:
		s, o = None, None
		if g1.getBody().grobj.__class__ == Ship:
			s = g1.getBody().grobj
			o = g2.getBody().grobj
		else:
			s = g2.getBody().grobj
			o = g1.getBody().grobj
		if o.__class__ == Hole:
			s.kill( (m1 + m2) * sqrt((vx1 - vx2) ** 2 + (vy1 - vy2) ** 2) / hfactor )
		elif o.__class__ == Checkpoint:
			o.bump(s)
		else:
			print "wtf?: %s" % o

	if bounce:
		for c in contacts:
			c.setBounce(1)
			c.setMu(500)
			j = ode.ContactJoint(world, contactgroup, c)
			j.attach(g1.getBody(), g2.getBody())


def step(dt):
	# apply gravity on ships
	for h in holes:
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

	# check for victory
	for p in players:
		p.checkpoints = 0

	for c in checkpoints:
		if c.ship == None:
			continue
		c.ship.player.checkpoints += 1

	for p in players:
		if p.checkpoints == checkpoints_num:
			p.ship.kill(p.ship.health, "wins")

	space.collide((world, contactgroup), collision_handler)
	world.step(dt)
	contactgroup.empty()
