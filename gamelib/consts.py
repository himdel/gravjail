#!/usr/bin/python

from pygame.locals import *

# global constants
xres = 800
yres = 600

#holes_spc = 128
holes_spc = 64
holes_num = 10

checkpoints_num = 4

ship_acc = 0.2
ship_mass = 250

#hole_mass = 50000
hole_mass = 150000
hole_r = 0.2		# active hole radius
hole_w = 0.5		# visual hole radius

bounds_acc = 0.1	# * distance in

#hfactor = 1000		# for health loss after collision
hfactor = 0.1

huds_force = (255, 0, 0)
huds_vel = (0, 255, 0)

#vp_zoom = [170, 13.6, 3.4]
vp_zoom = [100, 10]

pcolors = [(255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]    # player colors

keyConfigs = [
	(K_UP, K_DOWN, K_LEFT, K_RIGHT),
	(K_w, K_s, K_a, K_d),
	(K_i, K_k, K_j, K_l),
	(K_8, K_5, K_4, K_6),
]

menu_item = (128, 0, 128)
menu_active_item = (255, 0, 255)
