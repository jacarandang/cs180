import pygame
from pygame.locals import *
from virus import *
from AI import *

class Player():

	def __init__(self, board, thing):
		self.board = board
		self.thing = thing
		
	def hasValidPath(self, board):
		p = []
		cost = 0
		for i in xrange(board.h):
			if board.get(i) == 0:
				n = VirusNode((0, i), board)
				p, cost = DFS(n)
				if p!=[]:
					break
					
			return p != []
		
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
		cost = 400
		for i in xrange(self.board.h):
			if self.board.get(0, i) == 0:
				n = VirusNode((0, i), self.board)
				temp_p, temp_cost = BFS(n)
				if temp_p != []:
					if temp_cost < cost:
						p = temp_p
						cost = temp_cost
					
		group.setActions(p)
		for v in group:
			v.init()
		return group
		