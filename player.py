from pygame.locals import *
from consts import *

class Player:

	def __init__(self, ship, controls):
		self.acc, self.brake, self.left, self.right = controls
		self.ship = ship
	
	def process_key(self, key):
		if key == self.brake:
			self.ship.acc(-ship_acc)
		elif key == self.acc:
			self.ship.acc(ship_acc)
		elif key == self.left:
			self.ship.turn(1)
		elif key == self.right:
			self.ship.turn(-1)
