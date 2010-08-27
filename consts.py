#!/usr/bin/python

from pygame.locals import *

# global constants
xres = 512 + 384
yres = xres / 4 * 3

#holes_spc = 128
holes_spc = 60
holes_num = 16

ship_acc = 0.2

#hole_mass = 50000
hole_mass = 100000
hole_r = 0.3		# active hole radius
hole_w = 0.5		# visual hole radius

bounds_acc = 0.1	# * distance in

huds_force = (255, 0, 0)
huds_vel = (0, 255, 0)

#vp_zoom = [170, 13.6, 3.4]
vp_zoom = [100, 10]

pcolors = [(255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]    # player colors

keyConfigs = [(K_UP, K_DOWN, K_LEFT, K_RIGHT), 
              (K_w, K_s, K_a, K_d), 
              (K_i, K_k, K_j, K_l), 
              (K_8, K_5, K_4, K_6)]
