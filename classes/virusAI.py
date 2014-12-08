import pygame
from pygame.locals import *
from virus import *
from AI import *
from pickle import *

class Player():

	def __init__(self, board, thing, tower, values = None, atp = None):
		self.board = board
		self.thing = thing
		self.tower = tower
		self.values = values
		self.e = Evaluator(values)
		self.atp = atp
		self.costs = []
		
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
		v2 = Parasite(self.board, self.thing)
		v3 = Bacteria(self.board, self.thing)
		v4 = Virus(self.board, self.thing)
		v5 = Ebola(self.board, self.thing)
		v6 = HIV(self.board, self.thing)
		v7 = Fungi(self.board, self.thing)
		v7.visible = False
		v7.inviPast = True
		v7.name = 'invisible'
		group = VirusGroup()
		group.add()

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
				
		inrange = []
		for pos in p:
			for t in self.tower:
				if t in inrange: continue
				if t.inRange(pos): inrange.append(t)
		
		ntowers = [0 for i in xrange(14)]
		nnames = ["Stem Cell", "Lymphocyte", "Natural Killer Cell", "T-Cell", "B-Cell", "Plasma Cell", "Granulocyte", "Basophil", "Neutrophil", "Eosinophil", "Monocyte", "Macrophage", "Megakaryocyte", "Thrombocyte"]
		for t in inrange:
			for i in xrange(len(nnames)):
				if t.tower_type == nnames[i]:
					ntowers[i] += 1
					break
		
		prop = self.e.eval(ntowers, 6)
		print 10*prop[0], 10*prop[1], 10*prop[2], 10*prop[3], 10*prop[4], 10*prop[5]
		for i in xrange(int(10*prop[0])): group.add(Fungi(self.board, self.thing))
		for i in xrange(int(10*prop[1])): group.add(Parasite(self.board, self.thing))
		for i in xrange(int(10*prop[2])): group.add(Bacteria(self.board, self.thing))
		for i in xrange(int(10*prop[3])): group.add(Virus(self.board, self.thing))
		for i in xrange(int(10*prop[4])): group.add(Ebola(self.board, self.thing))
		for i in xrange(int(10*prop[5])): group.add(HIV(self.board, self.thing))
		
		group.setActions(p)
		
		return group
		
	def getPath(self): 
		board = self.board.board
		for i in xrange(self.board.w):
			for j in xrange(self.board.h):
				if board[i][j]:
					board[i][j] = -1
		
		one = [(-1, 1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		two = [(-1, -1)]
		for t in self.tower:
			d = t.damage * t.shoot
			r = t.radius/30.00
			mid = (t.occupy[-1][0] + t.occupy[0][0])/2, (t.occupy[-1][1] + t.occupy[0][1])/2
			print mid, r
			tl = int(mid[0] - r), int(mid[1] - r)
			br = int(mid[0] + r), int(mid[1] + r)
			print tl
			print tl[0]+ 2*r, tl[1] + 2*r