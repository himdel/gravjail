#!/usr/bin/python

import pygame
from pygame.locals import *

import random
random.seed()

import universe
import player
import layout
import consts

fps = 100
dt = 1.0/fps
clk = pygame.time.Clock()

nplayers = 4
universe.init(nplayers)

players = []
for x in range(nplayers):
	players.append(player.Player(universe.ships[x], consts.keyConfigs[x]))

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

	if not x:
		break

	for p in players:
		for k in keys.keys():
			p.process_key(k)

	universe.step(dt)
	layout.drawLayout(universe.hs + universe.cp + universe.ships)

	# game over
	x = False
	for s in universe.ships:
		if s.alive:
			x = True

	clk.tick(fps)
