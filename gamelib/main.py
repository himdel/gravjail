#!/usr/bin/python

import pygame
from pygame.locals import *
import random
import universe
import player
import ship
import layout
import consts
import menu
import data
from hole import Hole
from checkpoint import Checkpoint
random.seed()

fps = 100
dt = 1.0/fps
clk = pygame.time.Clock()

def play(nplayers):
	universe.ships = []
	universe.holes = []
	universe.checkpoints = []
	universe.players = []

	pos = [(1.5, -0.5), (1.5, -1.5), (0.5, -0.5), (0.5, -1.5)]
	pnames = ["yellow", "violet", "cyan", "white"]

	for x in range(nplayers):
		s = ship.Ship(pos[x][0], pos[x][1], consts.pcolors[x])
		p = player.Player(s, consts.keyConfigs[x], pnames[x])
		universe.ships.append(s)
		universe.players.append(p)

	for x in range(consts.holes_num):
		h = Hole(random.random() * consts.holes_spc - consts.holes_spc / 2, random.random() * consts.holes_spc - consts.holes_spc / 2)
		universe.holes.append(h)

	for x in range(consts.checkpoints_num):
		universe.checkpoints.append(Checkpoint(random.random() * consts.holes_spc - consts.holes_spc / 2, random.random() * consts.holes_spc - consts.holes_spc / 2))

	game_layout = layout.Layout(universe.players)
	x = True
	keys = {}
	while x:
		events = pygame.event.get()
		for e in events:
			if e.type == QUIT:
				menu.quit()
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
		game_layout.drawLayout(universe.holes + universe.checkpoints + universe.ships)

		# game over
		x = False
		for s in universe.ships:
			if s.alive:
				x = True

		clk.tick(fps)



def main():
	menu.wait = lambda: clk.tick(fps)
	menu.play = play
	menu.menu()
