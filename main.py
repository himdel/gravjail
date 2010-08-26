#!/usr/bin/python

import pygame
from pygame.locals import *

import universe
import viewport
import player

fps = 100
dt = 1.0/fps
clk = pygame.time.Clock()

x = True
players = [player.Player(universe.s)]
keys = {}
while x:
	events = pygame.event.get()
	for e in events:
		if e.type == QUIT:
			x = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				x = False
			keys[e.key] = 1
		if e.type == KEYUP:
			try:
				del keys[e.key]
			except:
				pass

	for p in players:
		for k in keys.keys():
			p.process_key(k)

	universe.step(dt, players)

	if not universe.s.alive:
		x = False

	clk.tick(fps)
