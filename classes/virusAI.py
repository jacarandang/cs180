import pygame
from pygame.locals import *
from virus import *
from AI import *

class Player():

	def __init__(self, board):
		self.board = board
		
	def getNextGroup(self):
		v1 = Virus(self.board, 5)
		v2 = Virus(self.board, 10)
		v3 = Virus(self.board, 8)
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
		