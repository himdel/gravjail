#!/usr/bin/python
import ode
from viewport import paint

world = ode.World()
space = ode.SimpleSpace()

from ship import Ship
from hole import Hole

h = Hole(1, 1)
h2 = Hole(0, 2)
s = Ship(1.5, 0)


#G = 6.67e-11
G = 6.67e-4
def grav(o1, o2):
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

	o1.body.setForce((Fx, Fy, 0))
	o2.body.setForce((-Fx, -Fy, 0))


def colvec(a, g1, g2):
	contacts = ode.collide(g1, g2)
	for c in contacts:
		a.zij = False




def step(dt):
	grav(h, s)
	grav(h2, s)

#	for p in players:
#		p.viewport.paint([p.ship] + objects)
	paint([s, h, h2])

	space.collide(s, colvec)
	world.step(dt)
