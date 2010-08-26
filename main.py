#!/usr/bin/python

import pygame
from pygame.locals import *

import universe
import player
import layout

fps = 100
dt = 1.0/fps
clk = pygame.time.Clock()

players = [
	player.Player(universe.s, (K_w, K_s, K_a, K_d)),
	player.Player(universe.s2, (K_UP, K_DOWN, K_LEFT, K_RIGHT)),
]
layout = layout.Layout(players)

x = True
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

	universe.step(dt)
	layout.drawLayout(universe.hs + universe.cp + [universe.s, universe.s2])

	if not universe.s.alive:
		x = False

	clk.tick(fps)
