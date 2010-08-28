from pygame.locals import *
from consts import *
from universe import players

class Player:
	checkpoints = 0

	def __init__(self, ship, controls, name):
		self.name = name
		self.acc, self.brake, self.left, self.right = controls
		self.ship = ship
		self.ship.player = self
		players.append(self)
	
	def process_key(self, key):
		if self.ship.alive == False:
			return
		if key == self.brake:
			self.ship.acc(-ship_acc)
		elif key == self.acc:
			self.ship.acc(ship_acc)
		elif key == self.left:
			self.ship.turn(1)
		elif key == self.right:
			self.ship.turn(-1)
