#!/usr/bin/python
import ode
import pygame
from universe import world, space, checkpoints

def mul(a, b):
	return map(lambda x: int(x[0] * x[1]), zip(a, b))

class Checkpoint:
	def __init__(self, x, y):
		self.body = b = ode.Body(world)
		self.body.grobj = self
		b.setPosition((x, y, 0))
		self.ship = None
		self.geom = g = ode.GeomSphere(space, 0.5)
		g.setBody(b)
		checkpoints.append(self)

	def paint(self, surface, coord, ra):
		x, y, z = self.body.getPosition()
		if self.ship:
			c = self.ship.color
			pygame.draw.circle(surface, mul(c, (1.0 / 4, 1.0 / 8, 1.0 / 8)), coord(x, y), ra(0.5), 0)
			pygame.draw.circle(surface, mul(c, (5.0 / 16, 5.0 / 32, 5.0 / 32)), coord(x, y), ra(0.4), 0)
			pygame.draw.circle(surface, mul(c, (3.0 / 8, 3.0 / 16, 3.0 / 16)), coord(x, y), ra(0.3), 0)
			pygame.draw.circle(surface, mul(c, (7.0 / 16, 7.0 / 32, 7.0 / 32)), coord(x, y), ra(0.2), 0)
			pygame.draw.circle(surface, mul(c, (1.0 / 2, 1.0 / 4, 1.0 / 4)), coord(x, y), ra(0.1), 0)
		else:
			pygame.draw.circle(surface, (32, 0, 0), coord(x, y), ra(0.5), 0)
			pygame.draw.circle(surface, (40, 0, 0), coord(x, y), ra(0.4), 0)
			pygame.draw.circle(surface, (48, 0, 0), coord(x, y), ra(0.3), 0)
			pygame.draw.circle(surface, (56, 0, 0), coord(x, y), ra(0.2), 0)
			pygame.draw.circle(surface, (64, 0, 0), coord(x, y), ra(0.1), 0)

	def bump(self, ship):
		self.ship = ship
