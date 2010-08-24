from pygame.locals import *

class Player:

	def __init__(self, ship):
		self.brake = K_s
		self.acc = K_w
		self.left = K_a
		self.right = K_d
		self.ship = ship
	
	def process_key(self, key):
		if key == self.brake:
			self.ship.acc(-1)
		elif key == self.acc:
			self.ship.acc(1)
		elif key == self.left:
			self.ship.turn(1)
		elif key == self.right:
			self.ship.turn(-1)