#!/usr/bin/python

import pygame
from pygame.locals import *

import universe
import viewport

fps = 100
dt = 1.0/fps
clk = pygame.time.Clock()

x = True
while x:
	events = pygame.event.get()
	for e in events:
		if e.type==QUIT:
			x = False
		if e.type==KEYDOWN:
			x = False

	universe.step(dt)

	if not universe.s.alive:
		x = False

	clk.tick(fps)
