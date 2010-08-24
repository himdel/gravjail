#!/usr/bin/python
import pygame

pygame.init()
surface = pygame.display.set_mode((640, 480))

def ra(r):
	return int(170 * r)

def xcoord(a, b):
	return lambda x, y: (int(a + ra(x)), int(b - ra(y)))

from star import Star
from random import random
stars = [Star(random() * 3.764, random() * -2.823) for x in range(50)]

lx = 0
ly = 0


def move_stars(stars, dx, dy):
	for s in stars:
		s.x += dx
		s.y += dy
		if (s.x > 3.764):
			s.x -= 3.764
			s.y = random() * -2.823

		if (s.x < 0):
			s.x += 3.764
			s.y = random() * -2.823

		if (s.y > 0):
			s.x = random() * 3.764
			s.y -= 2.823

		if (s.y < -2.823):
			s.x = random() * 3.764
			s.y += 2.823


def paint(objs):
	surface.fill((0, 0, 0))
	sx, sy, sz = objs[0].body.getPosition()

	global lx, ly
	move_stars(stars, lx - sx, ly - sy)
	for s in stars:
		s.paint(xcoord(0, 0), ra)

	for o in objs:
		o.paint(xcoord(320 - ra(sx), 240 + ra(sy)), ra)

	pygame.display.flip()
	lx, ly = sx, sy
