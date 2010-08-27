#!/usr/bin/python
import pygame

blackhole = None
ship = None
bonus = None

menubg = pygame.image.load("pic/main.png")

enabled = False

def toggle():
	global enabled, blackhole
	if enabled:
		enabled = False
		blackhole = None
	else:
		enabled = True
		blackhole = {0: pygame.image.load("pic/blackhole.png")}

def scale(obj, side):
	if not side in obj:
		obj[side] = pygame.transform.scale(obj[0], (side, side))
	return obj[side]
