import pygame
from pygame.locals import *
from virus import *
from AI import *

class Player():

	def __init__(self, board, thing):
		self.board = board
		self.thing = thing
		
	def getNextGroup(self):
		v1 = Fungi(self.board, self.thing)
		v2 = Parasite(self.board, self.thing)
		v3 = Bacteria(self.board, self.thing)
		v4 = Virus(self.board, self.thing)
		v5 = Ebola(self.board, self.thing)
		v6 = HIV(self.board, self.thing)
		group = VirusGroup()
		group.add(v1, v2, v3, v4, v5, v6)
		
		p = []
		for i in xrange(self.board.h):
			if self.board.get(0, i) == 0:
				n = VirusNode((0, i), self.board)
				p = DFS(n)
				if p != []:
					break
					
		group.setActions(p)
		for v in group:
			v.init()
		return group
		