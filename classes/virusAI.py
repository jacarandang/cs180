import pygame
from pygame.locals import *
from virus import *
from AI import *

class Player():

	def __init__(self, board, thing):
		self.board = board
		self.thing = thing
		
	def getNextGroup(self):
		v1 = Virus(self.board, self.thing, 10, 5)
		v2 = Virus(self.board, self.thing,  10, 8)
		v3 = Virus(self.board, self.thing,  10, 10)
		group = VirusGroup()
		group.add(v1, v2, v3)
		
		p = []
		for i in xrange(self.board.h):
			if self.board.get(0, i) == 0:
				n = VirusNode((0, i), self.board)
				p = DFS(n)
				if p != []:
					break
					
		group.setActions(p)
		return group
		