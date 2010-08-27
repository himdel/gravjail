#!/usr/bin/python

# global constants
xres = 512 + 384
yres = xres / 4 * 3

#holes_spc = 128
holes_spc = 60
holes_num = 16

ship_acc = 0.2

#hole_mass = 50000
hole_mass = 100000
hole_r = 0.3			# active hole radius
hole_w = 0.5		# visual hole radius

bounds_acc = 0.1	# * distance in

huds_force = (255, 0, 0)
huds_vel = (0, 255, 0)
