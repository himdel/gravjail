#!/usr/bin/python
import pygame
import data

blackhole = None
ship = None
bonus = None

enabled = False

def toggle():
	global enabled, blackhole
	if enabled:
		enabled = False
		blackhole = None
	else:
		enabled = True
		blackhole = {0: pygame.image.load(data.filepath("blackhole.png"))}

def scale(obj, side):
	if not side in obj:
		obj[side] = pygame.transform.scale(obj[0], (side, side))
	return obj[side]

try:
	toggle()
except:
	print "sorry, no graphics for you"
