#!/usr/bin/python
'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import data

import pygame
from pygame.locals import *

import random
random.seed()

import universe
import player
import ship
import layout
import consts


def main():
	fps = 100
	dt = 1.0/fps
	clk = pygame.time.Clock()

	import menu
	menu.wait = lambda: clk.tick(fps)
	menu.menu()

	nplayers = 2

	pos = [(1.5, -0.5), (1.5, -1.5), (0.5, -0.5), (0.5, -1.5)]
	pnames = ["yellow", "violet", "cyan", "white"]

	for x in range(nplayers):
		s = ship.Ship(pos[x][0], pos[x][1], consts.pcolors[x])
		player.Player(s, consts.keyConfigs[x], pnames[x])

	layout = layout.Layout(universe.players)

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
				if e.key == K_SPACE:
					import graphics
					graphics.toggle()
				keys[e.key] = 1
			if e.type == KEYUP:
				try:
					del keys[e.key]
				except:
					pass

		if not x:
			break

		for p in universe.players:
			for k in keys.keys():
				p.process_key(k)

		universe.step(dt)
		layout.drawLayout(universe.holes + universe.checkpoints + universe.ships)

		# game over
		x = False
		for s in universe.ships:
			if s.alive:
				x = True

		clk.tick(fps)
