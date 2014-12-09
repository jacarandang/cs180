import pygame
from pygame.locals import *

class TowerPlayer:

	def __init__(self, res, tlist, grid):
		self.actions = []
		self.res = res
		self.tlist = []
		self.grid = grid
		
	def getActions(self):
		pass